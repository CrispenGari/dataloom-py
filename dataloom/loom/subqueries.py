from dataloom.utils import get_table_fields, get_args, is_collection
from dataloom.types import DIALECT_LITERAL, Include, Filter, Order, Group
from dataloom.model import Model
from dataclasses import dataclass
from typing import Callable, Any, Optional
from dataloom.exceptions import UnknownRelationException
import re


@dataclass(kw_only=True)
class subquery:
    dialect: DIALECT_LITERAL
    _execute_sql: Callable[..., Any]

    def get_find_all_relations(
        self,
        parent: Model,
        includes: list[Include] | Include = [],
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        select: list[str] | str = [],
        order: Optional[list[Order] | Order] = [],
        group: Optional[list[Group] | Group] = [],
    ):
        if not is_collection(includes):
            includes = [includes]
        if not is_collection(select):
            select = [select]
        sql, params = parent._get_select_pk_stm(
            dialect=self.dialect,
            limit=limit,
            offset=offset,
            order=order,
        )
        pks = self._execute_sql(sql, fetchall=True, args=None, _verbose=0)
        data = []
        for (pk,) in pks:
            sql2, fields, _ = parent._get_select_by_pk_stm(
                dialect=self.dialect, select=select
            )
            row = self._execute_sql(sql2, fetchone=True, args=(pk,), _verbose=0)
            relations = self.get_find_by_pk_relations(
                parent=parent, pk=pk, includes=includes
            )
            data.append({**dict(zip(fields, row)), **relations})
        return data

    def get_find_many_relations(
        self,
        parent: Model,
        filters: Optional[Filter | list[Filter]] = None,
        includes: list[Include] | Include = [],
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        select: list[str] | str = [],
        order: Optional[list[Order] | Order] = [],
        group: Optional[list[Group] | Group] = [],
    ):
        if not is_collection(includes):
            includes = [includes]
        if not is_collection(select):
            select = [select]

        sql, params = parent._get_select_pk_stm(
            dialect=self.dialect,
            filters=filters,
            limit=limit,
            offset=offset,
            order=order,
        )
        args = get_args(params)
        pks = self._execute_sql(sql, fetchall=True, args=args, _verbose=0)
        data = []
        for (pk,) in pks:
            sql2, fields, _ = parent._get_select_by_pk_stm(
                dialect=self.dialect, select=select
            )
            row = self._execute_sql(sql2, fetchone=True, args=(pk,), _verbose=0)
            relations = self.get_find_by_pk_relations(
                parent=parent, pk=pk, includes=includes
            )
            allowed = self.get_name_and_alias(includes)
            delete_them = []
            for key, value in relations.items():
                if isinstance(value, dict):
                    if key not in allowed:
                        delete_them.append(key)
                elif is_collection(value):
                    if key not in allowed:
                        delete_them.append(key)

            for key in delete_them:
                del relations[key]

            data.append({**dict(zip(fields, row)), **relations})
        return data

    def get_name_and_alias(self, includes: list[Include]) -> list[tuple]:
        allowed = []
        for include in includes:
            table = include.model._get_table_name()
            alias = include.model.__name__.lower()
            allowed.append(table)
            allowed.append(alias)
        return allowed

    def get_find_one_relations(
        self,
        parent: Model,
        filters: Optional[Filter | list[Filter]] = None,
        includes: list[Include] | Include = [],
        offset: Optional[int] = None,
    ):
        if not is_collection(includes):
            includes = [includes]

        _, _, fks, _ = get_table_fields(parent, dialect=self.dialect)
        sql, params = parent._get_select_pk_stm(
            dialect=self.dialect,
            filters=filters,
            limit=1,
            offset=offset,
            order=[],
        )
        args = get_args(params)
        row = self._execute_sql(sql, args=args, fetchone=True, _verbose=0)
        if row is None:
            return {}
        relations = dict()
        (pk,) = row
        for include in includes:
            _, parent_pk_name, fks, _ = get_table_fields(
                include.model, dialect=self.dialect
            )
            if len(include.include) == 0:
                relations = {
                    **relations,
                    **self.get_one_by_pk(
                        parent=parent, pk=pk, include=include, foreign_keys=fks
                    ),
                }
            else:
                has_one = include.has == "one"
                table_name = include.model._get_table_name().lower()
                key = include.model.__name__.lower() if has_one else table_name
                relations = {
                    **relations,
                    **self.get_one_by_pk(
                        parent=parent, pk=pk, include=include, foreign_keys=fks
                    ),
                }
                _, parent_pk_name, parent_fks, _ = get_table_fields(
                    parent, dialect=self.dialect
                )

                if isinstance(relations[key], dict):
                    _pk = relations[key][re.sub(r'`|"', "", parent_pk_name)]
                    relations[key] = {
                        **relations[key],
                        **self.get_find_by_pk_relations(
                            include.model, _pk, includes=include.include
                        ),
                    }
                else:
                    _pk = (
                        relations[key][0][re.sub(r'`|"', "", parent_pk_name)]
                        if len(relations[key]) != 0
                        else None
                    )
                    if _pk is not None:
                        relations[key] = {
                            **relations[key],
                            **self.get_find_by_pk_relations(
                                include.model, _pk, includes=include.include
                            ),
                        }
        return relations

    def get_find_by_pk_relations(self, parent: Model, pk, includes: list[Include] = []):
        if not is_collection(includes):
            includes = [includes]

        relations = dict()
        for include in includes:
            _, parent_pk_name, fks, _ = get_table_fields(
                include.model, dialect=self.dialect
            )
            if len(include.include) == 0:
                relations = {
                    **relations,
                    **self.get_one_by_pk(
                        parent=parent, pk=pk, include=include, foreign_keys=fks
                    ),
                }
            else:
                has_one = include.has == "one"
                table_name = include.model._get_table_name().lower()
                key = include.model.__name__.lower() if has_one else table_name
                relations = {
                    **relations,
                    **self.get_one_by_pk(
                        parent=parent, pk=pk, include=include, foreign_keys=fks
                    ),
                }
                _, parent_pk_name, parent_fks, _ = get_table_fields(
                    parent, dialect=self.dialect
                )

                if isinstance(relations[key], dict):
                    _pk = relations[key][re.sub(r'`|"', "", parent_pk_name)]
                    relations[key] = {
                        **relations[key],
                        **self.get_find_by_pk_relations(
                            include.model, _pk, includes=include.include
                        ),
                    }

                else:
                    try:
                        _pk = (
                            relations[key][0][re.sub(r'`|"', "", parent_pk_name)]
                            if len(relations[key]) != 0
                            else None
                        )
                        if _pk is not None:
                            if isinstance(relations[key], dict):
                                relations[key] = {
                                    **relations[key],
                                    **self.get_find_by_pk_relations(
                                        include.model, _pk, includes=include.include
                                    ),
                                }

                            else:
                                _, parent_pk_name, parent_fks, _ = get_table_fields(
                                    include.model, dialect=self.dialect
                                )
                                t_name = (
                                    f'"{include.model._get_table_name()}"'
                                    if self.dialect == "postgres"
                                    else f"`{include.model._get_table_name()}`"
                                )
                                fk_name = None
                                for _fk in fks:
                                    if parent._get_table_name() in _fk:
                                        fk_name = (
                                            f'"{_fk[parent._get_table_name()]}"'
                                            if self.dialect == "postgres"
                                            else f"`{_fk[parent._get_table_name()]}`"
                                        )
                                placeholder = "?" if self.dialect == "sqlite" else "%s"
                                orders = [
                                    f'{f'"{order.column}"' if self.dialect == 'postgres' else f"`{order.column}`"} {order.order}'
                                    for order in include.order
                                ]
                                options = [
                                    ""
                                    if include.limit is None
                                    else f"LIMIT {placeholder}",
                                    ""
                                    if include.offset is None
                                    else f"OFFSET {placeholder}",
                                ]
                                orderby = (
                                    ""
                                    if len(orders) == 0
                                    else " ORDER BY " + " ".join(orders)
                                )
                                stmt = f"""
                                    select {parent_pk_name} from {t_name} where {fk_name} = {placeholder}{orderby} {' '.join(options)}
                                """

                                data = []
                                _args = [
                                    a
                                    for a in [pk, include.limit, include.offset]
                                    if a is not None
                                ]
                                pks = self._execute_sql(
                                    stmt, args=_args, fetchall=True, _verbose=1
                                )
                                for (_pk,) in pks:
                                    (
                                        sql2,
                                        fields,
                                        _,
                                    ) = include.model._get_select_by_pk_stm(
                                        dialect=self.dialect, select=include.select
                                    )
                                    row = self._execute_sql(
                                        sql2, fetchone=True, args=(_pk,), _verbose=0
                                    )
                                    relations = self.get_find_by_pk_relations(
                                        parent=include.model,
                                        pk=_pk,
                                        includes=include.include,
                                    )
                                    data.append({**dict(zip(fields, row)), **relations})
                                relations[key] = data
                    except Exception:
                        pass

        return relations

    def get_one_by_pk(
        self, parent: Model, include: Include, pk: Any, foreign_keys: list[dict]
    ):
        _, parent_pk_name, parent_fks, _ = get_table_fields(
            parent, dialect=self.dialect
        )
        here = [fk for fk in foreign_keys if parent._get_table_name() in fk]
        fks = here[0] if len(here) == 1 else dict()
        relations = dict()

        has_one = include.has == "one"
        has_many = include.has == "many"
        table_name = include.model._get_table_name().lower()
        key = include.model.__name__.lower() if has_one else table_name
        if len(fks) == 0:
            here = [fk for fk in parent_fks if include.model._get_table_name() in fk]
            parent_fks = dict() if len(here) == 0 else here[0]
            # this table is a child table meaning that we don't have a foreign key here
            try:
                fk = parent_fks[table_name]
            except KeyError:
                raise UnknownRelationException(
                    f'The table "{parent._get_table_name()}" does not have relations "{table_name}".'
                )
            sql, selected = include.model._get_select_child_by_pk_stm(
                dialect=self.dialect,
                select=include.select,
                parent_pk_name=parent_pk_name,
                parent_table_name=parent._get_table_name(),
                child_foreign_key_name=fk,
                limit=None if has_one else include.limit,
                offset=None if has_one else include.offset,
                order=None if has_one else include.order,
            )
            if has_one:
                rows = self._execute_sql(sql, args=(pk,), fetchone=has_one)
                relations[key] = dict(zip(selected, rows)) if rows is not None else None
            elif has_many:
                args = [
                    arg
                    for arg in [pk, include.limit, include.offset]
                    if arg is not None
                ]
                rows = self._execute_sql(sql, args=args, fetchone=has_one)
                try:
                    relations[key] = [dict(zip(selected, row)) for row in rows]
                except TypeError:
                    raise UnknownRelationException(
                        f'The model "{parent._get_table_name()}" does not maps to "{include.has}" of "{include.model._get_table_name()}".'
                    )

        else:
            # this table is a parent table. then the child is now the parent
            parent_table_name = parent._get_table_name()
            fk = fks[parent_table_name]
            child_pk_name = parent_pk_name
            sql, selected = include.model._get_select_parent_by_pk_stm(
                dialect=self.dialect,
                select=include.select,
                child_pk_name=child_pk_name,
                child_table_name=parent._get_table_name(),
                parent_fk_name=fk,
                limit=None if has_one else include.limit,
                offset=None if has_one else include.offset,
                order=None if has_one else include.order,
            )

            if has_one:
                rows = self._execute_sql(sql, args=(pk,), fetchone=has_one)
                relations[key] = dict(zip(selected, rows)) if rows is not None else None
            elif has_many:
                # get them by fks
                """SELECT FROM POSTS WHERE USERID = ID LIMIT=10, """
                args = [
                    arg
                    for arg in [pk, include.limit, include.offset]
                    if arg is not None
                ]
                rows = self._execute_sql(sql, args=args, fetchall=True)
                relations[key] = [dict(zip(selected, row)) for row in rows]

        return relations

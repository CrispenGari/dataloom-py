from dataloom.utils import get_table_fields, get_args
from dataloom.types import DIALECT_LITERAL, Include, Filter, Order
from dataloom.model import Model
from dataclasses import dataclass
from typing import Callable, Any, Optional
import re


@dataclass(kw_only=True)
class subquery:
    dialect: DIALECT_LITERAL
    _execute_sql: Callable[..., Any]

    def get_find_many_relations(
        self,
        parent: Model,
        filters: Optional[Filter | list[Filter]] = None,
        includes: list[Include] = [],
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        select: list[str] = [],
        order: Optional[list[Order]] = [],
    ):
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
            data.append({**dict(zip(fields, row)), **relations})
        return data

    def get_find_one_relations(
        self,
        parent: Model,
        filters: Optional[Filter | list[Filter]] = None,
        includes: list[Include] = [],
        offset: Optional[int] = None,
    ):
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

    def get_one_by_filters(
        self, parent: Model, include: Include, pk: Any, foreign_keys: list[dict]
    ):
        pass

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
            fk = parent_fks[table_name]
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
                relations[key] = [dict(zip(selected, row)) for row in rows]

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
                args = [
                    arg
                    for arg in [pk, include.limit, include.offset]
                    if arg is not None
                ]
                rows = self._execute_sql(sql, args=args, fetchall=True)
                relations[key] = [dict(zip(selected, row)) for row in rows]

        return relations

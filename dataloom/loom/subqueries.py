from dataloom.utils import get_table_fields
from dataloom.types import DIALECT_LITERAL, Include
from dataloom.model import Model
from dataclasses import dataclass
from typing import Callable, Any


@dataclass(kw_only=True)
class subquery:
    dialect: DIALECT_LITERAL
    _execute_sql: Callable[..., Any]

    def get_find_by_pk_relations(self, parent: Model, pk, includes: list[Include] = []):
        _, parent_pk_name, parent_fks, _ = get_table_fields(
            parent, dialect=self.dialect
        )
        relations = dict()
        for include in includes:
            fields, pk_name, fks, _ = get_table_fields(
                include.model, dialect=self.dialect
            )
            # if foreign key are {} meaning that we are querying from user
            # we need to think about it ??? we select records based on the primary key of the orphan table
            # how about subqueries
            has_one = include.has == "one"
            has_many = include.has == "many"

            table_name = include.model._get_table_name().lower()
            key = include.model.__name__.lower() if has_one else table_name
            if len(fks) == 0:
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
                    relations[key] = (
                        dict(zip(selected, rows)) if rows is not None else None
                    )
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
                    relations[key] = (
                        dict(zip(selected, rows)) if rows is not None else None
                    )
                elif has_many:
                    args = [
                        arg
                        for arg in [pk, include.limit, include.offset]
                        if arg is not None
                    ]
                    rows = self._execute_sql(sql, args=args, fetchall=True)
                    relations[key] = [dict(zip(selected, row)) for row in rows]

        return relations

from typing import Optional
from dataloom.types import Group, DIALECT_LITERAL
from dataloom.exceptions import UnknownColumnException, InvalidFilterValuesException
from dataloom.utils.helpers import is_collection
from dataloom.utils.tables import get_operator


def get_groups(
    fields: list[str],
    dialect: DIALECT_LITERAL,
    table_name: str,
    select: list[str] = [],
    group: Optional[list[Group] | Group] = [],
):
    group_fns = []
    group_columns = []
    having_columns = []
    having_values = []
    return_aggregation_column = True

    n_having = 0
    for g in group:
        if g.having is not None:
            if is_collection(g.having):
                n_having += len(g.having)
            else:
                n_having += 1

    for _group in group:
        if _group.column not in fields:
            raise UnknownColumnException(
                f'The table "{table_name}" does not have a column "{_group.column}".'
            )
        if len(select) != 0 and _group.column not in select:
            raise UnknownColumnException(
                f'The column "{_group.column}" was omitted in selection of records to be grouped.'
            )
        fn = (
            f'{_group.function}("{_group.column}")'
            if dialect == "postgres"
            else f"{_group.function}(`{_group.column}`)"
        )
        return_aggregation_column = _group.return_aggregation_column
        group_fns.append(fn)

        col = f'"{_group.column}"' if dialect == "postgres" else f"`{_group.column}`"
        ph = "?" if dialect == "sqlite" else "%s"
        group_columns.append(col)
        if _group.having is None:
            pass
        elif is_collection(_group.having):
            for hav in _group.having:
                op = get_operator(hav.operator)
                if op == "IN" or op == "NOT IN":
                    if is_collection(hav.value):
                        n_having -= 1
                        having_columns.append(
                            f"{fn} {op} ({', '.join([ph for _ in hav.value])}) {hav.join_next_with if n_having >0 else ''}".strip()
                        )
                        having_values += hav.value
                    else:
                        raise InvalidFilterValuesException(
                            f'The operator "{hav.operator}" value can only be a list, tuple or dictionary but got {type(hav.value)}.'
                        )
                else:
                    if not is_collection(hav.value):
                        n_having -= 1
                        having_columns.append(
                            f"{fn} {op} {ph} {hav.join_next_with if n_having >0 else ''}"
                        )
                        having_values.append(hav.value)
                    else:
                        raise InvalidFilterValuesException(
                            f'The operator "{hav.operator}" value can not be a collection.'
                        )
        else:
            hav = _group.having
            op = get_operator(hav.operator)
            if op == "IN" or op == "NOT IN":
                if is_collection(hav.value):
                    n_having -= 1
                    having_columns.append(
                        f"{fn} {op} ({', '.join([ph for _ in hav.value])}) {hav.join_next_with if  n_having >0 else '' }".strip()
                    )
                    having_values += hav.value
                else:
                    raise InvalidFilterValuesException(
                        f'The operator "{filter.operator}" value can only be a list, tuple or dictionary but got {type(filter.value)} .'
                    )
            else:
                if not is_collection(hav.value):
                    n_having -= 1
                    having_columns.append(
                        f"{fn} {op} {ph} {hav.join_next_with if  n_having > 0 else '' }"
                    )
                    having_values.append(hav.value)
                else:
                    raise InvalidFilterValuesException(
                        f'The operator "{hav.operator}" value can not be a collection.'
                    )

    return (
        group_fns,
        group_columns,
        having_columns,
        having_values,
        return_aggregation_column,
    )

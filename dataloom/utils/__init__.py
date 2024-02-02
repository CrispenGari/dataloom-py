from datetime import datetime


def logger(fn):
    def wrapper(*args, **kwargs):
        sql_statement, file_name, dialect = fn(*args, **kwargs)
        with open(file_name, "a+") as f:
            f.write(
                "[{time}] : Dataloom[{dialect}]: {sql_statement}\n".format(
                    dialect=dialect,
                    time=datetime.now(),
                    sql_statement=sql_statement,
                )
            )
        return sql_statement

    return wrapper


@logger
def logger_function(file_name: str, dialect: str, sql_statement: str) -> None:
    return sql_statement, file_name, dialect

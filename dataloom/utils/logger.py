from datetime import datetime
from dataloom.types import DIALECT_LITERAL


class Colors:
    RESET = "\033[0m"
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    PURPLE = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    BOLD = "\033[1m"


class logger:
    @staticmethod
    def file(fn):
        def wrapper(*args, **kwargs):
            sql_statement, file_name, dialect = fn(*args, **kwargs)
            with open(file_name, "a+") as f:
                f.write(
                    "[{time}] : Loom[{dialect}]: {sql_statement}\n".format(
                        dialect=dialect,
                        time=datetime.now().time(),
                        sql_statement=sql_statement,
                    )
                )
            return sql_statement

        return wrapper

    @staticmethod
    def console(fn):
        def wrapper(*args, **kwargs):
            index, sql_statement, dialect = fn(*args, **kwargs)
            if index % 2 == 0:
                print(
                    Colors.BOLD
                    + Colors.CYAN
                    + f"[{dialect}:{datetime.now().time()}] "
                    + Colors.RESET
                    + Colors.BOLD
                    + Colors.BLUE
                    + f"{sql_statement}"
                    + Colors.RESET
                )
            else:
                print(
                    Colors.BOLD
                    + Colors.CYAN
                    + f"[{dialect}:{datetime.now().time()}] "
                    + Colors.RESET
                    + Colors.BOLD
                    + Colors.GREEN
                    + f"{sql_statement}"
                    + Colors.RESET
                )

            print()
            return index

        return wrapper


@logger.file
def file_logger(file_name: str, dialect: DIALECT_LITERAL, sql_statement: str) -> None:
    return sql_statement, file_name, dialect


@logger.console
def console_logger(
    index: int,
    sql_statement: str,
    dialect: DIALECT_LITERAL,
):
    return index, sql_statement, dialect

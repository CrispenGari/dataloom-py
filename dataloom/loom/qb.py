from typing import Callable, Any, Literal, Optional

from dataloom.types import DIALECT_LITERAL


class qb:
    def __repr__(self) -> str:
        return f"Loom QB<{self.dialect}>"

    def __str__(self) -> str:
        return f"Loom QB<{self.dialect}>"

    def __init__(
        self, _execute_sql: Callable[..., Any], dialect: DIALECT_LITERAL
    ) -> None:
        self.__exc = _execute_sql
        self.dialect = dialect

    def run(
        self,
        sql: str,
        args: Any | None = None,
        fetchone: bool = False,
        fetchmany: bool = False,
        fetchall: bool = False,
        mutation: bool = True,
        bulk: bool = False,
        affected_rows: bool = False,
        operation: Optional[Literal["insert", "update", "delete", "read"]] = None,
        verbose: int = 1,
        is_script: bool = False,
    ):
        """
        run
        -----------

        Execute SQL query with optional parameters.

        Parameters
        ----------
        sql : str
            SQL query to execute.
        args : Any | None, optional
            Parameters for the SQL query. Defaults to None.
        fetchone : bool, optional
            Whether to fetch only one result. Defaults to False.
        fetchmany : bool, optional
            Whether to fetch multiple results. Defaults to False.
        fetchall : bool, optional
            Whether to fetch all results. Defaults to False.
        mutation : bool, optional
            Whether the query is a mutation (insert, update, delete). Defaults to True.
        bulk : bool, optional
            Whether the query is a bulk operation. Defaults to False.
        affected_rows : bool, optional
            Whether to return affected rows. Defaults to False.
        operation : Literal['insert', 'update', 'delete', 'read'] | None, optional
            Type of operation being performed. Defaults to None.
        verbose : int, optional
            Verbosity level for logging. Defaults to 1.
        is_script : bool, optional
            Whether the SQL is a script. Defaults to False.

        Returns
        -------
        Any
            Query result.

        Examples
        --------
        >>> qb = loom.getQueryBuilder()
        ... ids = qb.run("select id from posts;", fetchall=True)
        ... print(ids)
        ...
        """
        return self.__exc(
            sql,
            args=args,
            fetchall=fetchall,
            fetchmany=fetchmany,
            fetchone=fetchone,
            mutation=mutation,
            bulk=bulk,
            affected_rows=affected_rows,
            operation=operation,
            _verbose=verbose,
            _is_script=is_script,
        )

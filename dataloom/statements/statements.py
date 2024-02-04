class MySqlStatements:
    # delete
    DELETE_BY_PK = "DELETE FROM {table_name} WHERE {pk_name} = {pk};"
    DELETE_ONE_WHERE_COMMAND = """
    DELETE FROM {table_name} WHERE {pk_name} IN (
       SELECT {pk_name} FROM  (
                SELECT {pk_name} FROM {table_name} WHERE {filters} LIMIT 1
        ) AS subquery
    );
    """
    DELETE_FIRST_COMMAND = """
    DELETE FROM {table_name} WHERE {pk_name} IN (
       SELECT {pk_name} FROM  (
                SELECT {pk_name} FROM {table_name} LIMIT 1
        ) AS subquery
    );
    """
    DELETE_BULK_WHERE_COMMAND = "DELETE FROM {table_name} WHERE {filters};"
    DELETE_ALL_COMMAND = "DELETE FROM {table_name};"
    # updates
    UPDATE_BY_PK_COMMAND = (
        "UPDATE {table_name} SET {placeholder_values} WHERE {pk_name} = {pk};"
    )
    UPDATE_ONE_WHERE_COMMAND = """
        UPDATE {table_name} SET {placeholder_values} WHERE {pk_name} IN (
            SELECT {pk_name} FROM  (
                SELECT {pk_name} FROM {table_name} WHERE {placeholder_filters} LIMIT 1
            ) AS subquery
        );
        """
    UPDATE_BULK_WHERE_COMMAND = (
        "UPDATE {table_name} SET {placeholder_values} WHERE {placeholder_filters};"
    )

    # dropping table
    DROP_TABLE = "DROP TABLE IF EXISTS {table_name};"
    # getting tables
    GET_TABLES = "SHOW TABLES;"

    # creating table
    CREATE_NEW_TABLE = "CREATE TABLE {table_name} ({fields_name});"
    CREATE_NEW_TABLE_IF_NOT_EXITS = (
        "CREATE TABLE IF NOT EXISTS {table_name} ({fields_name});"
    )
    # insert
    INSERT_COMMAND_ONE = (
        "INSERT INTO {table_name} ({column_names}) VALUES ({placeholder_values});"
    )
    INSERT_COMMAND_MANY = (
        "INSERT INTO {table_name} ({column_names}) VALUES ({placeholder_values});"
    )

    # selecting data
    SELECT_COMMAND = "SELECT {column_names} FROM {table_name};"
    SELECT_BY_PK = "SELECT {column_names} FROM {table_name} WHERE {pk_name} = {pk};"
    SELECT_WHERE_COMMAND = "SELECT {column_names} FROM {table_name} WHERE {filters};"


class Sqlite3Statements:
    # delete
    DELETE_BY_PK = "DELETE FROM {table_name} WHERE {pk_name} = {pk};"
    DELETE_ONE_WHERE_COMMAND = """
    DELETE FROM {table_name} WHERE {pk_name} = (
        SELECT {pk_name} FROM  {table_name} WHERE {filters} LIMIT 1
    );
    """
    DELETE_FIRST_COMMAND = """
    DELETE FROM {table_name} WHERE {pk_name} = (
        SELECT {pk_name} FROM  {table_name}LIMIT 1
    );
    """
    DELETE_BULK_WHERE_COMMAND = "DELETE FROM {table_name} WHERE {filters};"
    DELETE_ALL_COMMAND = "DELETE FROM {table_name};"

    # updates
    UPDATE_BY_PK_COMMAND = (
        "UPDATE {table_name} SET {placeholder_values} WHERE {pk_name} = {pk};"
    )
    UPDATE_ONE_WHERE_COMMAND = """
        UPDATE {table_name} SET {placeholder_values} WHERE {pk_name} = (
            SELECT {pk_name} FROM  {table_name} WHERE {placeholder_filters} LIMIT 1
        );
        """
    UPDATE_BULK_WHERE_COMMAND = (
        "UPDATE {table_name} SET {placeholder_values} WHERE {placeholder_filters};"
    )

    # selecting data
    SELECT_COMMAND = "SELECT {column_names} FROM {table_name};"
    SELECT_BY_PK = "SELECT {column_names} FROM {table_name} WHERE {pk_name} = {pk};"
    SELECT_WHERE_COMMAND = "SELECT {column_names} FROM {table_name} WHERE {filters};"

    # dropping table
    DROP_TABLE = "DROP TABLE IF EXISTS {table_name};"
    # getting tables
    GET_TABLES = "SELECT name FROM sqlite_master WHERE type='{type}';"

    # creating table
    CREATE_NEW_TABLE = "CREATE TABLE {table_name} ({fields_name});"
    CREATE_NEW_TABLE_IF_NOT_EXITS = (
        "CREATE TABLE IF NOT EXISTS {table_name} ({fields_name});"
    )
    # insterting
    INSERT_COMMAND_ONE = (
        "INSERT INTO {table_name} ({column_names}) VALUES ({placeholder_values});"
    )
    INSERT_COMMAND_MANY = (
        "INSERT INTO {table_name} ({column_names}) VALUES ({placeholder_values});"
    )


class PgStatements:
    # updates
    UPDATE_BY_PK_COMMAND = (
        "UPDATE {table_name} SET {placeholder_values} WHERE {pk_name} = {pk};"
    )
    UPDATE_ONE_WHERE_COMMAND = """
        UPDATE {table_name} SET {placeholder_values} WHERE {pk_name} = (
            SELECT {pk_name} FROM  {table_name} WHERE {placeholder_filters} LIMIT 1
        );
        """
    UPDATE_BULK_WHERE_COMMAND = (
        "UPDATE {table_name} SET {placeholder_values} WHERE {placeholder_filters};"
    )
    # delete
    DELETE_BY_PK = "DELETE FROM {table_name} WHERE {pk_name} = {pk};"
    DELETE_ONE_WHERE_COMMAND = """
    DELETE FROM {table_name} WHERE {pk_name} = (
        SELECT {pk_name} FROM  {table_name} WHERE {filters} LIMIT 1
    );
    """
    DELETE_FIRST_COMMAND = """
    DELETE FROM {table_name} WHERE {pk_name} = (
        SELECT {pk_name} FROM  {table_name}LIMIT 1
    );
    """
    DELETE_BULK_WHERE_COMMAND = "DELETE FROM {table_name} WHERE {filters};"
    DELETE_ALL_COMMAND = "DELETE FROM {table_name};"
    # select
    SELECT_COMMAND = "SELECT {column_names} FROM {table_name};"
    SELECT_BY_PK = "SELECT {column_names} FROM {table_name} WHERE {pk_name} = {pk};"
    SELECT_WHERE_COMMAND = "SELECT {column_names} FROM {table_name} WHERE {filters};"
    # insert
    INSERT_COMMAND_ONE = "INSERT INTO {table_name} ({column_names}) VALUES ({placeholder_values}) RETURNING {pk};"
    INSERT_COMMAND_MANY = "INSERT INTO {table_name} ({column_names}) VALUES ({placeholder_values}) RETURNING *;"

    # creating table
    CREATE_NEW_TABLE = "CREATE TABLE {table_name} ({fields_name});"
    CREATE_NEW_TABLE_IF_NOT_EXITS = (
        "CREATE TABLE IF NOT EXISTS {table_name} ({fields_name});"
    )
    # altering tables

    # getting tables
    GET_TABLES = (
        "SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='{schema_name}';"
    )
    # dropping tables
    DROP_TABLE = "DROP TABLE IF EXISTS {table_name} CASCADE;"

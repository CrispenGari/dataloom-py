class Statements:
    # select
    SELECT_COMMAND = "SELECT {column_names} FROM {table_name};"
    SELECT_BY_PK = "SELECT {column_names} FROM {table_name} WHERE {pk_name}={pk};"
    SELECT_WHERE_COMMAND = "SELECT {column_names} FROM {table_name} WHERE {filters};"
    # insert
    INSERT_COMMAND = "INSERT INTO {table_name} ({column_name}) VALUES ( {placeholder_values} ) RETURNING *;"
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
    DROP_TABLE = "DROP TABLE IF EXISTS {table_name};"

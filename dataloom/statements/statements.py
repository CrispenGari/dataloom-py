class MySqlStatements:
    # Altering tables

    ALTER_TABLE_COMMAND = """
        -- Begin a transaction
        START TRANSACTION;
            {alterations}
        -- Commit the transaction
        COMMIT;
    
    """

    # describing tables

    DESCRIBE_TABLE_COMMAND = """
        SELECT {fields}
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE table_schema = {db_name} 
        AND table_name = {table_name};
    """

    # delete
    DELETE_BY_PK = "DELETE FROM {table_name} WHERE {pk_name} = {pk};"
    DELETE_ONE_WHERE_COMMAND = """
    DELETE FROM {table_name} WHERE {pk_name} IN (
       SELECT {pk_name} FROM  (
                SELECT {pk_name} FROM {table_name} WHERE {filters} {orders} LIMIT 1 {offset}
        ) AS subquery
    );
    """
    DELETE_FIRST_COMMAND = """
    DELETE FROM {table_name} WHERE {pk_name} IN (
       SELECT {pk_name} FROM  (
                SELECT {pk_name} FROM {table_name} {orders} LIMIT 1 {offset}
        ) AS subquery
    );
    """
    DELETE_BULK_WHERE_COMMAND = """
         DELETE FROM {table_name} WHERE {pk_name} IN (
            SELECT {pk_name} FROM (
                SELECT {pk_name} FROM  {table_name} WHERE {filters} {orders} {limit} {offset}
            ) AS subquery
        );
    """

    DELETE_ALL_COMMAND = """
        DELETE FROM {table_name} WHERE {pk_name} IN (
             SELECT {pk_name} FROM (
                SELECT {pk_name} FROM {table_name} {orders} {limit} {offset}
            ) AS subquery
        );
    """
    # updates
    INCREMENT_DECREMENT_COMMAND = (
        "UPDATE {table_name} SET {placeholder_values} WHERE {placeholder_filters};"
    )
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
    SELECT_COMMAND = "SELECT {column_names} FROM {table_name} {options};".strip()
    SELECT_BY_PK = "SELECT {column_names} FROM {table_name} WHERE {pk_name} = {pk};"
    SELECT_WHERE_COMMAND = (
        "SELECT {column_names} FROM {table_name} WHERE {filters} {options};".strip()
    )

    # ------------- child parent bidirectional sub queries
    SELECT_CHILD_BY_PK = """
    SELECT {child_column_names} FROM {child_table_name} WHERE {child_pk_name} IN (
        SELECT {child_foreign_key_name} FROM  (
                    SELECT {child_foreign_key_name} FROM {parent_table_name} WHERE {parent_pk_name} = {parent_pk}
        ) AS subquery
    ) {orders} {limit} {offset};
    """
    SELECT_PARENT_BY_PK = """
    SELECT {parent_column_names} FROM {parent_table_name} WHERE {parent_fk_name} IN (
        SELECT {child_pk_name} FROM  (
                    SELECT {child_pk_name} FROM {child_table_name} WHERE {child_pk_name} = {child_pk}
        ) AS subquery
    ) {orders} {limit} {offset};
    """

    GET_PK_COMMAND = "SELECT {pk_name} FROM {table_name} {filters} {options};".strip()

    # -------------- subqueries

    SELECT_BY_PK_INCLUDE_COMMAND = """
        SELECT 
            {parent_columns},
            {child_columns}
        FROM 
            {parent_table_name} parent
        {joins}
        WHERE 
            parent.{parent_pk_name} = {parent_pk};
    """

    SELECT_WHERE_INCLUDE_COMMAND = """
        SELECT 
            {parent_columns},
            {child_columns}
        FROM 
            {parent_table_name} parent
        {joins}
        WHERE 
            {filters} {options}
        ;
    """
    SELECT_INCLUDE_COMMAND = """
        SELECT 
            {parent_columns},
            {child_columns}
        FROM 
            {parent_table_name} parent
        {joins}
        {options}
        ;
    """


class Sqlite3Statements:
    # Altering tables

    ALTER_TABLE_COMMAND = """
    -- Begin a transaction
    BEGIN TRANSACTION;
    
    -- Create a new table with the desired schema
    {create_new_table_command}

    -- Copy data from the old table to the new one
    INSERT INTO {new_table_name} ({new_table_columns})
    SELECT {new_table_columns}
    FROM {old_table_name};

    -- Drop the old table
    DROP TABLE {old_table_name};

    -- Rename the new table to the original table name
    ALTER TABLE {new_table_name} RENAME TO {old_table_name};
    
    -- Commit the transaction
    COMMIT;
    """
    # describing table

    DESCRIBE_TABLE_COMMAND = """PRAGMA table_info({table_name});"""
    # delete
    DELETE_BY_PK = "DELETE FROM {table_name} WHERE {pk_name} = {pk};"
    DELETE_ONE_WHERE_COMMAND = """
    DELETE FROM {table_name} WHERE {pk_name} = (
        SELECT {pk_name} FROM  {table_name} WHERE {filters} {orders} LIMIT 1 {offset}
    );
    """
    DELETE_FIRST_COMMAND = """
    DELETE FROM {table_name} WHERE {pk_name} = (
        SELECT {pk_name} FROM  {table_name} {orders} LIMIT 1 {offset}
    );
    """
    DELETE_BULK_WHERE_COMMAND = """
         DELETE FROM {table_name} WHERE {pk_name} IN (
            SELECT {pk_name} FROM {table_name} WHERE {filters} {orders} {limit} {offset}
        );
    """
    DELETE_ALL_COMMAND = """
        DELETE FROM {table_name} WHERE {pk_name} IN (
            SELECT {pk_name} FROM {table_name} {orders} {limit} {offset}
        );
    """

    # updates
    INCREMENT_DECREMENT_COMMAND = (
        "UPDATE {table_name} SET {placeholder_values} WHERE {placeholder_filters};"
    )
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
    SELECT_COMMAND = "SELECT {column_names} FROM {table_name} {options};".strip()
    SELECT_BY_PK = "SELECT {column_names} FROM {table_name} WHERE {pk_name} = {pk};"
    SELECT_WHERE_COMMAND = (
        "SELECT {column_names} FROM {table_name} WHERE {filters} {options};".strip()
    )

    # ------------- child parent bidirectional sub queries
    SELECT_CHILD_BY_PK = """
    SELECT {child_column_names} FROM {child_table_name} WHERE {child_pk_name} IN (
        SELECT {child_foreign_key_name} FROM {parent_table_name} WHERE {parent_pk_name} = {parent_pk}
    ) {orders} {limit} {offset};
    """
    SELECT_PARENT_BY_PK = """
    SELECT {parent_column_names} FROM {parent_table_name} WHERE {parent_fk_name} IN (
        SELECT {child_pk_name} FROM {child_table_name} WHERE {child_pk_name} = {child_pk}
    ) {orders} {limit} {offset};
    """
    GET_PK_COMMAND = "SELECT {pk_name} FROM {table_name} {filters} {options};".strip()

    # -------------- subqueries

    SELECT_BY_PK_INCLUDE_COMMAND = """
        SELECT 
            {parent_columns},
            {child_columns}
        FROM 
            {parent_table_name} parent
        {joins}
        WHERE 
            parent.{parent_pk_name} = {parent_pk};
    """

    SELECT_WHERE_INCLUDE_COMMAND = """
        SELECT 
            {parent_columns},
            {child_columns}
        FROM 
            {parent_table_name} parent
        {joins}
        WHERE 
            {filters} {options}
        ;
    """
    SELECT_INCLUDE_COMMAND = """
        SELECT 
            {parent_columns},
            {child_columns}
        FROM 
            {parent_table_name} parent
        {joins}
        {options}
        ;
    """

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
    # Altering tables

    ALTER_TABLE_COMMAND = """
    {alterations}
    """
    # describing table
    DESCRIBE_TABLE_COMMAND = """
    SELECT {fields}
        FROM information_schema.columns
        WHERE table_schema = {table_schema}
        AND table_name = {table_name};
    """
    # updates
    INCREMENT_DECREMENT_COMMAND = (
        "UPDATE {table_name} SET {placeholder_values} WHERE {placeholder_filters};"
    )
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
        SELECT {pk_name} FROM  {table_name} WHERE {filters} {orders} LIMIT 1 {offset}
    );
    """
    DELETE_FIRST_COMMAND = """
    DELETE FROM {table_name} WHERE {pk_name} = (
        SELECT {pk_name} FROM  {table_name} {orders} LIMIT 1 {offset}
    );
    """
    DELETE_BULK_WHERE_COMMAND = """
         DELETE FROM {table_name} WHERE {pk_name} IN (
            SELECT {pk_name} FROM {table_name} WHERE {filters} {orders} {limit} {offset}
        );
    """
    DELETE_ALL_COMMAND = """
        DELETE FROM {table_name} WHERE {pk_name} IN (
            SELECT {pk_name} FROM {table_name} {orders} {limit} {offset}
        );
    """

    # select
    SELECT_COMMAND = "SELECT {column_names} FROM {table_name} {options};".strip()
    SELECT_BY_PK = "SELECT {column_names} FROM {table_name} WHERE {pk_name} = {pk};"
    SELECT_WHERE_COMMAND = (
        "SELECT {column_names} FROM {table_name} WHERE {filters} {options};".strip()
    )

    # ------------- child parent bidirectional sub queries
    SELECT_CHILD_BY_PK = """
    SELECT {child_column_names} FROM {child_table_name} WHERE {child_pk_name} IN (
        SELECT {child_foreign_key_name} FROM {parent_table_name} WHERE {parent_pk_name} = {parent_pk}
    ) {orders} {limit} {offset};
    """
    SELECT_PARENT_BY_PK = """
    SELECT {parent_column_names} FROM {parent_table_name} WHERE {parent_fk_name} IN (
        SELECT {child_pk_name} FROM {child_table_name} WHERE {child_pk_name} = {child_pk}
    ) {orders} {limit} {offset};
    """

    GET_PK_COMMAND = "SELECT {pk_name} FROM {table_name} {filters} {options};".strip()
    # -------------- subqueries

    SELECT_BY_PK_INCLUDE_COMMAND = """
        SELECT 
            {parent_columns},
            {child_columns}
        FROM 
            {parent_table_name} parent
        {joins}
        WHERE 
            parent.{parent_pk_name} = {parent_pk};
    """

    SELECT_WHERE_INCLUDE_COMMAND = """
        SELECT 
            {parent_columns},
            {child_columns}
        FROM 
            {parent_table_name} parent
        {joins}
        WHERE 
            {filters} {options}
        ;
    """
    SELECT_INCLUDE_COMMAND = """
        SELECT 
            {parent_columns},
            {child_columns}
        FROM 
            {parent_table_name} parent
        {joins}
        {options}
        ;
    """

    # insert
    INSERT_COMMAND_ONE = "INSERT INTO {table_name} ({column_names}) VALUES ({placeholder_values}) RETURNING {pk_name};"
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

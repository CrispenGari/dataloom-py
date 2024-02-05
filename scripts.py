SELECT_BY_PK_INCLUDE_COMMAND = """
    SELECT 
        {parent_columns}
        {child_columns}
    FROM 
        {parent_table_name} parent
    {joins}
    WHERE 
        parent.{parent_pk_name} = {parent_pk};
"""

# Example usage
relationships = [
    {
        "table_name": "users",
        "fk": "userId",
        "pk_name": "id",
        "alias": "author",
        "columns": ["id", "username"],
    },
    {
        "table_name": "reactions",
        "fk": "post_id",
        "pk_name": "id",
        "alias": "reaction",
        "columns": ["id", "reaction_type", "user_id"],
    },
]

table_names = {
    "parent_table_name": "posts",
    "parent_columns": ["id", "title"],
    "parent_pk_name": "id",
    "parent_pk": 2,
}

# Build JOIN clauses and SELECT columns dynamically
joins = ""
parent_columns = ", ".join(
    [
        f"parent.{col} AS \"{table_names['parent_table_name']}_{col}\""
        for col in table_names["parent_columns"]
    ]
)
child_columns = ""

for rel in relationships:
    joins += f"JOIN {rel['table_name']} {rel['alias']} ON parent.{rel['fk']} = {rel['alias']}.{rel['pk_name']} "
    child_columns += ", ".join(
        [
            f"{rel['alias']}.{col} AS \"{rel['table_name']}_{col}\""
            for col in rel["columns"]
        ]
    )


columns = [*parent_columns, *child_columns]

table_names["joins"] = joins
table_names["child_columns"] = child_columns
table_names["parent_columns"] = parent_columns

formatted_query = SELECT_BY_PK_INCLUDE_COMMAND.format(**table_names)
print(formatted_query)


SELECT_BY_PK_INCLUDE_COMMAND = """
    SELECT 
        parent.id AS "{parent_table_name}ID",
        parent.title AS "{parent_table_name}Title",
        {child_columns}
    FROM 
        {parent_table_name} parent
    {joins}
    WHERE 
        parent.{parent_pk_name} = {parent_pk};
    """

# Example usage
relationships = [
    {"table_name": "users", "fk": "userId", "pk_name": "id", "alias": "author"},
    {"table_name": "reactions", "fk": "post_id", "pk_name": "id", "alias": "reaction"},
]

table_names = {
    "parent_table_name": "posts",
    "parent_pk_name": "id",
    "parent_pk": 2,
}

# Build JOIN clauses and SELECT columns dynamically
joins = ""
columns = ""
for rel in relationships:
    joins += f"JOIN {rel['table_name']} {rel['alias']} ON parent.{rel['fk']} = {rel['alias']}.{rel['pk_name']} "
    columns += f",{rel['alias']}.id AS \"{rel['table_name']}ID\", {rel['alias']}.username AS \"{rel['table_name']}Username\""

table_names["joins"] = joins
table_names["child_columns"] = columns

formatted_query = SELECT_BY_PK_INCLUDE_COMMAND.format(**table_names)
print(formatted_query)

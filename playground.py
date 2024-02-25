from dataloom import (
    Loom,
    Model,
    PrimaryKeyColumn,
    Column,
    CreatedAtColumn,
    UpdatedAtColumn,
    TableColumn,
    ForeignKeyColumn,
    Filter,
    ColumnValue,
    Include,
    Order,
    Group,
    Having,
)

"""
 ALTER TABLE "users" ALTER COLUMN "bio" TYPE VARCHAR(200),
 ALTER COLUMN "bio" DROP DEFAULT, ALTER COLUMN "bio" SET DEFAULT 'Hello world', ALTER COLUMN "bio" DROP NOT NULL, DROP CONSTRAINT IF EXISTS  "unique_bio";

            ALTER TABLE "users" ALTER COLUMN "name" TYPE TEXT, ALTER COLUMN "name" DROP DEFAULT, ALTER COLUMN "name" SET DEFAULT 'Bob', ALTER COLUMN "name" DROP NOT NULL, ALTER COLUMN "name" SET NOT NULL, DROP CONSTRAINT IF EXISTS  "unique_name";
            ALTER TABLE "users" ADD "p" BIGSERIAL REFERENCES "profiles"("id") ON DELETE SET NULL; 
            ALTER TABLE "users" ALTER COLUMN "tokenVersion" TYPE INTEGER, ALTER COLUMN "tokenVersion" DROP DEFAULT, ALTER COLUMN "tokenVersion" SET DEFAULT '0', ALTER COLUMN "tokenVersion" DROP NOT NULL, DROP CONSTRAINT IF EXISTS  "unique_tokenVersion";
            ALTER TABLE "users" ALTER COLUMN "username" TYPE VARCHAR(255), ALTER COLUMN "username" DROP DEFAULT, ALTER COLUMN "username" DROP NOT NULL, DROP CONSTRAINT IF EXISTS  "unique_username", ADD CONSTRAINT "unique_username" UNIQUE ("username");
            ALTER TABLE "users" DROP COLUMN "p";
"""
from dataloom.decorators import initialize
import json, time
from typing import Optional
from dataclasses import dataclass

sqlite_loom = Loom(
    connection_uri="sqlite://hello/database.db",
    dialect="sqlite",
    database="hi.db",
    logs_filename="sqlite-logs.sql",
    sql_logger="console",
)


pg_loom = Loom(
    connection_uri="postgresql://postgres:root@localhost:5432/hi",
    dialect="postgres",
    sql_logger="console",
)

mysql_loom = Loom(
    connection_uri="mysql://root:root@localhost:3306/hi",
    dialect="mysql",
    sql_logger="console",
)


class User(Model):
    __tablename__: TableColumn = TableColumn(name="users")
    id = PrimaryKeyColumn(type="int", auto_increment=True)
    name = Column(type="text", nullable=False, default="Bob")
    username = Column(type="varchar", unique=True, length=255)
    tokenVersion = Column(type="int", default=0)


class Post(Model):
    __tablename__: TableColumn = TableColumn(name="posts")
    id = PrimaryKeyColumn(type="int", auto_increment=True, nullable=False, unique=True)
    completed = Column(type="boolean", default=False)
    title = Column(type="varchar", length=255, nullable=False)
    # timestamps
    createdAt = CreatedAtColumn()
    # relations
    userId = ForeignKeyColumn(
        User,
        maps_to="1-N",
        type="int",
        required=True,
        onDelete="CASCADE",
        onUpdate="CASCADE",
    )


conn, tables = mysql_loom.connect_and_sync([User, Post], drop=True, force=True)

userId = mysql_loom.insert_one(
    instance=User,
    values=ColumnValue(name="username", value="@miller"),
)

for title in ["Hey", "Hello", "What are you doing", "Coding"]:
    mysql_loom.insert_one(
        instance=Post,
        values=[
            ColumnValue(name="userId", value=userId),
            ColumnValue(name="title", value=title),
        ],
    )


avg = mysql_loom.avg(
    instance=Post,
    column="id",
    distinct=True,
)

print(avg)

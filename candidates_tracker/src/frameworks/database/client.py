import os
import sqlite3
from abc import ABC, abstractmethod
from typing import Any, Dict

import psycopg2


class DatabaseConnection(ABC):
    @abstractmethod
    def connect(self) -> Any:
        pass


class PostgreSQLConnection(DatabaseConnection):
    def __init__(self, config: Dict[str, str]):
        self.config = config

    def connect(self) -> psycopg2.extensions.connection:
        return psycopg2.connect(**self.config)


class SQLiteConnection(DatabaseConnection):
    def __init__(self, config: Dict[str, str]):
        self.config = config

    def connect(self) -> sqlite3.Connection:
        return sqlite3.connect(self.config["database"])


def _create_connection(db: str) -> DatabaseConnection:
    db_config = {
        "host": os.environ.get("DB_HOST"),
        "port": int(os.environ.get("DB_PORT", 3306)),
        "user": os.environ.get("DB_USERNAME"),
        "password": os.environ.get("DB_PASSWORD"),
        "database": os.environ.get("DB_NAME"),
    }

    databases = {
        "postgresql": PostgreSQLConnection(db_config),
        "sqlite": SQLiteConnection({"database": db_config["database"]}),
    }

    database = databases.get(db)

    if not database:
        raise ValueError(f"Unsupported database: {db}")

    return database


def get_database_connection(db: str = "postgresql") -> DatabaseConnection:
    connection = _create_connection(db)
    return connection.connect()

import logging

import pytest
from dependency_injector import containers, providers

from application.database import Database


class Container(containers.DeclarativeContainer):
    db = providers.Singleton(Database, db_url="sqlite:///:memory")


def test_inject_database() -> None:
    container = Container()
    db = container.db()
    db.create_database()
    logging.info(container.providers)

from contextlib import contextmanager
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, sessionmaker

from wtenw.database.schema import Base


class DatabaseError(Exception):
    pass


class SQLDatabase:
    def __init__(self):
        self.base = Base
        database_path = str(Path(__file__).parent.parent / 'food' / 'food.sqlite')
        engine_url = f'sqlite:///{database_path}'
        self.engine = create_engine(engine_url, future=True)
        self._session_maker = sessionmaker(bind=self.engine, future=True)
        self.ro_session = None

    def create_tables(self):
        self.base.metadata.create_all(self.engine)

    @contextmanager
    def get_read_write_session(self) -> Session:
        session = self._session_maker()
        try:
            yield session
            session.commit()
        except (SQLAlchemyError, DatabaseError):
            session.rollback()
            raise
        finally:
            session.invalidate()

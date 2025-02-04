from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncEngine,
    AsyncSession,
)

from db.db_settings.db_settings import Settings


class DataBaseHelper:
    def __init__(self, db_url, db_echo: bool = False):
        self.engine = create_async_engine(url=db_url, echo=db_echo)
        self.session_factory = async_sessionmaker(
            bind=self.engine, autoflush=False, autocommit=False, expire_on_commit=False
        )

    #
    # async def get_engine(self) -> AsyncEngine:
    #     return self.db_engine
    #
    # async def set_engine(self, url: str) -> None:
    #     self.db_engine = create_async_engine(url=url, echo=True)
    #
    # async def set_session_factory(self) -> None:
    #     self.session_factory = async_sessionmaker(bind=self.db_engine)
    #
    # async def init_db(self, base) -> None:
    #     async with self.db_engine.begin() as conn:
    #         await conn.run_sync(base.metadata.drop_all)
    #         await conn.run_sync(base.metadata.create_all)


db_helper = DataBaseHelper(db_url=Settings().database_url)

# @property
# def db_engine(self) -> AsyncEngine:
#     print("Get Async Engine")
#     return self.db_engine
#
# @db_engine.setter
# def db_engine(self, url: str):
#     print("Set Async Engine")
#     self.db_engine = create_async_engine(url=url, echo=True)
#
# @property
# def session_factory(self):
#     print("Get Async Session")
#     return self.session_factory
#
# @session_factory.setter
# def session_factory(self, ur):
#     print("Set Async Session")
#     self.session_factory = async_sessionmaker(bind=self.db_engine)
#     # autoflush = False,
#     # autocommit = False,
#     # expire_on_commit = False

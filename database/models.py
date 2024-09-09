import os
from dotenv import find_dotenv, load_dotenv


from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

load_dotenv(find_dotenv())

engine = create_async_engine(os.getenv('SQLALCHEMY_URL'), echo=True)

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int] = mapped_column(BigInteger)

    orders = relationship("Order", back_populates="user")

class Order(Base):
    __tablename__ = 'orders'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column()
    phone: Mapped[str] = mapped_column()
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    user = relationship("User", back_populates="orders")

async def async_main():
    async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

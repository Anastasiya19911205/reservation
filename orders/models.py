import random

from sqlalchemy import Integer, String, Column, MetaData, create_engine,TIMESTAMP,ForeignKey, func
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, Session, sessionmaker

Base = declarative_base()
metadata = MetaData()
# engine = create_engine('postgresql+psycopg2://friender:friender@localhost/reservation', echo=True)
engine = create_async_engine('postgresql+asyncpg://friender:friender@localhost:5432/reservation', echo=True)

async def get_async_session():
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session


# class Base(declarative_base):
#     pass

class Waiters(Base):
    __tablename__ = "waiters"

    waiter_id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    last_name = Column(String(30), default="Smith")
    age = Column(Integer)

# создание столиков, которые будут обслуживать официанты:
class TableReservation(Base):
    __tablename__ = "tables"
    table_id = Column(Integer, primary_key=True)
    start_armor = Column(TIMESTAMP)
    end_armor = Column(TIMESTAMP)
    waiter = Column(Integer, ForeignKey("waiters.waiter_id"))

#создание официантов
# with Session(engine) as session:
#
#     waiter_1 = Waiters(name="Mark",last_name="Parker",age=38)
#     waiter_2 = Waiters(name="Anna", last_name="Gerasimenya", age=21)
#     waiter_3 = Waiters(name="Naik", last_name="Walter", age=25)
#     session.add_all([waiter_1, waiter_2, waiter_3])
#     session.commit()

#перечислить(перебрать) всех официантов 2 варианта:
# with Session(engine) as session:
#     # waiters = session.query(Waiters).all()
#     waiters = session.query(Waiters.name,Waiters.age).all()
#     for waiter in waiters:
#         print(waiter.name, waiter.age)

#все,  в диапазоне от 25 до 30:
# with Session(engine) as session:
#     waiters = session.query(Waiters.name,Waiters.age).filter((Waiters.age>=25)&(Waiters.age<=30))
#     for waiter in waiters:
#         print(waiter.name,waiter.age)

#все,  кто старше 25 лет:
# with Session(engine) as session:
#     waiters = session.query(Waiters.name,Waiters.age).filter(Waiters.age>=25)
#     for waiter in waiters:
#         print(waiter.name,waiter.age)


# все с фио Parker и отсортировать по возрасту
# with Session(engine) as session:
#     waiters = session.query(Waiters.name,Waiters.age).filter(Waiters.last_name=="Parker").order_by(Waiters.age)
#     for waiter in waiters:
#         print(waiter.name,waiter.age)

#  возраст больше 10, по убывающему возрасту, первых 4, исключая первых 2
# with Session(engine) as session:
#     waiters = session.query(Waiters).filter(Waiters.age>=10).order_by(-Waiters.age).limit(4).offset(2)
#     for waiter in waiters:
#         print(waiter.name,waiter.age)

#  изменить возраст
# with Session(engine) as session:
#     waiter = session.query(Waiters).filter(Waiters.waiter_id==1).first()
#     waiter.age = 24
#     session.commit()

# удалили официанта по id
# with Session(engine) as session:
#     waiter = session.query(Waiters).filter(Waiters.waiter_id==4).first()
#     session.delete(waiter)
#     session.commit()

# delete from add

# назначить каждому официанту случайный столик
# with Session(engine) as session:
#     from random import randint
#     for _ in range(20):
#         table = TableReservation(waiter=random.randint(5,6))
#         session.add(table)
#         session.commit()

#назначить столики одному официанту
# with Session(engine) as session:
#     waiter_tables = session.query(TableReservation).join(Waiters).filter(Waiters.waiter_id ==2)
#     # waiter_tables_count = session.query(TableReservation.table_id,
#     #               func.count(Waiters.waiter_id)).group_by(Waiters.waiter_id).all()
#     for table in waiter_tables:
#         print(table.table_id)

# вывести кол-во столиков сгруппированых по нашим официантам
# with Session(engine) as session:
#     waiter_tables_count = session.query(TableReservation.table_id,
#                   func.count(Waiters.waiter_id)).group_by(Waiters.waiter_id).all()
#     for table in waiter_tables_count:
#         print(table)
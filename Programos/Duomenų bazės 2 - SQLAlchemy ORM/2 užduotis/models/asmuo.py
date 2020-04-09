
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///asmenys.db")
Base = declarative_base()

class Asmuo(Base):
    __tablename__ = "Asmuo"

    id = Column(Integer, primary_key=True)
    name = Column("Vardas", String)
    surname = Column("Pavardė", String)
    age = Column("Amžius", Integer)

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.surname}, {self.age}"

Base.metadata.create_all(engine)

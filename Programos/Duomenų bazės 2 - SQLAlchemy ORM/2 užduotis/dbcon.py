
from models.asmuo import Asmuo

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///asmenys.db')
Session = sessionmaker(bind=engine)
session = Session()

def add_record(name, surname, age):
    asmuo = Asmuo(name, surname, age)
    session.add(asmuo)
    session.commit()

def update_record(record_id, newname, newsurname, newage):
    asmuo = session.query(Asmuo).get(record_id)
    asmuo.name = newname
    asmuo.surname = newsurname
    asmuo.age = newage
    session.commit()

def delete_record(record_id):
    asmuo = session.query(Asmuo).get(record_id)
    session.delete(asmuo)
    session.commit()

def get_all_records_list():
    return session.query(Asmuo).all()

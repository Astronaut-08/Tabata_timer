'''This is user preset for tabata timer power by SQLAlchemy'''
from sqlalchemy import create_engine, MetaData, Column, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///presets.db')
metadata = MetaData()
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Preset(Base):
    '''This is the table of preset'''
    __tablename__='presets'
    id = Column(Integer, primary_key=True, autoincrement=True)
    work = Column(Integer)
    rest = Column(Integer)
    exercises = Column(Integer)
    rounds = Column(Integer)
    rounds_reset = Column(Integer)

Base.metadata.create_all(engine)

def add_records(work=1, rest=1, exercises=1, rounds=1, rounds_reset=1):
    '''Addicted records to the preset'''
    s = Session()
    new_record = Preset(work=work, rest=rest, exercises=exercises,\
                        rounds=rounds, rounds_reset=rounds_reset)
    s.add(new_record)
    s.commit()

def select_all_id():
    '''Return all column of id'''
    s = Session()
    res = s.query(Preset).all()
    return [row[0] for row in res]

def select_records_by_id(user_id):
    '''Select records by name and return, to use try: select_records_by_name.row_name'''
    s = Session()
    res = s.query(Preset).filter_by(id = user_id).first()
    return res

def delete_records_by_name(user_id):
    '''Delete records by the name'''
    s = Session()
    delete_name = s.query(Preset).filter_by(id = user_id).first()
    s.delete(delete_name)
    s.commit()

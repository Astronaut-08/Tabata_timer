'''This is user preset for tabata timer power by SQLAlchemy'''
from sqlalchemy import create_engine, MetaData, Column, Integer, Unicode
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
    name = Column(Unicode, unique=True)
    work = Column(Integer)
    rest = Column(Integer)
    exercises = Column(Integer)
    rouds = Column(Integer)
    rounds_reset = Column(Integer)

Base.metadata.create_all(engine)

def add_records(name='def', work=1, rest=1, exercises=1, rounds=1, rounds_reset=1):
    '''Addicted records to the preset'''
    s = Session()
    if name != s.query(Preset).filter_by(name = name).first().name:
        new_record = Preset(name=name, work=work, rest=rest, exercises=exercises,\
                            rouds=rounds, rounds_reset=rounds_reset)
        s.add(new_record)
        s.commit()
    else:
        return None

def select_records_by_name(name):
    '''Select records by name and return, to use try: select_records_by_name.row_name'''
    s = Session()
    res = s.query(Preset).filter_by(name = name).first()
    return res

def update_records_by_name(old_name, new_name):
    '''Update records be the name'''
    s = Session()
    update_record = s.query(Preset).filter_by(name = old_name).first()
    update_record.name = new_name
    s.commit()

def delete_records_by_name(name):
    '''Delete records by the name'''
    s = Session()
    delete_name = s.query(Preset).filter_by(name = name).first()
    s.delete(delete_name)
    s.commit()

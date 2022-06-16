from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from backend.local_settings import postgresql as settings
#connect with DB
def get_engine(user, passwd, host, port, db):
    url = f"postgresql://{user}:{passwd}@{host}:{port}/{db}"
    engine = create_engine(url, pool_size = 50, echo=False)
    return engine

def get_engine_from_settings():
    keys = ['USER','PASSWORD','HOST','POST','NAME']
    # if not all(key in keys for key in settings.keys()):
    #     raise Exception('bad config file')
    return get_engine(settings['USER'],settings['PASSWORD'],settings['HOST'],settings['PORT'],settings['NAME'])

def get_session():
    engine = get_engine_from_settings()
    session = sessionmaker(bind=engine)()
    return session

session = get_session()
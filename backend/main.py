from re import L
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from local_settings import postgresql as settings

def get_engine(user, passwd, host, port, db):
    url = f"postgresql://{user}:{passwd}@{host}:{port}/{db}"
    engine = create_engine(url, pool_size = 50, echo=False)
    return engine

engine1 = get_engine(settings['USER'],settings['PASSWORD'],settings['HOST'],settings['PORT'],settings['NAME'])

def get_engine_from_settings():
    keys = ['USER','PASSWORD','HOST','POST','NAME']
    # if not all(key in keys for key in settings.keys()):
    #     raise Exception('bad config file')
    
    return get_engine(settings['USER'],settings['PASSWORD'],settings['HOST'],settings['PORT'],settings['NAME'])

#create session
def get_session():
    engine = get_engine_from_settings()
    session = sessionmaker(bind=engine)()
    return session

session = get_session()

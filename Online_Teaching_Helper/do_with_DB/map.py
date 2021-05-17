# -*-coding:utf-8-*-
from sqlalchemy.ext.automap import automap_base
from do_with_DB.Session import get_session
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy import create_engine, MetaData

#注意传str 表明的时候要小写
engine = create_engine('mysql+pymysql://root:nbuser@localhost:3306/online_teaching_helper?charset=utf8', echo=True)

def to_dict(self):
    return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class DbSharding(object):
    def __init__(self, map_tables=None):
        self.tables = map_tables
        if not map_tables:
            self.auto_base = automap_base()
            self.auto_base.prepare(engine, reflect=True)
        else:
            self.metadata = MetaData()
            self.metadata.reflect(engine, only=map_tables)
            self.auto_base = automap_base(metadata=self.metadata)
            self.auto_base.prepare()

    def get_model(self, table_name):
        if not table_name:
            return None
        try:
            model: DeclarativeMeta = getattr(self.auto_base.classes, str(table_name))
            model.to_dict = to_dict
            return model
        except AttributeError:
            return False

'''test!
if __name__ == '__main__':
    db = DbSharding()
    model = db.get_model("user")
    # print(model.to_dict())
    session=get_session()
    res = session.query(model).filter(model.ID == 101).one()
    print(res.ID)
    res_dict = res.to_dict()
    print(res_dict)
    session.close()
    '''

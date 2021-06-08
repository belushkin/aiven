import os
import pg_simple


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


@singleton
class DB():

    def __init__(self):
        self.connection_pool = pg_simple.config_pool(
            max_conn=250,
            expiration=60,
            db_url=os.environ['DB_DSN']
        )
        self.db = pg_simple.PgSimple(self.connection_pool)

    def getConn(self):
        return self.db

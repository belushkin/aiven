import os
import pg_simple

from utils.decorators import singleton


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

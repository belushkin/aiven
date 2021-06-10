import os
import pg_simple

from utils.decorators import singleton


@singleton
class DB():

    def __init__(self):
        self.connection_pool = pg_simple.config_pool(
            max_conn=os.environ['DB_POOL_MAX_CONN'],
            expiration=os.environ['DB_POOL_EXPIRATION_TIME'],
            db_url=os.environ['DB_DSN']
        )
        self.db = pg_simple.PgSimple(self.connection_pool)

    def getConn(self):
        return self.db

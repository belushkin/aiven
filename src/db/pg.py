import os
import pg_simple

from utils.singleton import Singleton


class DB(metaclass=Singleton):
    """DB connection singleton, incapsulates usage of PG_SIMPLE over
    psycopg2 Postgres adapter

    Returns
    -------
    PgSimple
        Connection pool
    """
    def __init__(self):
        connection_pool = pg_simple.config_pool(
            max_conn=os.environ['DB_POOL_MAX_CONN'],
            expiration=os.environ['DB_POOL_EXPIRATION_TIME'],
            db_url=os.environ['DB_DSN']
        )
        self.db = pg_simple.PgSimple(connection_pool)

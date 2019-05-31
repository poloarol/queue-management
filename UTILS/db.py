import os
import urllib.parse as up
import psycopg2

DATABASE_URL = "postgres://ynsvtncb:v3StzUeatCf_PrpAfcdIwVe6RW-Qn6rI@isilo.db.elephantsql.com:5432/ynsvtncb"


class DB:
    """ DB connector """

    def __init__(self):
        up.uses_netloc.append('postgres')
        self._conn = None
        try:
            self._url = up.urlparse(DATABASE_URL)
            # self._url = up.urlparse(os.environ['DATABASE_URL'])
            self._conn = psycopg2.connect(database=self._url.path[1:], user=self._url.username, password=self._url.password, host=self._url.hostname, port=self._url.port)  # noqa
        except RuntimeError:
            raise RuntimeError("DATABASE_URL is not set, hence access doesn't occur")  # noqa

    def get_connection(self):
        return self._conn

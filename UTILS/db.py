import os
import urllib.parse as up
import psycopg2

class DB:
    """ DB connector """

    def __init__(self):
        up.uses_netloc.append('postgres')
        self._conn = None
        try:
            self._url = up.urlparse(os.environ['DATABASE_URL'])
            self._conn = psycopg2.connect(database=self._url.path[1:], 
                                            user=self._url.username, 
                                            password=self._url.password, 
                                            host=self._url.hostname, 
                                            port=self._url.port)
        except:
            raise RuntimeError("DATABASE_URL is not set, hence access doesn't occur")
    
    def get_connection(self):
        return self._conn
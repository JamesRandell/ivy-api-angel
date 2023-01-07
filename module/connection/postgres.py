from module.util.console import Log

import psycopg2


class Connection(object):

    _instances = {}

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            print('Creating the object...')
            cls.instance = super(Connection, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        
        self.connection = self.connect()




    def connect(self):
        Log.info('Running connect in connector....')
        return psycopg2.connect(database="test",
                                host="localhost",
                                user="root",
                                password="root",
                                port="5432")

    def query(self, query):

        cur = self.connection.cursor()

        
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print(db_version)
            
        # close the communication with the PostgreSQL
        cur.close()

    def _process_field(self):
        pass
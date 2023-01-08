from module.util.console import Console
from module.interface.IConnection import Base

import psycopg2


class Connection(Base,object):

    _instances = {}

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            print('Creating the object...')
            cls.instance = super(Connection, cls).__new__(cls)
        return cls.instance


    def __init__(self):
        self.connection = self.connect()
        self.query_parts_og = {}
        self.query_parts = {}


    def connect(self):
        Console.info('Running connect in connector....')
        conn = psycopg2.connect(database="test",
                                host="localhost",
                                user="root",
                                password="root",
                                port="5432")

        conn.autocommit = True

        return conn


    def query(self, queryDict):
        cursor = self.connection.cursor()
        self.query_parts_og = queryDict
        result = {}

        
        #self._reset()
        '''
        We loops through the query parts to call various functions to perform the translation so it works with this datasource
        '''
        for key in queryDict:
            if key == 'action': 
                continue
            do = f"_{key}"
            
            if hasattr(self, do) and callable(func := getattr(self, do)):
                self.query_parts[key] = func(self.query_parts_og[key])

        self.query_parts['action'] = self._action(self.query_parts_og['action'])

        #Console.log(self.query_parts_og)
        Console.log(self.query_parts)


        do = f"_action_{self.query_parts_og['action']}"

        command = ''
        if hasattr(self, do) and callable(func := getattr(self, do)):
            command = func()

        
        result: any


        Console.log(f'{command}')
        try:
            cursor.execute(command)
            result = cursor.fetchall()
            column_names = [desc[0] for desc in cursor.description]
            
            for row in result:
                f = {}
                keyIndex = 0
                for field in column_names:
                    f[field] = row[keyIndex]

                    keyIndex = keyIndex+1
                print(f)
                result.append(f)

        except Exception as err:
            result = False
            Console.error(f'{err}')
            Console.error(f'{type(err)}')

        # close the communication with the PostgreSQL
        cursor.close()
        return result
        

    def _process_field(self):
        pass


    def _action(self, value):
        match value:
            case 'select':
                return 'SELECT'
            case 'update':
                return 'UPDATE'
            case 'insert':
                return 'INSERT INTO'
            case 'delete':
                return 'DELETE'
            case 'create':
                return 'CREATE TABLE'
            case 'drop':
                return 'DROP TABLE'
            case 'alter':
                return 'ALTER TABLE'


    def _field(self, fieldArr):
        string = ','.join(fieldArr)

        return string


    def _order(self, value):
        pass


    def _pagination(self, value):
        return(f'LIMIT {value}')


    def _table(self, value):
        return(f'{value}')


    def _where(self, value):
        pass


    def _database(self, value):
        return(f'{value}')


    def _data(self, value):
        return value


    def _action_create(self):
        arr = []
        for field, schema in self.query_parts_og['field'].items():
 
            if 'auto' in schema.keys():
                arr.append(f'{field} SERIAL PRIMARY KEY,')
            elif schema['type'] in 'int,number':
                arr.append(f'{field} {schema["type"].upper()},')
            else:
                arr.append(f'{field} {schema["type"].upper()}({schema["size"]}),')

            
        
        result = ''.join(arr)[:-1]
        self.query_parts['field'] = '(' + result + ')'
        
        return self.query_parts['action'] + ' ' + self.query_parts['table'] + ' ' + self.query_parts['field'] + ' '
        

    def _action_drop(self):
        return self.query_parts['action'] + ' ' + self.query_parts['table']


    def _action_select(self):
        return self.query_parts['action'] + ' ' + self.query_parts['field'] + ' FROM ' + self.query_parts['table']


    def _action_insert(self):
        valueArr = []
        for field, value in self.query_parts['data'].items():
            valueArr.append(str(value))

        return self.query_parts['action'] + ' ' + self.query_parts['table'] + ' (' + self.query_parts['field'] + ') VALUES (' + ','.join(valueArr) + ')'


    def _reset(self):
        self.query_parts = self.query_parts_og

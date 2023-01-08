from module.util.console import Console
from module.validation import Validation

from importlib import import_module

from module.dictionary import Dictionary

class Datasource(Dictionary, Validation):

    queryParts:dict = {
        'field':{},
        'pagination':{},
        'where':{},
        'order':{},
        'action':'',
        'table': '',
        'database': '',
        'data':{}
    }
    
    @property
    def data(self):
        return self._data


    @data.setter
    def data(self, dataDict):
        self.queryParts["field"] = Validation.fieldExists(self, dataDict)
        
        for field in self.queryParts["field"]:
            self._data[field] = dataDict[field]
            self.queryParts['data'][field] = dataDict[field]


    def __init__(self, schemaFile):
        Console.info('Datasource instance.................')
        super().__init__(schemaFile)
        
        database_type = self.database_spec['type']

        self.db = import_module(f'module.connection.{database_type}').Connection()
        self._data = {}

        self.queryParts['database'] = self.database_spec['name']
        self.queryParts['table'] = self.table_spec['name']
        

    def select(self):
        self.queryParts['action'] = 'select'
        self._data = self.db.query(self.queryParts)


    def insert(self, data: dict = None):
        self.queryParts['action'] = 'insert'

        if data:
            self.data = data

        self.db.query(self.queryParts)


    def field(self, fields: list):
        Console.info('field')
        self.queryParts["field"] = Validation.fieldExists(self, fields)
        return self
    

    def order(self, fields):
        Console.info('order')
        return self


    def where(self, fields):
        Console.info('where')
        return self


    def limit(self, fields):
        Console.info('limit')
        return self    


    def table(self, table):
        self.queryParts["table"] = table


    def object(self, object):
        self.table(object)


    def create(self):
        self.queryParts["action"] = 'create'

        fields = {}
        for field in self.field_spec:
            fields[field] = self.field_spec[field]['back']

        self.queryParts["field"] = fields
        self.db.query(self.queryParts)


    def drop(self):
        self.queryParts["action"] = 'drop'
        self.db.query(self.queryParts)
from module.util.console import Log
from module.validation import Validation

from importlib import import_module

from module.dictionary import Dictionary

class Datasource(Dictionary, Validation):

    queryParts:dict = {
        'field':dict,
        'pagination':dict,
        'where':dict,
        'order':dict,
        'action':str,
        'table':str
    }
    

    def __init__(self, schemaFile):
        Log.info('Datasource instance.................')


        #Dictionary.__init__(self, schemaFile)
        #Validation.__init__(self, schemaFile)

        super().__init__(schemaFile)
        
        database_type = self.database_spec['type']


        self.db = import_module(f'module.connection.{database_type}').Connection()


        self.db.query(self.queryParts)
        self.db.query(self.queryParts)
        self.db.query(self.queryParts)
        

    def select(self):
        query = ""
        query = "SELECT version()"

        self.queryParts['action'] = 'select'
        Log.info(self.queryParts)

         

        
        
        

    def field(self, fields):
        Log.info('field')
        self.queryParts["field"] = Validation.fieldExists(self, fields)
        return self
    
    def order(self, fields):
        Log.info('order')

    def where(self, fields):
        Log.info('where')

    def limit(self, fields):
        Log.info('limit')

    def table(self, table):
        self.queryParts["table"] = table
        Log.warn(111)
        Log.ok(self.model)
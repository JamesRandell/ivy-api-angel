from module.util.console import Log

class Validation:


    

    def __init__(self, schemaFile):
        Log.info('Validation instance.................')

        self.model = {}
        self.field_spec = {}
        self.table_spec = {}
        self.database_spec = {}

    def fieldExists(self, field: list):


        for key in field:
            if not self.field_spec.get(key):
                field.remove(key)

        return field
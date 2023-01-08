from module.util.console import Console

class Validation:


    

    def __init__(self, schemaFile):
        Console.info('Validation instance.................')

        self.model = {}
        self.field_spec = {}
        self.table_spec = {}
        self.database_spec = {}

    def fieldExists(self, field: dict):


        for key in field:
            if not self.field_spec.get(key):
                field.remove(key)

        return field
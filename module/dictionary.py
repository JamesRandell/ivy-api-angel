from module.util.console import Log
from module.file import File
import json
import jsonschema
from jsonschema import validate
import os
from collections import namedtuple

modelSpec = {
    "type":"object",
    "properties": {
        "fieldSpec": {
            "type":"object",
                "patternProperties": {
                "^[^{}\"/\\\\]+$": {
                    "type": "object",
                    "properties": {
                        "front": {"type":"object"},
                        "back": {
                            "type":"object",
                            "properties": {
                                "type": {
                                    "description":"The data type. This is translated at the vendor level",
                                    "type":"string"
                                },
                                "size": {
                                    "description":"Length of the column/field",
                                    "type":"number"
                                },
                                "required": {
                                    "description":"Is the field not null?",
                                    "type": "boolean"
                                }
                            },
                            "required": [
                                "type",
                                "size"
                            ]
                        },
                        "join": {"type":"object"},
                        "options": {"type":"object"},
                    },
                    "required": [
                        "front",
                        "back"
                    ]
                },
            },
        },
        "tableSpec": {"type": "object"},
        "databaseSpec": {"type": "object"},
    },
    "required": ["fieldSpec","tableSpec","databaseSpec"],
    "additionalProperties": False
}
class Dictionary:



    @property
    def modelPath(self):
        return os.getcwd() + '/model/'
        


    def __init__(self, schemaFile):
        Log.info('Dictionary instance.................')

        self.model = {}
        self.field_spec = {}
        self.table_spec = {}
        self.database_spec = {}

        self.processSchema(schemaFile)

    def processSchema(self, schemaFile):
        Log.info('Dictionary instance process schema')


        filePath = self.modelPath + schemaFile
        model = File(filePath).result

        try:
            jsonschema.validate(instance=model, schema=modelSpec)
        except jsonschema.exceptions.ValidationError as err:
            Log.error(err)
            return False


        self.model = model
        self.field_spec = model['fieldSpec']
        self.table_spec = model['tableSpec']
        self.database_spec = model['databaseSpec']

        #return model

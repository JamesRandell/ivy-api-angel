from quart import Quart
from quart_cors import cors


from flask import Flask, request, jsonify
from flask_restx import Resource, Api, reqparse, Namespace
from flask_cors import CORS, cross_origin
from module.base import base
import json

from flask_jwt_extended import JWTManager
from flask_jwt_extended.exceptions import JWTExtendedException

from view.ns_company import ns_company
from view.ns_keyspace import ns_keyspace


#from auth import AuthError

import pathlib

#app = Flask(__name__) 
app = Flask('Angel', static_folder=None) 
#app.config.from_pyfile(pathlib.Path(__file__).parent / "config.py")

# Setup extensions
#from extensions import api, jwt
jwt = JWTManager()
jwt.init_app(app)

#api.init_app(app)
#api = Api(app = app) 
#api = Api.init_app(


authorizations = {"Bearer": {"type": "apiKey", "in": "header", "name": "x-access-token"}}
authorizations = {
    'Bearer' : {
        'type' : 'apiKey',
        'in' : 'header',
        'name' : 'x-access-token'
    }
}

api = Api(
    app = app,
    version="1.0.0",
    title="API Angel",
    description="Angel REST API",
    authorizations=authorizations,
    security='Bearer'
)



db: dict = {
    "database":"test",
    "host":"localhost",
    "user":"root",
    "password":"root",
    "port":"5432"
}


@api.errorhandler
def default_error_handler(error):
    # default status code
    status_code = getattr(error, 'status_code', 500)
    
    if isinstance(error, JWTExtendedException):#or isinstance(error, PyJWTError):
        return {"message": str(error)}, 401

    #elif type(error) in [OperationalError, DataError, IntegrityError]:
        # Unexpected database error. Is database down?
    #    return {"message": "Database error."}, status_code

    # INCLUDING MORE HANDLERS HERE

    else:
    
        return {"message": str(error)}, status_code


# ####### JWT #######
jwt = JWTManager()

# Error handler
class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code



@api.errorhandler(AuthError)
def handle_auth_error(ex):
    print (111111111111111111111111111111111111)
    print(ex)
    print (222222222222222222222222222222222222)
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response

    
# enable CORS
CORS(app, allow_origin="*", allow_methods=["GET", "POST", "DELETE", "OPTIONS"], allow_headers=['Content-Type', 'Access-Control-Allow-Origin','Access-Control-Allow-Headers', 'Access-Control-Allow-Methods'])


#CORS(app)
#CORS(app, resources={r"/*": {"origins": "http://localhost:5000"}}, allow_headers=['Content-Type', 'Access-Control-Allow-Origin',
#                         'Access-Control-Allow-Headers', 'Access-Control-Allow-Methods'])
#CORS(app, support_credentials=True)
#, resources={r'/*': {'origins': '*'}}

#parser = reqparse.RequestParser()  # initialize
# APIs are defined under a given namespace, they appear under a given heading in Swagger
api.add_namespace(ns_company)
api.add_namespace(ns_keyspace)


#app.register_blueprint(api_bp, url_prefix='/test')



#@ns_server.route('/')
'''
class keyspace(Resource, base):
    def get(self, keyspace):
        out, err = self.command(f"cqlsh -e \"SELECT JSON * FROM system_schema.tables WHERE table_name = '{keyspace}' ALLOW FILTERING\"")
        print(out)
        print('fffffff')
        out = self.process_cql_result(out, key="table_name")
        
        return jsonify(out)

api.add_resource(keyspace, '/<string:keyspace>')
'''






#ssl_context='adhoc',
if __name__ == '__main__':
     app.run(host='0.0.0.0', port='5000', debug=False)

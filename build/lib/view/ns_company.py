from flask import Flask, Blueprint, jsonify
from flask_restx import Resource, Api, reqparse, Namespace
from module.base import base
import json
from ivyorm import Datasource
from auth import requires_auth


db: dict = {
    "database":"test",
    "host":"localhost",
    "user":"root",
    "password":"root",
    "port":"5432"
}

orm = Datasource('model/test.json', db)

# Namespace
ns_company = Namespace('company', description='Information about a company')


@ns_company.route('/',
    doc={
        'description':'Everything related to cassandra keyspaces'
    }
)
class ns_company_company(Resource, base):


    @ns_company.doc(
        responses={
            401: 'Unauthorised'
        }
    )
    
    @requires_auth
    def get(self):
        orm.select()
        return orm.data, 200


    def put(self):
        out = 'Something here'
        return out, 200



@ns_company.route('/<string:id>')
class ns_company_single(Resource, base):

    @ns_company.doc(
        responses={
            200: 'Returns information about a company',
            404: 'Company not found'},
        params={
            'id': 'Primary key of a company'
        }
    )
    def get(self, id):
        orm.where(['ID', id])
        orm.select()
        
        if orm.data:
            return orm.data, 200
        else:
            return None, 404


    def delete(self):

        out = 'Something here'
        return out, 200


    def post(self):
        out = 'Something here'
        return out, 200


#ns_company = api
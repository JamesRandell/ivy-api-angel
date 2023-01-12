from flask import Flask, Blueprint, jsonify
from flask_restx import Resource, Api, reqparse, Namespace
from module.base import base
import json

#blueprint = Blueprint("api", __name__, url_prefix="/api/v1")

# Namespace
api = Namespace('company', description='Information about a company')


class ns_company_company(Resource, base):

    def get(self):

        out = 'Something here'
        return out, 200

ns_company = api
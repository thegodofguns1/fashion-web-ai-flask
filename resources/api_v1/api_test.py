from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse, request,fields, marshal_with
from werkzeug.datastructures import FileStorage
import sys
import numpy as np


# reqparse用于验证表单数据
class Test(Resource):
    def get(self):
        
        return "hello fashion web ai flask"
    def post(self):
        pass
    def delete(self):
        pass
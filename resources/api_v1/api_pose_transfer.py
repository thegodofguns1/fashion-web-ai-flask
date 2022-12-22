from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse, request,fields, marshal_with
from werkzeug.datastructures import FileStorage
import sys
import numpy as np
sys.path.append("../../")
from dior_package import pose_transfer

# reqparse用于验证表单数据
class PoseTransfer(Resource):
    # 单张图片参数解析
    parser = reqparse.RequestParser()
    parser.add_argument('source_img', type=FileStorage, location='files')
    parser.add_argument('target_pose', type=FileStorage, location='files')
    
    # 统一回复数据
    response_data = {
        'status':fields.Integer,
        'message':fields.String,
        'data':fields.List,
    }
    def get(self): 
        pass
    def post(self):
        args = parser.parse_args()
        source_img = args.get('source_img')
        target_pose = args.get('target_pose')
        # """
        # 传多张图片  for file in request.files.getlist('image')
        # """
        # for file in request.files.getlist('image'):
        #     print(file.filename)
        # 与data_process 通信
        
        return "yes"
    
    def delete(self):
        pass
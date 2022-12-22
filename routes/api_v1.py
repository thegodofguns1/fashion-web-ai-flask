# -*- coding: utf-8 -*-
from flask import Blueprint
from flask_restful import Api
 

api_v1 = Blueprint('api_v1', __name__)

api = Api(api_v1)

from resources.api_v1.api_pose_transfer import PoseTransfer
from resources.api_v1.api_test import Test
api.add_resource(Test,'/')
api.add_resource(PoseTransfer, '/api/v1/poseTransfer')
from flask_restful import Api, Resource, reqparse, request,fields, marshal_with
from flask import Response
import requests
from werkzeug.datastructures import FileStorage
import logging
import sys
import numpy as np
import cv2
import json
import logging
from PIL import Image
import torch
import matplotlib.pyplot as plt
from torchvision import transforms
from io import BytesIO
import base64
sys.path.append("../../")
from common import code
from dior_package import virtual_try_on

# url = "http://42.192.160.69:8081/api/v1/fashionEditing"
url = "http://42.192.160.69:8081/api/v1/loadData"
# reqparse用于验证表单数
class fashionEditing(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('source_img', type=FileStorage, location='files',action='append')
    parser.add_argument('target_img', type=FileStorage, location='files',action='append')
    def __init__(self):
        self.model = virtual_try_on.virtualTryOn()


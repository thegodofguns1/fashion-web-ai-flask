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
from dior_package import pose_transfer
from Logger import logger, LogLevel, TraceException
# from dior_package.pose_transfer import pose_transfer
# url = "http://42.192.160.69:8081/api/v1/openPose"
url = "http://42.192.160.69:8081/api/v1/loadData"
# reqparse用于验证表单数
class PoseTransfer(Resource):
    # 单张图片参数解析
    # parser = reqparse.ReqestParser()
    # parser.add_argument('source_img', type=FileStorage, location='files',action='append')
    # parser.add_argument('target_img', type=FileStorage, location='files',action='append')
    def __init__(self):
        self.model = pose_transfer.poseTransfer()
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('source_img', type=FileStorage, location='files',action='append') # 多个值&列表
        self.parser.add_argument('target_img', type=FileStorage, location='files',action='append')
        # pose_transfer(self,source_img,source_parse,source_pose, target_pose):
    # @marshal_with(response_data_fields)
    def get(self): 
        data_list = []
        files = {'source_img':open('/workspace/fashion-web-ai-flask/Imgs/00001-dries-van-noten-spring-2023-ready-to-wear-credit-gorunway.webp','rb'),'target_img':open("/workspace/fashion-web-ai-flask/Imgs/fashionWOMENTees_Tanksid0000796209_7additional.jpg",'rb')}
        
        rep = requests.post(url,files=files)
        
        rep_json = rep.json()
        if rep_json['code'] == code.OK:
            source_pimg = torch.Tensor(rep_json['source_pimg']) # c h w RGB
            source_parse = torch.Tensor(rep_json['source_parse'])
            source_kpt = torch.Tensor(rep_json['source_kpt'])
            target_pimg = torch.Tensor(rep_json['target_pimg'])
            target_parse = torch.Tensor(rep_json['target_parse'])
            target_kpt = torch.Tensor(rep_json['target_kpt'])
            # 测试kpt
            # 测试parse
            # 测试pimg
            
            # print(source_pimg.shape) # 3 256 176
            # print(source_parse.shape) # 
            # print(target_kpt.shape)
            img = torch.squeeze(self.model.pose_transfer(source_pimg, source_parse, source_kpt, target_kpt),0) # 如果batch_size为1,则删除第一维
            out = img.float().cpu().detach().numpy()
            out = (out + 1) / 2 # denormalize   unnormalize反归一化，归一化是减均值除方差，反归一化是+均值乘方差
            out = np.transpose((out * 255.0).astype(np.uint8), [1,2,0])
            img = Image.fromarray(out)
            img.save("./Imgs/out.png")
            # plt.imshow(img)
            # plt.axis('off')
            # plt.show() 
            # plt.savefig('./Imgs/test.png', bbox_inches='tight')
            # print(img.max())
            img_base64 = self.image_to_bytes(img)
            return {
                    "code":rep_json['code'],
                    "target_img":img_base64.decode(),
                    "message": "Image is Base 64 encoded"
                }
            # return {'code': rep_json['code']}
        return {'code': rep_json['code']}
    # @marshal_with(response_data_fields)
    def post(self):
        try:
            args = self.parser.parse_args()
            source_img_bytes = args.get('source_img')[0].read()
            target_pose_bytes = args.get('target_img')[0].read()
        except:
            return {'code':code.PARAM_ERROR, 'message':'请上传两张图片，图片格式为formdata'}
        
        source_img = BytesIO(source_img_bytes)
        target_pose = BytesIO(source_img_bytes)
        # source_img.save("source_img.png")
        # target_img.save("target_img.png")
        # pil_image = Image.open(BytesIO(source_img_bytes))
        files = {'source_img':source_img, 'target_img':target_pose}
        # logger.log(LogLevel.INFO,"test logger")
        while True:
            try:
                rep = requests.post(url, files=files)
                break
            except requests.exceptions.ConnectionError as ce:
                # print('ConnectionError -- please wait 3 seconds')
                logger.log(LogLevel.ERROR,"Connection Error")
                time.sleep(3)
            except requests.exceptions.ChunkedEncodingError as cee:
                # print('ChunkedEncodingError -- please wait 3 seconds')
                logger.log(LogLevel.ERROR,"ChunkedEncodingError")
                time.sleep(3)    
            except:
                # print('Unfortunitely -- An Unknow Error Happened, Please wait 3 seconds')
                logger.log(LogLevel.ERROR,"An Unknow Error Happened")
                time.sleep(3)  
        logger.log(LogLevel.INFO,rep.text) 
        rep_json = rep.json()
        if rep_json['code'] == code.OK:
            source_pimg = torch.Tensor(rep_json['source_pimg']) # c h w RGB
            source_parse = torch.Tensor(rep_json['source_parse'])
            source_kpt = torch.Tensor(rep_json['source_kpt'])
            target_pimg = torch.Tensor(rep_json['target_pimg'])
            target_parse = torch.Tensor(rep_json['target_parse'])
            target_kpt = torch.Tensor(rep_json['target_kpt'])
            # # 测试kpt
            # # 测试parse
            # # 测试pimg
            # image = transforms.ToPILImage()(source_pimg)
            # image.save("source_pimg.png")
            # print(source_pimg.shape) # 3 256 176
            # print(source_parse.shape) # 
            # print(target_kpt.shape)
            # print(source_pimg.shape) # 3 256 176
            img = torch.squeeze(self.model.pose_transfer(source_pimg, source_parse, source_kpt, target_kpt),0) # 如果batch_size为1,则删除第一维
            out = img.float().cpu().detach().numpy()
            out = (out + 1) / 2 # denormalize   unnormalize反归一化，归一化是减均值除方差，反归一化是+均值乘方差
            out = np.transpose((out * 255.0).astype(np.uint8), [1,2,0])
            img = Image.fromarray(out)
            # img.save("./Imgs/out.png")
            img_base64 = self.image_to_bytes(img)
            return {
                    "code":rep_json['code'],
                    "target_img":img_base64.decode(),
                    "message": "Image is Base 64 encoded"
                }

            # return {'code': rep_json['code']}
            # 传多张图片  for file in request.files.getlist('image')
            # """
            # for file in request.files.getlist('image'):
            #     print(file.filename)
            # 与data_process 通信
        else:
            return {'code':code.SEVER_ERROR, 'message':'生成失败'}
        # return JsonResponse(status=code.OK,message="success", data=[])

    def delete(self):
        pass

    def image_to_bytes(self, image: Image.Image, fmt='png') -> str:
        output_buffer = BytesIO()
        image.save(output_buffer, format=fmt)
        byte_data = output_buffer.getvalue()
        image_bytes = base64.b64encode(byte_data)
        return image_bytes
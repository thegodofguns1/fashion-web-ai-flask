# 时尚网站AI lab Flask服务器
## 将dressing in order模型打包成一个包，供服务器调用
## 算法服务器要调用数据处理服务器的接口

启动脚本
```
启动脚本
gunicorn部署Flask服务
python manager.py run
tree 
├── app
│   ├── api
│   │   ├── background_editing.py
│   │   ├── error.py
│   │   ├── fashion_editing.py
│   │   ├── hair_editing.py
│   │   ├── __init__.py
│   │   ├── makeup.py
│   │   └── pose_transfer.py
│   └── __init__.py
    common --复用的组件，比如相应请求和加密等
├── clip_package
├── dior_package
│   ├── __init__.py
│   └── __pycache__
│       └── __init__.cpython-37.pyc
├── fashion_web_ai_flask.py # 入口文件
    config.py # 存储配置
└── README.md
```

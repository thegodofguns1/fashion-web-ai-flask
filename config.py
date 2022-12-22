# -*- coding: utf-8 -*-
import os
import multiprocessing

# MODE = 'develop'  # develop: 开发模式; production: 生产模式
MODE = 'production'

# data_process 服务器 ip+端口

class ProductionConfig(object):
    """
    生产配置 
    """
    BIND = '0.0.0.0:8891'
    WORKERS = multiprocessing.cpu_count() * 2 + 1
    WORKER_CONNECTIONS = 10000
    BACKLOG = 64
    TIMEOUT = 60
    LOG_LEVEL = 'INFO'
    LOG_DIR_PATH = os.path.join(os.path.dirname(__file__), 'logs')
    LOG_FILE_MAX_BYTES = 1024 * 1024 * 100
    LOG_FILE_BACKUP_COUNT = 10
    PID_FILE = 'run.pid'


class DevelopConfig(object):
    """
    开发配置
    """
    BIND = '0.0.0.0:8891'
    WORKERS = 2
    WORKER_CONNECTIONS = 1000
    BACKLOG = 64
    TIMEOUT = 30
    LOG_LEVEL = 'DEBUG'
    LOG_DIR_PATH = os.path.join(os.path.dirname(__file__), 'logs')
    LOG_FILE_MAX_BYTES = 1024 * 1024
    LOG_FILE_BACKUP_COUNT = 1
    PID_FILE = 'run.pid'


if MODE == 'production':
    config = ProductionConfig
else:
    config = DevelopConfig
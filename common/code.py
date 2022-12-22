# -*- coding: utf-8 -*-

OK = 200

DB_ERROR = 4001

PARAM_ERROR = 400

AUTHORIZATION_ERROR = 401

FORBIDDEN = 403

SEVER_ERROR = 500


UNKNOWN_ERROR = 4301

CODE_MSG_MAP = {
    OK: 'ok',
    DB_ERROR: '数据库错误',
    PARAM_ERROR: '请求参数错误',
    AUTHORIZATION_ERROR: 'Unauthorized',
    FORBIDDEN:'Forbidden',
    SEVER_ERROR:'服务器内部错误',
    UNKNOWN_ERROR: "未知错误",
}
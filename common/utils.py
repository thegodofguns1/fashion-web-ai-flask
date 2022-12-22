# -*- coding: utf-8 -*-
import hashlib
import datetime
from .code import CODE_MSG_MAP


def pretty_result(code, msg=None, data=None):
    if msg is None:
        msg = CODE_MSG_MAP.get(code)
    return {
        'code': code,
        'msg': msg,
        'data': data
    }


def hash_md5(data):
    md5 = hashlib.md5()
    md5.update(data)
    return md5.hexdigest()
def get_age(year, month, day):
    now = datetime.datetime.now()
    now_year, now_month, now_day = now.year, now.month, now.day

    if year >= now_year:
        return 0
    elif month > now_month or (month == now_month and day > now_day):
        return now_year - year - 1
    else:
        return now_year - year
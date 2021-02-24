# -*- coding: utf-8 -*-
import hashlib


def _md5(data):
    md5 = hashlib.md5(data).hexdigest()
    return md5


def md5_file(filePath):
    path = filePath.replace("\\", "/")
    print(path)
    with open(path, "rb") as f_read:
        buff = f_read.read()
        # print(buff)
        if len(buff) > 0:
            md5 = _md5(buff)
            return md5
        else:
            return ""

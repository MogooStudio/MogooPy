# -*- coding: utf-8 -*-
import xxtea


def _ecrypt(data, key):
    buff = xxtea.encrypt(data, key)
    return buff


def _decrypt(data, key):
    buff = xxtea.encrypt(data, key)
    return buff


def encrypt_file(filePath, key):
    path = filePath.replace("\\", "/")
    with open(path, "rb") as f_read:
        buff = f_read.read()
        # print(buff)
        buff = _ecrypt(buff, key)
        print(buff)
        return buff


def decrypt_file(filePath, key):
    path = filePath.replace("\\", "/")
    with open(path, "rb") as f_read:
        buff = f_read.read()
        # print(buff)
        buff = _decrypt(buff, key)
        print(buff)
        return buff

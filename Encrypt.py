# -*- coding: utf-8 -*-
import xxtea


def _ecrypt(data, key):
    buff = xxtea.encrypt(data, key)
    return buff


def _decrypt(data, key):
    buff = xxtea.encrypt(data, key)
    return buff


def encrypt_file(filepath, key):
    path = filepath.replace("\\", "/")
    with open(path, "rb") as f_read:
        buff = f_read.read()
        buff = _ecrypt(buff, key)
        print(buff)
        return buff


def decrypt_file(filepath, key):
    path = filepath.replace("\\", "/")
    with open(path, "rb") as f_read:
        buff = f_read.read()
        buff = _decrypt(buff, key)
        print(buff)
        return buff

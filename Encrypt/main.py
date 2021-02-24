# -*- coding: utf-8 -*-
import hashlib
import xxtea

filePath = r"F:\work\slots\frameworks\runtime-src\proj.android-studio\app\build\outputs\apk\googleAvidlyFirst\debug\Slots-google-avidly-first-debug\assets\src\app\activity\vegasGuide\VegasModel.luac"
    # r"F:\work\slots\src\app\activity\vegasGuide\VegasModel.lua"

key = 'Hummer9072019Gam'
sign = 'y<W(:\q0V}'
test = "123abc"


def xxtea_crypt(path):
    fileName = path.replace("\\", "/")
    print(fileName)
    with open(fileName, "rb") as f_read:
        buff = f_read.read()
        buff = xxtea.decrypt(buff, key)
        print(buff)


def md5_crypt(path):
    fileName = path.replace("\\", "/")
    print(fileName)
    with open(fileName, "rb") as f_read:
        buff = f_read.read()
        if len(buff) > 0:
            md5 = hashlib.md5(buff).hexdigest()
            print('{0}{1}'.format("=", md5))


def init():
    md5_crypt(filePath)


if __name__ == '__main__':
    init()

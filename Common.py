# -*- coding: utf-8 -*-
import hashlib
import subprocess
import sys

zip_split_len = 500
zip_max_len = 100


def os_popen(_cmd):
    print "cmd", _cmd
    np = subprocess.Popen(_cmd, shell=True, stdout=subprocess.PIPE)
    while np.poll() is None:
        ret = np.stdout.readline()[:-1]
        if ret != "":
            print ret
    if np.poll():
        print "cmd error:", _cmd
        sys.exit(1)


def _md5(_data):
    md5 = hashlib.md5(_data).hexdigest()
    return md5


def md5_file(_filepath):
    path = _filepath.replace("\\", "/")
    print(path)
    with open(path, "rb") as f_read:
        buff = f_read.read()
        if len(buff) > 0:
            md5 = _md5(buff)
            return md5
        else:
            return ""


def zip_files(_zip_name, _zip_filepath):
    if not isinstance(_zip_filepath, list):
        return
    _len = len(_zip_filepath)
    if _len <= 0:
        return
    if _len <= zip_split_len:
        cmd = "zip -r %s ./ -i %s" % (_zip_name, " -i ".join(_zip_filepath))
        os_popen(cmd)
    else:
        while _len > 0:
            cmd = "zip -r %s ./ -i %s" % (_zip_name, " -i ".join(_zip_filepath[0:zip_max_len]))
            os_popen(cmd)
            _zip_filepath = _zip_filepath[zip_max_len:]

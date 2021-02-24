# -*- coding: utf-8 -*-
import hashlib
import subprocess
import sys


def os_popen(cmd):
    print
    var = "cmd", cmd
    np = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    while np.poll() is None:
        ret = np.stdout.readline()[:-1]
        if ret != "":
            print ret
    if np.poll():
        print "cmd error:", cmd
        sys.exit(1)


def _md5(data):
    md5 = hashlib.md5(data).hexdigest()
    return md5


def md5_file(filepath):
    path = filepath.replace("\\", "/")
    print(path)
    with open(path, "rb") as f_read:
        buff = f_read.read()
        if len(buff) > 0:
            md5 = _md5(buff)
            return md5
        else:
            return ""

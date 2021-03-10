# -*- coding: utf-8 -*-
import hashlib
import subprocess
import sys

G_ZIP_SPLIT_LINE = 500
G_ZIP_SPLIT_UNIT = 100


def os_popen(cmd):
    print "cmd", cmd
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


def zip_files(name, filepath):
    if not isinstance(filepath, list):
        return
    zip_len = len(filepath)
    if zip_len <= 0:
        return
    if zip_len <= G_ZIP_SPLIT_LINE:
        cmd = "zip -r %s ./ -i %s" % (name, " -i ".join(filepath))
        os_popen(cmd)
    else:
        while zip_len > 0:
            cmd = "zip -r %s ./ -i %s" % (name, " -i ".join(filepath[0:G_ZIP_SPLIT_UNIT]))
            os_popen(cmd)
            filepath = filepath[G_ZIP_SPLIT_UNIT:]

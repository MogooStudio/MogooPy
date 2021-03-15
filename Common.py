# -*- coding: utf-8 -*-
import hashlib
import subprocess
import sys
import os
import argparse

G_ZIP_SPLIT_LINE = 500
G_ZIP_SPLIT_UNIT = 100


def os_system(cmd, use_secure = False):
    print "cmd", cmd
    os.system(cmd)


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


def read_file(filename, mode="r"):
    with open(filename, mode) as f_read:
        buff = f_read.read()
        return buff


def save_file(filename, content, mode="w"):
    with open(filename, mode) as f_write:
        f_write.write(content)


def _md5(data):
    _hash = hashlib.md5(data).hexdigest()
    return _hash


def md5(filepath):
    path = filepath.replace("\\", "/")
    print(path)
    with open(path, "rb") as f_read:
        buff = f_read.read()
        if len(buff) > 0:
            _hash = _md5(buff)
            return _hash
        else:
            return ""


def zip_dir(name, dirpath):
    assert isinstance(dirpath, str), "error: dirpath={0}".format(dirpath)
    os.chdir(dirpath)
    files = []
    for name in os.listdir("."):
        files.append(os.path.join(dirpath, name))
    zip_files(name, files)


def zip_files(name, filepath):
    assert isinstance(filepath, list), "error: filepath={0}".format(filepath)
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

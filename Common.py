# -*- coding: utf-8 -*-
import hashlib
import subprocess
import sys

G_ZIP_SPLIT_LINE = 500
G_ZIP_SPLIT_UNIT = 100


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
    z_len = len(_zip_filepath)
    if z_len <= 0:
        return
    if z_len <= G_ZIP_SPLIT_LINE:
        cmd = "zip -r %s ./ -i %s" % (_zip_name, " -i ".join(_zip_filepath))
        os_popen(cmd)
    else:
        while z_len > 0:
            cmd = "zip -r %s ./ -i %s" % (_zip_name, " -i ".join(_zip_filepath[0:G_ZIP_SPLIT_UNIT]))
            os_popen(cmd)
            _zip_filepath = _zip_filepath[G_ZIP_SPLIT_UNIT:]

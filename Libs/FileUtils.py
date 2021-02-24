# -*- coding: utf-8 -*-
import os
import logging


def StringEndswith(str, suffix):
    if isinstance(suffix, list):
        for tmp in suffix:
            if str.endswith(tmp):
                return True
    else:
        return str.endswith(suffix)
    return False


def GetAllFiles(dirpath, _extnames="", _mtimescope=[]):
    files = os.listdir(dirpath)
    result = []
    extnames = []
    if isinstance(_extnames, list):
        extnames = _extnames
    else:
        extnames = _extnames.split("|")

    bValidModifyTimeScope = len(_mtimescope) == 2
    mtime_min = 0
    mtime_max = 0
    if bValidModifyTimeScope:
        mtime_min = _mtimescope[0]
        mtime_max = _mtimescope[1]

    for file in files:
        filepath = dirpath + "/" + file
        if not os.path.isdir(filepath):
            if StringEndswith(filepath, extnames):
                if bValidModifyTimeScope:
                    st = os.stat(filepath)
                    if st.st_mtime >= mtime_min and st.st_mtime <= mtime_max:
                        result.append(filepath)
                else:
                    result.append(filepath)
        else:
            tmp = GetAllFiles(filepath, extnames, _mtimescope)
            result.extend(tmp)
    return result


def GetAllLines(filepath):
    lines = []
    try:
        f = open(filepath, "r")
        lines = f.readlines()
        f.close()
    except Exception as e:
        f.close()
        try:
            f = open(filepath, "r")
            lines = f.readlines()
            f.close()
        except Exception as e:
            f.close()
            logging.error("GetAllLines: %s", filepath)
            logging.error(e)
            lines = []
    return lines
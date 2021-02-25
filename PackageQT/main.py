# coding=utf-8

import os

# qt安装目录
qtEnv = "/Users/jinshan/Qt/5.15.2/clang_64/bin"
# 项目目录
appPath = "/Users/jinshan/workspace/win/Debugtools/build-Debugtools-Desktop_Qt_5_15_2_clang_64bit-Release/Debugtools.app"
# 导出目录
outPath = "/Applications"


def package():
    print "开始打包..."
    os.chdir(qtEnv)
    print os.getcwd()
    os.system("./macdeployqt {0}".format(appPath))
    print "打包成功..."
    os.system("cp -rf {0} {1}".format(appPath, outPath))
    print "拷贝完成，请到{0}查看".format(outPath)


if __name__ == '__main__':
    package()

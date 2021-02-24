import os
import subprocess
import sys

path = "F:\\work\\slots"

zip_name = "111"
max_len = 2


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


def main():
    files = [
         '/src/theme2/client/themeList/ThemeDrRichGrand.lua',
         '/src/theme2/client/themeList/ThemeFrankenMoolah.lua',
         '/src/theme2/client/themeList/ThemeFrogTale.lua',
         '/src/theme2/client/themeList/ThemeHotLittleDevil.lua',
         '/src/theme2/client/themeList/ThemeJinSeDao.lua',
         '/src/theme2/client/themeList/ThemeKronos.lua',
         '/src/theme2/client/themeList/ThemeLavaCash.lua',
         '/src/theme2/client/themeList/ThemeLongTengHuXiao.lua',
         '/src/theme2/client/themeList/ThemeMermaidPearls.lua',
         ]
    os.chdir(path)
    while len(files) > 0:
        cmd = "zip -r %s ./ -i %s" % ("111", " -i ".join(files[0:max_len]))
        os_popen(cmd)
        files = files[max_len:]
    os_popen(cmd)
    print "zip end"


if __name__ == '__main__':
    main()

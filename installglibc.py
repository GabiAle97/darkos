import os, shutil, time
def packages():
    os.system("pkg install x11-repo -y &>/dev/null")
    os.system("pkg install pulseaudio wget xkeyboard-config freetype fontconfig libpng xorg-xrandr termux-x11-nightly termux-am zenity which bash curl sed cabextract -y --no-install-recommends &>/dev/null")
def check_prev_version():
    prefix = "/data/data/com.termux/files/home/.wine"
    glibc = "/data/data/com.termux/files/usr/glibc"
    config = "/data/data/com.termux/files/usr/glibc/opt/configos"
    if os.path.exists(prefix):
        shutil.rmtree(prefix)
    if os.path.exists(glibc):
        shutil.rmtree(glibc)
    if os.path.exists(config):
        shutil.rmtree(config)
def install_glibc():
    os.system("wget -q --show-progress https://github.com/Ilya114/Box64Droid/releases/download/alpha/glibc-prefix.tar.xz")
    os.system("tar -xJf glibc-prefix.tar.xz -C $PREFIX/")
def scripts():
    os.system("wget https://raw.githubusercontent.com/Ilya114/Box64Droid/main/scripts/native/box64droid &>/dev/null")
    os.system("wget https://raw.githubusercontent.com/Ilya114/Box64Droid/main/scripts/native/box64droid.py &>/dev/null")
    os.system("wget https://raw.githubusercontent.com/Ilya114/Box64Droid/main/scripts/native/start-box64.py &>/dev/null")
    os.system("wget https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks &>/dev/null")
    os.system("chmod +x box64droid winetricks")
    os.system("mv box64droid box64droid.py start-box64.py winetricks $PREFIX/bin/")
    os.system("ln -s $PREFIX/glibc/opt/wine/bin/wine $PREFIX/glibc/bin/wine")
    os.system("ln -s $PREFIX/glibc/opt/wine/bin/wine64 $PREFIX/glibc/bin/wine64")
    os.system("ln -s $PREFIX/glibc/opt/wine/bin/wineserver $PREFIX/glibc/bin/wineserver")
    os.system("ln -s $PREFIX/glibc/opt/wine/bin/wineboot $PREFIX/glibc/bin/wineboot")
    os.system("ln -s $PREFIX/glibc/opt/wine/bin/winecfg $PREFIX/glibc/bin/winecfg")
def clear_waste():
    os.system("rm glibc-prefix.tar.xz install native.py")
    os.system("clear")
def storage():
    os.system("termux-setup-storage")
    time.sleep(2)
os.system("clear")
print(" darkosbinstallation is beginnin😉Please allow storage permission!")
storage()
print("")
packages()
check_prev_version()
print(" Downloading and unpacking glibc-prefix")
print("")
install_glibc()
print("")
scripts()
print("")
clear_waste()
print(" Installation finished starting os write.darkos.")

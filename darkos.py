import os
import re
import subprocess
import time
import threading
import shutil
import sys, urllib.request, urllib.error

R = "\033[1;31m"
G = "\033[1;32m"
Y = "\033[1;33m"
B = "\033[1;34m"
C = "\033[1;36m"
W = "\033[1;37m"
BOLD = "\033[1m"

current_version = "0.911"
url = 'https://raw.githubusercontent.com/ahmad1abbadi/darkos/main/currently%20version.txt'

def colored_input(prompt):
    print(f"{R}[{W}-{R}]{G}{BOLD} {prompt} {W}", end="")
    user_input = input()
    return user_input

def start_darkos():
    os.system("clear")
    if "LD_PRELOAD" in os.environ:
        del os.environ["LD_PRELOAD"]
    print(f"{R}[{W}-{R}]{G}{BOLD} Starting {W}")
    os.system("termux-x11 :0 &>/dev/null &")
    os.system('pulseaudio --start --load="module-native-protocol-tcp auth-ip-acl=127.0.0.1 auth-anonymous=1" --exit-idle-time=-1 &>/dev/null')
def wine_container():
    os.system("clear")
    photo()
    print(f"{R}[{W}-{R}]{G}{BOLD} Select Wine container: {W}")
    
    wine_paths = {
        "1": "/data/data/com.termux/files/usr/glibc/opt/wine/1/wine/bin",
        "2": "/data/data/com.termux/files/usr/glibc/opt/wine/2/wine/bin",
        "3": "/data/data/com.termux/files/usr/glibc/opt/wine/3/wine/bin"
    }
    
    for key, path in wine_paths.items():
        if os.path.exists(path):
            if key == "1":
                print(f"{Y}{BOLD} wine 1 {W}")
            if key == "2":
                print(f"{Y} 2) wine 2 {W}")
            if key == "3":
                print(f"{Y} 3) wine 3 {W}")
    
    print(f"{Y} Else) Back to the main menu 👑 {W}")
    print("")
    
    prefix_path = colored_input("Enter your selection:")
    
    if prefix_path not in wine_paths.keys():
        print(f"{R}Incorrect or empty option! {W}")
        time.sleep(1)
        main_menu()
    else:
        conf_path = f"/data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/os.conf"
        wine_prefix = f"/data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/.wine"
        os.system("chmod +x $PREFIX/glibc/bin/box86")
        os.system("chmod +x $PREFIX/glibc/bin/box64")
        os.system(f"chmod +x /data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/wine/bin/wine")
        os.system(f"chmod +x /data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/wine/bin/wineserver")
        os.system(f"ln -sf /data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/wine/bin/wine $PREFIX/glibc/bin/wine")
        if not os.path.exists(f"/data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/wine/bin/wine64"):
            os.system(f"ln -sf /data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/wine/bin/wine $PREFIX/glibc/bin/wine64")
            os.system(f"chmod +x /data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/wine/bin/wine64")
            os.system(f"ln -sf /data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/wine/bin/wine $PREFIX/glibc/opt/wine/{prefix_path}/wine/bin/wine64")
        else:
            os.system(f"chmod +x /data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/wine/bin/wine64")
            os.system(f"ln -sf /data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/wine/bin/wine64 $PREFIX/glibc/bin/wine64")
        os.system(f"ln -sf /data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/wine/bin/wineserver $PREFIX/glibc/bin/wineserver")
        os.system(f"ln -sf /data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/wine/bin/wineboot $PREFIX/glibc/bin/wineboot")
        os.system(f"ln -sf /data/data/com.termux/files/us/glibc/opt/wine/{prefix_path}/wine/bin/winecfg $PREFIX/glibc/bin/winecfg")
        #os.system("ln -sf /var/lib/dbus/machine-id /etc/machine-id")
        os.environ.pop('LD_PRELOAD', None)
        ### AZ DARK 
        if os.path.exists(conf_path):
            exec(open(conf_path).read())
        if not os.path.exists(wine_prefix):
            print(f"{R}[{W}-{R}]{G}{BOLD} Creating wine prefix 💫 {W}")
            os.system(f'WINEDLLOVERRIDES="mscoree=disabled" box64 wine64 wineboot &>/dev/null')
            os.system(f'cp -r $PREFIX/glibc/opt/Startxmenu/* "{wine_prefix}/drive_c/ProgramData/Microsoft/Windows/Start Menu"')
            os.system(f'rm "{wine_prefix}/dosdevices/z:"')
            os.system(f'ln -s /sdcard/Download "{wine_prefix}/dosdevices/o:" &>/dev/null')
            os.system(f'ln -s /sdcard/darkos "{wine_prefix}/dosdevices/e:" &>/dev/null')
            os.system(f'ln -s /data/data/com.termux/files "{wine_prefix}/dosdevices/z:"')
            print(f"{G} Installing DXVK+Zink... {W}")
            os.system(f'box64 wine "$PREFIX/glibc/opt/apps/Install OS stuff.bat" &>/dev/null')
            print(f"{R}[{W}-{R}]{G}{BOLD} Done! {W}")
            #os.system("clear") 
            print(f"{R}[{W}-{R}]{G}{BOLD} prefix done enjoy 🤪 {W}")
            time.sleep(3)
            os.system("box64 wineserver -k &>/dev/null")
            start_container()
    start_container()
def recreate_32bit():
    os.system("clear")
    photo()
    print(f"{R}[{W}-{R}]{G}{BOLD} select wine : {W}")
    
    wine_paths = {
        "1": "/data/data/com.termux/files/usr/glibc/opt/wine/1/wine/bin",
        "2": "/data/data/com.termux/files/usr/glibc/opt/wine/2/wine/bin",
        "3": "/data/data/com.termux/files/usr/glibc/opt/wine/3/wine/bin"
    }
    
    for key, path in wine_paths.items():
        if os.path.exists(path):
            if key == "1":
                print(f"{Y} 1) wine 1 {W}")
            if key == "2":
                print(f"{Y} 2) wine 2 {W}")
            if key == "3":
                print(f"{Y} 3) wine 3 {W}")
    
    print(f"{Y} Else) Back to the settings menu {W}")
    print("")
    
    prefix_path = colored_input("Enter your selection:")
    
    if prefix_path not in wine_paths.keys():
        change_setting()
    else:
        conf_path = f"/data/data/com.termux/files/usr/glibc/opt/wine/1/os.conf"
        wine_prefix = f"/data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/.wine"
        os.system("chmod +x $PREFIX/glibc/bin/box86")
        os.system("chmod +x $PREFIX/glibc/bin/box64")
        os.system(f"chmod +x /data/data/com.termux/files/usr/glibc/opt/wine/1/wine/bin/wine")
        os.system(f"chmod +x /data/data/com.termux/files/usr/glibc/opt/wine/1/wine/bin/wine64")
        os.system(f"chmod +x /data/data/com.termux/files/usr/glibc/opt/wine/1/wine/bin/wineserver")
        os.system("rm -rf $PREFIX/glibc/bin/wine $PREFIX/glibc/bin/wine64 $PREFIX/glibc/bin/wineserver")
        os.system(f"ln -sf /data/data/com.termux/files/usr/glibc/opt/wine/1/wine/bin/wine $PREFIX/glibc/bin/wine")
        os.system(f"ln -sf /data/data/com.termux/files/usr/glibc/opt/wine/1/wine/bin/wine64 $PREFIX/glibc/bin/wine64")
        os.system(f"ln -sf /data/data/com.termux/files/usr/glibc/opt/wine/1/wine/bin/wineserver $PREFIX/glibc/bin/wineserver")
        os.system(f"ln -sf /data/data/com.termux/files/usr/glibc/opt/wine/1/wine/bin/wineboot $PREFIX/glibc/bin/wineboot")
        os.system(f"ln -sf /data/data/com.termux/files/us/glibc/opt/wine/1/wine/bin/winecfg $PREFIX/glibc/bin/winecfg")
        os.environ.pop('LD_PRELOAD', None)
        ### AZ DARK 
        exec(open(conf_path).read())
        def prefix_gstreamer():
            os.environ['WINEPREFIX'] = os.path.expandvars("$PREFIX/glibc/opt/wine/3/.wine")
            print(f"{R}[{W}-{R}]{G}{BOLD} Fixing wine prefix .... {W}")
            os.system(f'WINEDLLOVERRIDES="mscoree=disabled" box64 wine64 wineboot &>/dev/null')
            os.system(f'cp -r $PREFIX/glibc/opt/Startxmenu/* "{wine_prefix}/drive_c/ProgramData/Microsoft/Windows/Start Menu"')
            os.system(f'rm "{wine_prefix}/dosdevices/z:"')
            os.system(f'ln -s /sdcard/Download "{wine_prefix}/dosdevices/o:" &>/dev/null')
            os.system(f'ln -s /sdcard/darkos "{wine_prefix}/dosdevices/e:" &>/dev/null')
            os.system(f'ln -s /data/data/com.termux/files "{wine_prefix}/dosdevices/z:"')
            print(f"{R}[{W}-{R}]{C}{BOLD} please wait .. {W}")
            os.system(f'box64 wine "$PREFIX/glibc/opt/apps/Install OS stuff.bat" &>/dev/null')
            print(f"{R}[{W}-{R}]{G}{BOLD} done...please restart OS {W}")
            time.sleep(1)
            os.system("box64 wineserver -k &>/dev/null")
            main_menu()
        if os.path.exists(wine_prefix):
            shutil.rmtree(wine_prefix)
            time.sleep(1)
            prefix_gstreamer()
        if not os.path.exists(wine_prefix):
            prefix_gstreamer()
def photo():
    os.system("python3 $PREFIX/bin/photo.py")
def check_network_connection():
    try:
        urllib.request.urlopen("http://www.google.com", timeout=5)
        return True
    except urllib.error.URLError:
        return False
def main():
    if not check_network_connection():
        print(f"{R}[{W}-{R}]{R}{BOLD} No network connection available. {W}")
        return
    try:
        response = urllib.request.urlopen(url)
        latest_version = response.read().decode('utf-8').strip()
        if latest_version < current_version:
            os.system("curl -o install https://raw.githubusercontent.com/ahmad1abbadi/darkos/main/installO.sh && chmod +x install && ./install")
        if latest_version > current_version:
            print(f"{R}[{W}-{R}]{C}{BOLD} update available....please update DARKOS {W}")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print("🙅‍♂️🛜", e)
        else:
            print(f"{R} something went wrong please send this error to developer {W}")

def mangohud_vulkan():
    os.system("apt reinstall vulkan-icd-loader-glibc")
    print(f"{R}[{W}-{R}]{Y}{BOLD} working...... please wait {W}")
    os.system("grun -s ldconfig")
def winetricks():
    os.system("clear")
    photo()
    print(f"{R}[{W}-{R}]{G}{BOLD} winetricks menu : {W}")
    print("")
    print(f"{Y} 1) winetricks gui 🖥️ {W}")
    print("")
    print(f"{Y} 2) winetricks verbs 🧑‍💻 {W}")
    print("")
    print(f"{Y} Else) Back to the main menu 👑 {W}")
    print("")
    choise = input()
    conf_path = f"/data/data/com.termux/files/usr/glibc/opt/wine/os.conf"
    if choise != "1" and choise != "2":
        print(f"{R}[{W}-{R}]{G}{BOLD} backing to main menu {W}")
        time.sleep(2)
        main_menu()
    elif choise == "1":
        exec(open(conf_path).read())
        exec(open('/sdcard/darkos/darkos_dynarec.conf').read())
        exec(open('/sdcard/darkos/darkos_custom.conf').read())
        os.system("clear")
        photo()
        print(f"{R}[{W}-{R}]{G}{BOLD} loading...... winetrick {W}")
        print(f"{R}[{W}-{R}]{Y}{BOLD} winetricks working just wait its take 1 minute to launch menu {W}")
        print(f"{R}[{W}-{R}]{G}{BOLD} if you want to close it and back to main menu press control+C {W}")
        os.system("am start -n com.termux.x11/com.termux.x11.MainActivity &>/dev/null")
        os.system("LD_PRELOAD= WINESERVER=$PREFIX/glibc/bin/wineserver WINE=$PREFIX/glibc/bin/wine64 $PREFIX/glibc/bin/box64 $PREFIX/glibc/bin/bash86 $PREFIX/glibc/bin/winetricks &>/dev/null")
        main_menu()
    elif choise == "2":
        exec(open(conf_path).read())
        exec(open('/sdcard/darkos/darkos_dynarec.conf').read())
        exec(open('/sdcard/darkos/darkos_custom.conf').read())
        os.system("clear")
        photo()
        print(f"{R}[{W}-{R}]{G}{BOLD} winetrick verbs ready to use on chosen container... {W}")
        print("")
        print(f"{R}[{W}-{R}]{G}{BOLD} input verbs: {W}")
        winetrick_verbs = input()
        os.system(f"LD_PRELOAD= WINESERVER=$PREFIX/glibc/bin/wineserver WINE=$PREFIX/glibc/bin/wine64 $PREFIX/glibc/bin/box64 $PREFIX/glibc/bin/bash86 $PREFIX/glibc/bin/winetricks {winetrick_verbs} ")
        print("")
        print(f"{R}[{W}-{R}]{G}{BOLD} winetrick packages installed successfully...👍 {W}")
        print(f"{R}[{W}-{R}]{G}{BOLD} backing to main menu..... 🔁 {W}")
        time.sleep(4)
        main_menu()
def start_container():
    start_darkos()
    exec(open('/sdcard/darkos/darkos_dynarec.conf').read())
    os.system("chmod +x $PREFIX/glibc/bin/box86")
    os.system("chmod +x $PREFIX/glibc/bin/box64")
    xrandr_output = os.popen('xrandr').read()
    current_resolution_match = re.search(r'current\s+(\d+) x (\d+)', xrandr_output)

    if current_resolution_match:
        current_resolution = f"{current_resolution_match.group(1)}x{current_resolution_match.group(2)}"
    else:
        current_resolution = "800x600"
    res = current_resolution
    os.system("taskset -c 4-7 box64 wine64 explorer /desktop=shell," + res + " $PREFIX/glibc/opt/apps/run.exe &>/dev/null &")
    os.system("am start -n com.termux.x11/com.termux.x11.MainActivity &>/dev/null")
    os.system("clear")
    os.system("python3 $PREFIX/bin/photo.py")
    print(f"{Y}exit 1️⃣ {W}")
    user_input = colored_input("Enter 1 to stop: ")
    if user_input == "1":
        os.system("box64 wineserver -k")
        print(f"{Y} Exiting 👋 {W}")
        os.system('pkill -f "app_process / com.termux.x11"')
        os.system('pkill -f pulseaudio')
        print(f"{G} see you later {W}")
        main_menu()
    main_menu()
        
def uninstall_wine():
    os.system("clear")
    photo()
    print(f"{R}[{W}-{R}]{G}{BOLD} Are you sure you want to delete the wine version? {W}")
    print("")
    if os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/1/wine/bin"):
        print(f"{Y}1) Delete wine 1 {W}")
    if os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/2/wine/bin"):
        print(f"{Y} 2) Delete wine 2 {W}")
    if os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/3/wine/bin"):
        print(f"{Y} 3) Delete wine 3 {W}")
    print(f"{Y} else) main menu ⬅️ {W}")
    print("")
    choice = input()
    if choice != "1" and choice != "2" and choice != "3":
        print(f"{R} Incorrect or empty option! {W}")
        main_menu()
    elif choice == "1" and os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/3/wine/bin"):
        print(f"{R}[{W}-{R}]{G} Deleting wine 1, please wait... {W}")
        print("")
        uninstall_wine9()
    elif choice == "2" and os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/2/wine/bin"):
        print(f"{R}[{W}-{R}]{G} Deleting wine 2, please wait... {W}")
        print("")
        uninstall_wine8()
    elif choice == "3" and os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/1/wine/bin"):
        print(f"{R}[{W}-{R}]{G} Deleting wine 3, please wait... {W}")
        print("")
        uninstall_wine7()
    main_menu()
def uninstall_wine9():
    if os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/1/wine/bin"):
        os.system("rm -r /data/data/com.termux/files/usr/glibc/opt/wine/1/wine")
        if os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/1/.wine"):
            shutil.rmtree('/data/data/com.termux/files/usr/glibc/opt/wine/1/.wine')
def recreate_prefix_wineAZ():
    print(f"{R}[{W}-{R}]{G}{BOLD} select version of wine you want to recreate_prefix: {W}")
    print("")
    if os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/1/.wine"):
        print(f"{Y} 1) remove prefix on container 1 {W}")
    if os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/2/.wine"):
        print(f"{Y} 2) remove prefix on container 2 {W}")
    if os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/3/.wine"):
        print(f"{Y} 3) remove prefix on container 3 {W}")
    if os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/4/.wine"):
        print(f"{Y} 4) remove prefix on container 4 {W}")
    if os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/5/.wine"):
        print(f"{Y} 5) remove prefix on container 5 {W}")
    print("")
    print(f"{Y} else) back to settings menu {W}")
    print("")
    user_input = input()
    if user_input not in ["1", "2", "3", "4", "5"]:
        change_setting()
    elif user_input == "1":
         shutil.rmtree('/data/data/com.termux/files/usr/glibc/opt/wine/1/.wine')
         print(f"{G} Done {W}")
    elif user_input == "2":
         shutil.rmtree('/data/data/com.termux/files/usr/glibc/opt/wine/2/.wine')
         print(f"{G} Done {W}")
    elif user_input == "3":
         shutil.rmtree('/data/data/com.termux/files/usr/glibc/opt/wine/3/.wine')
         print(f"{G} Done {W}")
    elif user_input == "4":
         shutil.rmtree('/data/data/com.termux/files/usr/glibc/opt/wine/4/.wine')
         print(f"{G} Done {W}")
    elif user_input == "5":
         shutil.rmtree('/data/data/com.termux/files/usr/glibc/opt/wine/5/.wine')
         print(f"{G} Done {W}")
    main_menu()
def xinput_support():
    print(f"{R}[{W}-{R}]{G}{BOLD} Select the version of Wine you want to add xinput support for: {W}")
    print("")
    for i in range(1, 6):
        wine_path = f"/data/data/com.termux/files/usr/glibc/opt/wine/{i}/.wine"
        if os.path.exists(wine_path):
            print(f"{Y} {i}) Add xinput support on container {i} {W}")
    print("")
    print(f"{Y} Else) Back to the settings menu {W}")
    print("")
    user_input = colored_input("Enter your choice: ")
    if user_input not in ["1", "2", "3", "4", "5"]:
        # Handle invalid input
        change_setting()
    else:
        wine_container = int(user_input)
        wine_lib64_path = f"/data/data/com.termux/files/usr/glibc/opt/wine/{wine_container}/wine/lib64"
        wine_lib_path = f"/data/data/com.termux/files/usr/glibc/opt/wine/{wine_container}/wine/lib/wine"
        if os.path.exists(wine_lib64_path):
            os.system(f"tar -xJf $PREFIX/glibc/opt/darkos/XinputBridge_ge.tar.xz -C /data/data/com.termux/files/usr/glibc/opt/wine/{wine_container}/wine/ &>/dev/null")
        else:
            os.system(f"tar -xJf $PREFIX/glibc/opt/darkos/XinputBridge.tar.xz -C {wine_lib_path} &>/dev/null")
        print(f"{R}[{W}-{R}]{G}{BOLD} xinput support added to Wine in container {C}{wine_container} {W}")
        time.sleep(2)
        change_setting()
def check_config_wine():
    config_folder = "/sdcard/darkos"
    exec(open('/sdcard/darkos/darkos_dynarec.conf').read())
def Compile():
    os.system("apt install cmake-glibc make-glibc python-glibc")
    os.system("pkg install -y git; unset LD_PRELOAD; export GLIBC_PREFIX=/data/data/com.termux/files/usr/glibc; export PATH=$GLIBC_PREFIX/bin:$PATH; cd ~/; git clone https://github.com/ptitSeb/box64; cd ~/box64; sed -i 's/\/usr/\/data\/data\/com.termux\/files\/usr\/glibc/g' CMakeLists.txt; sed -i 's/\/etc/\/data\/data\/com.termux\/files\/usr\/glibc\/etc/g' CMakeLists.txt; mkdir build; cd build; cmake --install-prefix $PREFIX/glibc .. -DARM_DYNAREC=1 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DBAD_SIGNAL=ON -DSD845=ON; make -j8; make install")
def install_wine9():
    os.system("wget -q --show-progress https://github.com/ahmad1abbadi/darkos/releases/download/beta/wine-default.tar.xz")
    os.system("tar -xJf wine-default.tar.xz -C $PREFIX/glibc/opt/wine/1")
    os.remove("wine-default.tar.xz")
def auto_start():
    os.system("clear")
    photo()
    print(f"{R}[{W}-{R}]{G}{BOLD} select what you refer: {W}")
    print("")
    print(f"{Y} 1) turn-on auto start os 👍 {W}")
    print("")
    print(f"{Y} 2) turn-off auto start os 👎 {W}")
    print("")
    print(f"{Y} else) back to settings menu {W}")
    choice = input()
    if choice != "1" and choice != "2":
        change_setting()
    elif choice == "1":
        command = "darkos"
        bashrc_path = os.path.expanduser('~/.bashrc')
        command_exists = False
        if os.path.exists(bashrc_path):
            with open(bashrc_path, 'r') as f:
                for line in f:
                    if command in line:
                        command_exists = True
                        print(f"{R}[{W}-{R}]{G}{BOLD} auto start os already activated... {W}")
                        time.sleep(2)
                        change_setting()
        if not command_exists:
            with open(bashrc_path, 'a') as f:
                f.write(command + '\n')
            print(f"{R}[{W}-{R}]{G}{BOLD} auto start os activated successfully {W}")
            time.sleep(2)
            change_setting()
    elif choice == "2":
        command = "darkos"
        bashrc_path = os.path.expanduser('~/.bashrc')
        command_exists = False
        if os.path.exists(bashrc_path):
            with open(bashrc_path, 'r') as f:
                lines = f.readlines()
            with open(bashrc_path, 'w') as f:
                for line in lines:
                    if command not in line:
                        f.write(line)
            print(f"{R}[{W}-{R}]{G}{BOLD} Auto start os deactivated successfully {W}")
            time.sleep(2)
            change_setting()
def styles():
    os.system("clear")
    photo()
    print(f"{R}[{W}-{R}]{G}{BOLD} install styles menu 🏞️ {W}")
    print("")
    print(f"{Y} 1) Windows 10 {W}")
    print("")
    print(f"{Y} 2) MacOS Style {W}")
    print("")
    print(f"{Y} 3) Manjaro Style {W}")
    print("")
    print(f"{Y} 4) Android Special Style {W}")
    print("")
    print(f"{Y} else) back to settings menu {W}")
    choice = input()
    if choice == "1":
        os.system("chmod +x $PREFIX/glibc/opt/scripts/install_win10_xfce4.sh")
        os.system("bash $PREFIX/glibc/opt/scripts/install_win10_xfce4.sh")
    elif choice == "2":
        os.system("chmod +x $PREFIX/glibc/opt/scripts/install_macos_xfce4.sh")
        os.system("bash $PREFIX/glibc/opt/scripts/install_macos_xfce4.sh")
    elif choice == "3":
        os.system("chmod +x $PREFIX/glibc/opt/scripts/install_manjaro_xfce.sh")
        os.system("bash $PREFIX/glibc/opt/scripts/install_manjaro_xfce.sh")
    elif choice == "4":
        os.system("chmod +x $PREFIX/glibc/opt/scripts/install_android_xfce.sh")
        os.system("bash $PREFIX/glibc/opt/scripts/install_android_xfce.sh")
        exit()
    else:
        change_setting()
def change_setting():
    os.system("clear")
    photo()
    print(f"{R}[{W}-{R}]{G}{BOLD} SETTINGS ⚙️ {W}")
    print(f"{Y} 1) Update OS 👑 {W}")
    print(f"{Y} 2) Wine manager 🍷 {W}")
    print(f"{Y} 3) Change box86-box64 version 📥 {W}")
    print(f"{Y} 4) Delete prefix 🪡 {W}")
    print(f"{Y} 5) Change auto start setting 🖱️ {W}")
    print(f"{Y} 6) Debug mode 🔧 {W}")
    print(f"{Y} 7) Fix prefix for non wow64 wine ♻️ {W}")
    print(f"{Y} 8) Boost cpu 🔥 (needed root in some devices) {W}")
    print(f"{Y} 9) Install Styles For Dark Os 🎭 {W}")
    print(f"{Y} 10) winetricks ⛑️ {W}")
    print(f"{Y} 11) add xinput support to wine 👾 (experimental) {W}")
    print(f"{Y} else) Back 🔙 {W}")
    print("")
    choice = input()
    if choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6" and choice != "7" and choice != "8" and choice != "9" and choice != "10" and choice != "dev" and choice != "11":
        print(f"{G} ........... {W}")
        main_menu()
    elif choice == "3":
        box_version()
    elif choice == "dev":
        os.system("clear")
        print(f"{G}{BOLD} share log file on our Telegram group {W}")
        print(f"{G} dev mode {W}")
        os.system("BOX86_LOG=1 BOX86_SHOWSEGV=1 BOX86_DYNAREC_LOG=1 BOX86_DYNAREC_MISSING=1 BOX86_DLSYM_ERROR=1 BOX64_LOG=1 BOX64_SHOWSEGV=1 BOX64_DYNAREC_LOG=1 BOX64_DYNAREC_MISSING=1 WINEDEBUG=warn+all BOX64_DLSYM_ERROR=1 WINEDEBUG=+err taskset -c 4-7 box64 wine64 explorer /desktop=shell,800x600 $PREFIX/glibc/opt/apps/pc.ex >/sdcard/darkos.log")
    elif choice == "1":
        print("")
        print(f"{G} Shutdown OS.... {W}")
        print("")
        print(f"{Y} checking 🔎..... {W}")
        time.sleep(1)
        response = urllib.request.urlopen(url)
        latest_version = response.read().decode('utf-8').strip()
        try:
            if latest_version > current_version:
                print(f"{R}[{W}-{R}]{C}{BOLD} update available..... updating......📥 {W}")
                os.system("python3 $PREFIX/bin/update-darkos.py")
                time.sleep(3)
                change_setting()
        except urllib.error.HTTPError as e:
            if e.code == 404:
                os.system("clear")
                print(f"{R} no internet connection 😵 backing to the settings {W}")
                time.sleep(3)
                change_setting()
        else:
            print(f"{R}[{W}-{R}]{G}{BOLD} no update available {W}")
            time.sleep(3)
            change_setting()
    elif choice == "2":
        os.system("python3 $PREFIX/bin/setting-darkos.py")
    elif choice == "6":
        os.system("python3 $PREFIX/bin/debug-darkos.py")
    elif choice == "9":
        print("")
        styles()
    elif choice == "r":
        print(f"{R}[{W}-{R}]{G} to contact developer via telegram channel.... {C}(https://t.me/DARKOS4android) {W}")
        back = input("🔙 = 1")
        if back == "1":
            change_setting()
    elif choice == "4":
        recreate_prefix_wineAZ()
    elif choice == "5":
        auto_start()
    elif choice == "7":
        recreate_32bit()
    elif choice == "10":
        winetricks()
    elif choice == "11":
        os.system("clear")
        photo()
        xinput_support()
    elif choice == "8":
        os.system("clear")
        photo()
        print(f"{Y} loading......... {W}")
        reload()
        new_sesson()
        print(f"{R}[{W}-{R}]{G}{BOLD} installing python packages {W}")
        os.system('pkg install python vulkan-tools python-pip coreutils &> /dev/null')
        print("")
        os.system('pip install aiofiles psutil blessings &> /dev/null')
        print(f"{R}[{W}-{R}]{G} python packages.... 100% {W}")
        print("")
        print(f"{R}[{W}-{R}]{G}{BOLD} starting boost 💥 {W}")
        time.sleep(3)
        print("")
        print(f"{R}[{W}-{R}]{G} check the new session for more info 👀 {W}")
        time.sleep(5)
        change_setting()
def box_version():
    os.system("clear")
    photo()
    print(f"{R}[{W}-{R}]{G}{BOLD} select box version: {W}")
    print("")
    print(f"{Y} 1) SAFE-BOX {W}")
    print(f"{Y} 2) Compile and UPDATED BOX64 {W}")
    print(f"{Y} 3) BOX86 FOR Wine non-wow64 version {W}")
    print(f"{Y} else) CANCEL AND BACK {W}")
    print("")
    choice = input()
    file_path64 = "/data/data/com.termux/files/usr/glibc/bin/box64"
    file_path86 = "/data/data/com.termux/files/usr/glibc/bin/box86"
    if choice not in ["1", "2", "3"]:
        change_setting()
    elif choice == "1":
        if os.path.exists(file_path64):
            os.remove(file_path64)
        if os.path.exists(file_path86):
            os.remove(file_path86)
        os.system("tar -xJf $PREFIX/glibc/opt/box/safe-box.tar.xz -C $PREFIX/glibc/bin/")
        os.system("chmod +x $PREFIX/glibc/bin/box86")
        os.system("chmod +x $PREFIX/glibc/bin/box64") 
        change_setting()
    elif choice == "2":
        if os.path.exists(file_path64):
            os.remove(file_path64)
        print(f"{R}[{W}-{R}]{G}{BOLD} compiling.... {W}")
        os.system("apt install cmake-glibc make-glibc python-glibc -y &>/dev/null")
        Compile()
        os.system("mv //data/data/com.termux/files/home/box64/build/box64 $PREFIX/glibc/bin/")
        os.system("chmod +x $PREFIX/glibc/bin/box64")
        shutil.rmtree('/data/data/com.termux/files/home/box64')
        print(f"{G}{BOLD} done {W}")
        time.sleep(2)
        change_setting()
    elif choice == "3":
        os.system("wget https://github.com/ahmad1abbadi/darkos/releases/download/beta/box.tar.xz")
        if os.path.exists(file_path64):
            os.remove(file_path64)
        if os.path.exists(file_path86):
            os.remove(file_path86)
        os.system("tar -xJf box.tar.xz -C $PREFIX/glibc/bin/")
        os.system("chmod +x $PREFIX/glibc/bin/box86")
        os.system("chmod +x $PREFIX/glibc/bin/box64")
        change_setting()
def reload():
    file_path = os.path.expanduser("~/.termux/termux.properties")
    with open(file_path, "r") as file:
        lines = file.readlines()
    with open(file_path, "w") as file:
        for line in lines:
            if line.startswith("# allow-external-apps = true"):
                line = line.replace("# ", "")
            file.write(line)
            #print(f"File updated: {file_path}")
    os.system("termux-reload-settings")
def new_sesson():
    os.system("am startservice --user 0 -n com.termux/com.termux.app.RunCommandService \
    -a com.termux.RUN_COMMAND \
    --es com.termux.RUN_COMMAND_PATH '/data/data/com.termux/files/usr/bin/python' \
    --esa com.termux.RUN_COMMAND_ARGUMENTS '/data/data/com.termux/files/usr/bin/cpu_boost.py' \
    --es com.termux.RUN_COMMAND_WORKDIR '/data/data/com.termux/files/home' \
    --ez com.termux.RUN_COMMAND_BACKGROUND 'false' \
    --es com.termux.RUN_COMMAND_SESSION_ACTION '1' &> /dev/null ")
def main_menu():
    os.system("clear")
    photo()
    print(f"{R}[{W}-{R}]{G}{BOLD} welcome to darkos safe mode {W}")
    print("")
    print(f"{R}[{W}-{R}]{G}{BOLD} Select what you need to do: {W}")
    print(f"{Y} 1) START DARK OS IN SAFE MODE 🚑 {W}")
    print(f"{Y} 2) SETTINGS ⚙️ {W}")
    print(f"{Y} 3) EXIT SAFE MODE 🚪 {W}")
    print(f"{Y} 4) KILL DARK OS AND EXIT TO TERMINAL 😭 {W}")
    print("")
    main()
    choice = input()
    if choice != "1" and choice != "2" and choice != "3" and choice != "4":
        print(f"{R} wrong {W}")
        main_menu()
    elif choice == "1":
        wine_container()
    elif choice == "2":
        change_setting()
    elif choice == "3":
        print("")
        os.system("clear")
        photo()
        print("")
        print(f"{R}[{W}-{R}]{G}{BOLD} Restarting..... {W}")
        time.sleep(1)
        print("")
        subprocess.run(["bash", "darkos"])
    elif choice == "4":
        print("")
        os.system("clear")
        photo()
        print("")
        print(f"{R}[{W}-{R}]{C}{BOLD} good bye 😭 {W}")
        os.system('pkill -f "app_process / com.termux.x11"')
        os.system('pkill -f pulseaudio')
        os._exit(0)
start_darkos()
main_menu()

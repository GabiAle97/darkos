#!/bin/bash
clear
echo "Updating Termux packages list. Please wait..."
apt update > /dev/null
echo "Upgrading Termux tools..."
apt-get upgrade termux-tools -y > /dev/null
echo "Selecting the best Termux packages mirror. Please wait..."
unlink "$PREFIX/etc/termux/chosen_mirrors" > /dev/null
ln -s "$PREFIX/etc/termux/mirrors/all" "$PREFIX/etc/termux/chosen_mirrors" > /dev/null
TERMUX_APP_PACKAGE_MANAGER=apt pkg --check-mirror update
echo "Upgrading Termux packages. This might take some time..."
apt-get -y --with-new-pkgs -o Dpkg::Options::="--force-confdef" upgrade > /dev/null
echo "Please allow storage permission."
termux-setup-storage
echo "Installing Python..."
apt install python --no-install-recommends -y > /dev/null
echo "Please be patient..."
curl -o installglibc.py https://raw.githubusercontent.com/ahmad1abbadi/darkos/main/installglibc.py && python3 installglibc.py
exit

#!/bin/bash

clear
echo "==============================================================================="
echo "                      UNKNOW 23 - Dependency Installer"
echo "==============================================================================="
sleep 1


if [[ $EUID -ne 0 ]]; then
   echo "[!] run this script with root : sudo ./install.sh"
   exit 1
fi
   echo "[+] Update and Upgrade"
   sudo apt update && sudo apt upgrade -y

   echo "[+] Install the system dependencies"
   sudo apt install -y python3-venv python3-pip figlet curl wget php

   echo "[*] Install the other system dependencies..."
apt install -y
python3 \
python3-pip \
python2 \
php \
bash \
curl \
wget \
figlet \
git \
lolcat


echo "[+] Create VENV"
python3 -m venv venv

echo "[+] Activate VENV"
source venv/bin/activate

echo "[+] update of pip"
pip install --upgrade pip

echo "[+] Install the python dependencies"
pip install -r requirements.txt

echo "[+] Desactivate VENV"
deactivate

echo
echo "[✔] Installation terminée !"
echo "run the tool with : python3 unknow23.py"

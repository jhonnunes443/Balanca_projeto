#!/bin/bash
sudo apt install git -y
sudo apt install python3-pip -y

git clone https://github.com/jhonnunes443/balanca_projeto.git
pip install -r /Balanca_projeto/requirements.txt
python3 /Balanca_projeto/Balanca_final.py

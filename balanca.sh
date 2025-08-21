#!/bin/bash
sudo apt install git -y
sudo apt install python3-pip -y

git clone https://github.com/jhonnunes/balanca_projeto.git
pip install -r /balanca_projeto/requirements.txt
python3 /balanca_projeto/Balanca_final.py

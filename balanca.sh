#!/bin/bash

if ! command -v git &> /dev/null; then
    echo "Git não encontrado. Instalando..."
    sudo apt install git -y
else
    echo "Git já está instalado."
fi

if ! command -v python3 &> /dev/null || ! command -v pip3 &> /dev/null; then
    echo "Python3 ou pip3 não encontrados. Instalando..."
    sudo apt install python3-pip -y
else
    echo "Python3 e pip3 já estão instalados."
fi

if [ ! -d "Balanca_projeto" ]; then
    git clone https://github.com/jhonnunes443/Balanca_projeto.git
else
    echo "Repositório 'Balanca_projeto' já existe. Pulando o clone."
fi

chmod +x Balanca_projeto/balanca.sh
./Balanca_projeto/Balanca_final.py

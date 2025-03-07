#!/bin/bash

function erro() {
    echo "Erro: $1"
    exit 1
}

function verificar_comando() {
    if [[ $? -ne 0 ]]; then
        erro "$1"
    fi
}

function verificar_existencia() {
    if [[ ! -e "$1" ]]; then
        erro "$2"
    fi
}

function configurar_ambiente_virtual() {
    if [[ ! -d ".venv" ]]; then
        echo "Criando ambiente virtual..."
        python3 -m venv .venv
        verificar_comando "Falha ao criar o ambiente virtual. Verifique se o python3-venv está instalado."
    fi

    source .venv/bin/activate
    verificar_comando "Falha ao ativar o ambiente virtual."
}

function instalar_dependencia() {
    local pacote=$1
    pip3 show "$pacote" > /dev/null 2>&1
    if [[ $? -ne 0 ]]; then
        echo "$pacote não encontrado. Instalando..."
        pip3 install "$pacote" > /dev/null 2>&1
        verificar_comando "Falha ao instalar $pacote. Verifique sua conexão com a internet."
        echo "$pacote instalado com sucesso."
    fi
}

function executar_script() {
    python3 main.py
    verificar_comando "Erro durante a execução do script. Verifique o arquivo de log para mais detalhes."
}

function main() {
    cd "$(dirname "$0")" || erro "Falha ao mudar para o diretório do script."

    verificar_existencia "main.py" "O arquivo 'main.py' não foi encontrado no diretório corrente."

    configurar_ambiente_virtual

    instalar_dependencia selenium
    instalar_dependencia requests

    executar_script

    deactivate
}

main
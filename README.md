# Projeto de Mineração de Bitcoin

Este projeto automatiza o processo de mineração de Bitcoin utilizando Selenium para interagir com o site [FreeMining.club](https://www.freemining.club). Ele verifica saldos, contrata planos de mineração e exibe um sumário dos saldos em BTC e BRL.



## Estrutura do Projeto
Aqui está a árvore de diretórios e arquivos do projeto:

```bash
projeto/
│
├── func/                       # Pasta com módulos de funções
│   ├── __init__.py             # Arquivo de inicialização do pacote
│   ├── formatacao.py           # Funções para formatação de valores
│   ├── cotacao.py              # Funções para obter a cotação do Bitcoin
│   ├── navegador.py            # Funções para configurar o navegador
│   ├── mineracao.py            # Funções para iniciar a mineração
│   ├── saldo.py                # Funções para verificar saldos
│   ├── saque.py                # Funções para processar saques (não implementado)
│   ├── plano.py                # Funções para verificar e contratar planos
│   └── sumario.py              # Funções para formatar e exibir o sumário
│
├── carteiras.txt               # Arquivo com as carteiras de Bitcoin (uma por linha)
├── main.py                     # Script principal
├── start.sh                    # Script de inicialização do projeto
├── execution.log               # Arquivo de log gerado durante a execução
└── README.md                   # Documentação do projeto
```

## Pré-requisitos
1. **Python 3**: Certifique-se de ter o Python 3 instalado.
2. **Pip**: Gerenciador de pacotes do Python.
3. **Selenium**: Biblioteca para automação de navegadores.
4. **Requests**: Biblioteca para fazer requisições HTTP.
5. **Google Chrome**: Navegador utilizado pelo Selenium.
6. **ChromeDriver**: Driver para o Google Chrome (compatível com a versão do Chrome instalada).


## Configuração
### 1. Configurar o ambiente virtual
O script start.sh já cria e ativa um ambiente virtual automaticamente. Se preferir fazer manualmente:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 2. Instalar dependências
As dependências serão instaladas automaticamente pelo start.sh. Para instalar manualmente:

```bash
pip install selenium requests
```

---

### 3. Configurar o arquivo carteiras.txt
Adicione as carteiras de Bitcoin que deseja processar no arquivo carteiras.txt, uma por linha. Exemplo:

```bash
bc1************yr4************************
bc1**************************aW2**********
bc1************************************09i
```

---

### 4. Configurar o ChromeDriver
Baixe o ChromeDriver compatível com a versão do seu Google Chrome e coloque-o no PATH do sistema ou no diretório do projeto. Certifique-se de que o ChromeDriver está acessível.

## Executando o Projeto
### 1. Executar o script
Para executar o projeto, use o script start.sh:

```bash
./start.sh
```

---

### 2. Verificar logs
O script gera um arquivo de log chamado execution.log na raiz do projeto. Ele contém todas as mensagens de log, incluindo erros e informações sobre o processamento das carteiras.

## Agendando no Crontab
Para agendar a execução do script a cada duas horas, siga os passos abaixo:

### Abra o crontab para edição:

```bash
crontab -e
```

---

### Adicione a seguinte linha para executar o script a cada duas horas:

```bash
0 */2 * * * /caminho/para/o/projeto/start.sh
```

---

### Substitua /caminho/para/o/projeto/ pelo caminho absoluto do diretório do projeto.

Salve e saia do editor.

## Detalhes dos Arquivos
### 1. main.py
* **Função**: Script principal que orquestra a execução do projeto.
* **O que faz**:
    * Lê as carteiras do arquivo carteiras.txt.
    * Obtém a cotação do Bitcoin em BRL.
    * Inicia a mineração para cada carteira.
    * Verifica saldos e contrata planos de mineração.
    * Exibe um sumário dos saldos.

### 2. start.sh
* **Função**: Script de inicialização do projeto.
* **O que faz**:
    * Configura o ambiente virtual.
    * Instala as dependências necessárias (selenium e requests).
    * Executa o script main.py.

### 3. carteiras.txt
* **Função**: Armazena as carteiras de Bitcoin que serão processadas.
* **Formato**: Uma carteira por linha.

4. execution.log
* **Função**: Armazena os logs gerados durante a execução do script.
* **O que contém**:
    * Informações sobre o processamento das carteiras.
    * Erros e mensagens de depuração.

## Exemplo de Saída
### Aqui está um exemplo de saída do script:

```bash
2025-03-07 07:39:02,419 - INFO - Cotação atual do Bitcoin: R$ 513.983,00 BRL
2025-03-07 07:39:02,419 - INFO - Processando carteira: ******************************************
2025-03-07 07:39:02,419 - INFO - Plano: Plano Básico | BTC/Min: 0.00000050 | BTC/Day: 0.00072000
2025-03-07 07:39:02,419 - INFO - Saldo atual: 0.00123456 BTC | R$ 634,12 BRL
2025-03-07 07:39:02,419 - INFO - Condições atendidas para contratar o próximo plano: BTC/Min = 0.00000200, BTC/Day = 0.00288
2025-03-07 07:39:02,419 - INFO - Novo plano contratado com sucesso!
2025-03-07 07:39:02,419 - INFO - Processando carteira: ******************************************
```

## Considerações Finais
* **Segurança**: Nunca compartilhe suas carteiras de Bitcoin publicamente.

* **Atualizações**: Verifique regularmente se o site FreeMining.club mudou sua estrutura, pois isso pode quebrar o script.

* **Contribuições**: Sinta-se à vontade para contribuir com melhorias no projeto.
# movimentação-financeira

Você pode fazer upload de um arquivo CNAB com os dados de movimentações financeiras de várias lojas, esses dados vão ser exibidos em tela.

# Sobre a aplicação

Para construir e executar o programa, utilizamos as seguintes tecnologias:

python e o framework DJANGO.

# Instalação e uso

Faça o fork do repositório e em seguida execute o comando git clone para clonar o projeto para seu dispositivo. Dentro da pasta do projeto, execute o comando abaixo para instalar todas as dependências da aplicação.

pip install -r requirements.txt

# Ambiente Virtual

Verifique se sua versão instalada do Python é a 3.10.0 ou superior: 
python -V
Para fazer a criação do nosso ambiente virtual, use o comando no diretório raiz do projeto:
python -m venv venv

Ativar o venv source: venv/bin/activate

Ativar o venv no windows:  .\venv\Scripts\activate

# DB
db.sqlite3

Para executar as makemigrations: 

python manage.py makemigrations

python manage.py migrate

Executar o servidor:
python manage.py runserver

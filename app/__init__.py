from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script._compat import Manager
from flask_migrate import Migrate, MigrateCommand



app = Flask(__name__)

# configuração do caminho que vai fazer até o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db' # configurando URI do banco de dados 
# banco de dados
db = SQLAlchemy(app)

# esse migrate vai cuidar das minhas migrações
migrate = Migrate(app, db)

# Controle de informações que a vai passar na execução
manager = Manager(app)
# vai cuidar dos comandos que vou usar pra inicializar a minha aplicção

manager.add_command('db', MigrateCommand)
                    
from app.controlers import default

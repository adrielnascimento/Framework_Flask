from app import db

# db.model é uma classe do sqlalchemy que trás um modelo de tabela padrão
class User(db.Model): 
    __tablename__ = "users" # parametro configurando o nome da tabela la no banco de dados.

    # Criação das colunas. 
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    nome = db.Column(db.String)
    email = db.Column(db.String(120), unique=True)
    
    # Construtor
    def __init__(self, username, password, nome, email):
        self.username = username
        self.password = password 
        self.nome = nome 
        self.email = email 

    # repr, uma apresentação é o jeito que essa classe vai aparecer quando fizer uma pesquisa no banco (Uma forma "bonitinha" de mostrar os registros).
    def __repr__(self):
         return "<User %r>" % self.username

# Tabela dos posts
class Post(db.Model): 
    __tablename__ = "posts"

    id = db.Column(id.Integer, primary_key=True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    # esse comando vera todas as informações do usuario que está relacionando essa tabela
    user = db.relationship('User', foreign_keys=user_id)

    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id
    
    def __repr__(self): 
        return "<Post %r>" % self.id

# tabela do follow
class Follow(db.Model): 
    __tablename__ = "follow"

    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'))
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user1 = db.relationship('User', foreign_keys=id_user)
    user2 = db.relationship('User', foreign_keys=follower_id)


    def __init__(self, id_user, follower_id):
        self.id_user = id_user
        self.follower_id = follower_id
        
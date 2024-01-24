from mercado import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  usuario = db.Column(db.String(length=30), nullable=False)
  email = db.Column(db.String(length=50), nullable=False, unique=True)
  senha = db.Column(db.String(length=60), nullable=False, unique=True)
  valor = db.Column(db.Integer, nullable=False, default=5000)
  items = db.relationship('Item', backref='admin_user', lazy=True)

class Item(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(length=30), nullable=False, unique=True)
  preco = db.Column(db.Integer, nullable=False)
  cod_barra = db.Column(db.String(length=12), nullable=False, unique=True)
  descricao = db.Column(db.String(length=1024), nullable=False, unique=True)
  admin = db.Column(db.Integer, db.ForeignKey('user.id'))

  def __repr__(self):
    return f"Item {self.nome}"

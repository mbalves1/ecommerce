from mercado import app
from flask import render_template
from mercado.models import Item
from forms import CadastroForm

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/produtos')
def page_produto():
  items = Item.query.all()
  return render_template('produtos.html', items=items)

@app.route('/cadastro')
def page_cadastro():
  form = CadastroForm()
  return render_template('cadastro.html', form=form)
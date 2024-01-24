from mercado import app
from flask import render_template, redirect, url_for
from mercado.models import Item, User
from mercado.forms import CadastroForm
from mercado import db

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/produtos')
def page_produto():
  items = Item.query.all()
  return render_template('produtos.html', items=items)

@app.route('/cadastro', methods=['GET', 'POST'])
def page_cadastro():
  form = CadastroForm()
  if form.validate_on_submit():
    usuario = User(
      usuario = form.usuario.data,
      email = form.email.data,
      senha = form.senha1.data
    )
    print("user", usuario)
    db.session.add(usuario)
    db.session.commit()
    return redirect(url_for('page_produto'))
  if form.errors != {}:
    for err in form.errors.values():
      print(f"Erro ao cadastrar usuário!")

  return render_template('cadastro.html', form=form)
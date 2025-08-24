from flask import Blueprint, render_template, redirect, url_for, abort
from . import db
from .models import Usuario

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/add_user/<nombre>/<email>')
def add_user(nombre, email):
    if not nombre or not email:
        abort(400, description='Nombre y email son requeridos')

    # Evitar duplicados por email (tiene unique=True)
    exists = db.session.query(Usuario.id).filter_by(email=email).first()
    if exists:
        return redirect(url_for('main.usuarios'))

    usuario = Usuario(nombre=nombre, email=email)
    db.session.add(usuario)
    db.session.commit()
    return redirect(url_for('main.usuarios'))

@main.route('/usuarios')
def usuarios():
    usuarios = Usuario.query.all()
    return render_template('usuarios.html', usuarios=usuarios)

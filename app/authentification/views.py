from flask import render_template
from . import auth

@auth.route('/register', methods=('GET', 'POST'))
def register():
   return render_template('authentification/register.html')

@auth.route('/login', methods=('GET', 'POST'))
def login():
   return render_template('authentification/login.html')
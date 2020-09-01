from flask import render_template, flash, url_for, redirect, request, session
from app.user.forms import (AjoutUserForm)
from . import user
from ..models import User, Communaute
from .. import db, bcrypt
from app.package.fonction import utilisateur, role_utilisateur




""" Communauté """
@user.route('/ajouter', methods=['GET', 'POST'])
def ajouter_utilisateur():
   # Title
   title="{} | Sr. Xavérienne".format('Utilisateur')
   #Vérification de l'existenc d'aumoins une communaute
   communaute=Communaute.query.all()
   if len(communaute) == 0:
      flash("Ajouter d'abord aumoins une communaute",'danger')
      return redirect(url_for('communaute.communaute'))
   # Formulaire
   form=AjoutUserForm()
   
   if form.validate_on_submit():
      
      #Username et/ou mot de passe
      username=utilisateur(form.prenom.data,form.post_nom.data,user_pass=False)
      if username is None:
         flash("Priere d'indique le Prénom et le Post-nom")
         print('Le compte existe déjà')
         return redirect(url_for('user.ajouter_utilisateur'))
      
      #Role de l'utilisateur
      role=role_utilisateur(form.role.data)
      if role is None:
         print('Role existe déjà')
         flash("La mère superieure existe déjà",'danger')
         return redirect(url_for("user.ajouter_utilisateur"))
      
      #Mot de passe
      password_hash=bcrypt.generate_password_hash(form.password.data).decode('utf-8') #génération du password Hacher
      #Enregistrement
      user_add=User(nom=form.nom.data.upper(), post_nom=form.post_nom.data.upper(), prenom=form.prenom.data.capitalize(),
                    tel=form.tel.data, username=username, password_vis=form.password.data, password=password_hash, role=form.role.data, communaute_id=form.communaute.data.id)
      db.session.add(user_add)
      db.session.commit()
      flash("Ajout avec succès",'success')
      return redirect(url_for("user.index"))
   return render_template('user/ajouter.html', title=title, form=form)



"""Affichage de l'index"""
@user.route('/', methods=['GET', 'POST'])
def index():
   # Title
   title="{} | Sr. Xavérienne".format('Utilisateur')
   #Les utilisateurs
   utilisateurs=User.query.order_by(User.id.asc()).all()
   print(utilisateurs,'__________________________________________________')
   
   return render_template('user/index.html', title=title, utilisateur=utilisateurs)




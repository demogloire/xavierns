from flask import render_template, flash, url_for, redirect, request, session
from app.user.forms import (AjoutUserForm, EditerUserForm, SuperUserForm)
from . import user
from ..models import User, Communaute
from .. import db, bcrypt
from app.package.fonction import utilisateur, role_utilisateur




""" Ajout de l'utilisateur """
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
   
   return render_template('user/index.html', title=title, utilisateur=utilisateurs)


""" Modification des utilisateurs """
@user.route('/<int:id>', methods=['GET', 'POST'])
def editet_utilisateur(id):
   # Title
   title="{} | Sr. Xavérienne".format('Utilisateur')
   # Formulaire
   form=EditerUserForm()
   #Id de l'utilisateur
   id=id
   #Requete de vérification
   utilisateur=User.query.filter_by(id=id).first_or_404()
   #Mise à jour des opérations
   if form.validate_on_submit():
      #Enregistrement
      if utilisateur.role == form.role.data:
         utilisateur.nom=form.nom.data.upper()
         utilisateur.post_nom=form.post_nom.data.upper()
         utilisateur.prenom=form.prenom.data.capitalize()
         utilisateur.tel=form.tel.data
         utilisateur.communaute_id=form.communaute.data.id
         db.session.commit()
         
         flash("Modification de l'utilisateur",'success')
         return redirect(url_for("user.index"))
      else:
         if form.role.data =='Mère supérieure':
            print("2_______________________________")
            flash("Attention cette permission est pour la Mère superieure",'success')
            return redirect(url_for("user.editet_utilisateur", id=id)) 
         utilisateur.nom=form.nom.data.upper()
         utilisateur.post_nom=form.post_nom.data.upper()
         utilisateur.prenom=form.prenom.data.capitalize()
         utilisateur.tel=form.tel.data
         utilisateur.role=form.role.data
         utilisateur.communaute_id=form.communaute.data.id
         db.session.commit()
         print("3_______________________________")
         flash("Modification de l'utilisateur",'success')
         return redirect(url_for("user.index"))
   #envoir des informations de mise à jour
   if request.method=='GET':
      form.nom.data=utilisateur.nom
      form.post_nom.data=utilisateur.post_nom
      form.prenom.data=utilisateur.prenom
      form.tel.data=utilisateur.tel
      form.role.data=utilisateur.role
      form.communaute.data=utilisateur.communaute_user
      
      
   return render_template('user/edit.html', title=title, form=form)


""" Blocage de l'utilisateur """
@user.route('/act/<int:id>', methods=['GET','POST'])
def activation(id):
   user_act=User.query.filter_by(id=id).first_or_404()
   message=None
   if user_act.statut==True:
      user_act.statut=False
      message="Vous avez bloqué l'utilisateur"
      db.session.commit()
   else:
      user_act.statut=True
      message="Vous avez debliqué l'utilisateur"
      db.session.commit()
   flash("{}".format(message),'success')
   return redirect(url_for('user.index'))
      

""" Ajout de l'utilisateur """
@user.route('/super_admin_ajouter', methods=['GET', 'POST'])
def superajouterutilisateur():
   # Title
   title="{} | Sr. Xavérienne".format('Super admin')
   form=SuperUserForm()
   
   if form.validate_on_submit():
      #Username et/ou mot de passe
      username=utilisateur(form.prenom.data,form.post_nom.data,user_pass=True)
      username_compte, password=username
      if username is None:
         flash("Priere d'indique le Prénom et le Post-nom")
         return redirect(url_for('auth.login'))
      
      #Mot de passe
      password_hash=bcrypt.generate_password_hash(password).decode('utf-8') #génération du password Hacher
      #Enregistrement
      user_add=User(nom=form.nom.data.upper(), post_nom=form.post_nom.data.upper(), prenom=form.prenom.data.capitalize(),
                    tel=form.tel.data, username=username, password_vis=password, password=password_hash, role=form.role.data)
      db.session.add(user_add)
      db.session.commit()
      flash("Ajout avec succès",'success')
      return redirect(url_for('auth.login'))
   return render_template('user/super_ajouter.html', title=title, form=form)


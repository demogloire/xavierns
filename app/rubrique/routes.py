from flask import render_template, flash, url_for, redirect, request, session
from app.rubrique.forms import (AjoutRubriqueForm, EditRubriqueForm)
from . import rubrique
from ..models import Communaute, Rubrique
from .. import db



""" Editer un rubrique """
@rubrique.route('/<int:id>', methods=['POST', 'GET'])
def editer_rubrique(id):
   title="{} | Sr. Xavérienne".format('Rubrique')
   # Formulaire
   form=EditRubriqueForm()
   #Requete de formulaire
   id_rubrique=Rubrique.query.filter_by(id=id).first_or_404()
   # Editer le formulaire
   if form.validate_on_submit():
      if form.nom.data==id_rubrique.nom:
         # Enregistrement des données
         db.session.commit()
         flash('Enregistremet réussi','success')
         return redirect(url_for('rubrique.rubrique'))
      else:
         id_rubrique.nom=form.nom.data
      
         # Enregistrement des données
         db.session.commit()
         flash('Enregistremet réussi','success')
         return redirect(url_for('rubrique.rubrique'))
         
   if request.method =='GET':
      form.nom.data=id_rubrique.nom
   return render_template('rubrique/edit_rubrique.html', title=title, form=form)




@rubrique.route('/ajouter', methods=['GET', 'POST'])
def ajout_rubrique():
   # Title
   title="{} | Sr. Xavérienne".format('Rubrique')
   # Formulaire
   form=AjoutRubriqueForm()
   #  Selection de tous les rubriques de la BD 
   rubrique_req=Rubrique.query.all()
   #Ajout du formulaire
   if form.validate_on_submit():
      ajout=Rubrique(nom=form.nom.data)
      db.session.add(ajout)
      db.session.commit()
      flash('Enregistremet réussi','success')
      return redirect(url_for('rubrique.ajout_rubrique'))
   
   return render_template('rubrique/ajout_rubrique.html', title=title, form=form, rubrique=rubrique_req)








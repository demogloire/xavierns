from flask import render_template, flash, url_for, redirect, request, session
from app.communaute.forms import (AjoutCommunauteForm, EditCommunauteForm)
from . import communaute
from ..models import Communaute
from .. import db



""" Editer la communauté """
@communaute.route('/<int:id>', methods=['POST', 'GET'])
def communaute_maj(id):
   title="{} | Sr. Xavérienne".format('Communauté')
   # Formulaire
   form=EditCommunauteForm()
   #Requete de formulaire
   id_communaute=Communaute.query.filter_by(id=id).first_or_404()
   # Editer le formulaire
   if form.validate_on_submit():
      if form.nom.data==id_communaute.nom:
         id_communaute.lieu=form.lieu.data
         id_communaute.province=form.province.data
         id_communaute.pays=form.pays.data
         # Enregistrement des données
         db.session.commit()
         flash('Enregistremet réussi','success')
         return redirect(url_for('communaute.communaute'))
      else:
         id_communaute.nom=form.nom.data
         id_communaute.lieu=form.lieu.data
         id_communaute.province=form.province.data
         id_communaute.pays=form.pays.data
         # Enregistrement des données
         db.session.commit()
         flash('Enregistremet réussi','success')
         return redirect(url_for('communaute.communaute'))
         
   if request.method =='GET':
      form.nom.data=id_communaute.nom
      form.lieu.data=id_communaute.lieu
      form.province.data=id_communaute.province
      form.pays.data=id_communaute.pays
   return render_template('communaute/edit.html', title=title, form=form)


""" Communauté """
@communaute.route('/communaute', methods=['GET', 'POST'])
def communaute():
   # Title
   title="{} | Sr. Xavérienne".format('Communauté')
   # Formulaire
   form=AjoutCommunauteForm()
   #  Une communauté  
   communaute_req=Communaute.query.all()
   #Ajout du formulaire
   if form.validate_on_submit():
      enregistrement=Communaute(nom=form.nom.data, lieu=form.lieu.data, province=form.province.data, pays=form.pays.data)
      db.session.add(enregistrement)
      db.session.commit()
      flash('Enregistremet réussi','success')
      return redirect(url_for('communaute.communaute'))
   #Envoi du pays en formulaire
   if request.method=='GET':
      form.pays.data='RDCongo'
   
   return render_template('communaute/ajouter.html', title=title, form=form, communaute=communaute_req)




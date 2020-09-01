from app import db, login_manager
from datetime import datetime, date
from sqlalchemy.orm import backref
from flask_login import UserMixin, current_user



class Rubrique(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nom=db.Column(db.String(120))
    statut=db.Column(db.Boolean, default=True)
    affectation=db.Column(db.Boolean, default=True)
    rubrique_communautes=db.relationship('Rubriquecommunaute', backref='rubrique_communaute', lazy='dynamic')

class User(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    nom=db.Column(db.String(120))
    post_nom=db.Column(db.String(120))
    prenom=db.Column(db.String(120))
    role=db.Column(db.String(120))
    tel=db.Column(db.String(120))
    username=db.Column(db.String(120))
    password=db.Column(db.String(255))
    password_vis=db.Column(db.String(255))
    avatar=db.Column(db.String(120))
    statut=db.Column(db.Boolean, default=True)
    communaute_id=db.Column(db.Integer, db.ForeignKey('communaute.id'))
    operations=db.relationship('Operation', backref='user_operation', lazy='dynamic')
    

class Communaute(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nom=db.Column(db.String(120))
    lieu=db.Column(db.String(120))
    province=db.Column(db.String(120))
    pays=db.Column(db.String(120))
    users=db.relationship('User', backref='communaute_user', lazy='dynamic')
    rubriquecommunautes=db.relationship('Rubriquecommunaute', backref='rubcom', lazy='dynamic')
    syntheses=db.relationship('Synthese', backref='communaute_synthese', lazy='dynamic')
    soldes=db.relationship('Solde', backref='communaute_solde', lazy='dynamic')
     
class Operation(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    designation=db.Column(db.String(255))
    montant_usd=db.Column(db.DECIMAL(precision=10, scale=2, asdecimal=False))
    montant_cdf=db.Column(db.DECIMAL(precision=10, scale=2, asdecimal=False))
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    rubriquecommunaute_id=db.Column(db.Integer, db.ForeignKey('rubriquecommunaute.id'), nullable=False)
    source_id=db.Column(db.Integer, db.ForeignKey('source.id'), nullable=False)
    annee_id=db.Column(db.Integer, db.ForeignKey('annee.id'), nullable=False)
    taux_id=db.Column(db.Integer, db.ForeignKey('taux.id'), nullable=False)
    
class Taux(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    usd_edf=db.Column(db.DECIMAL(precision=10, scale=2, asdecimal=False))
    cdf_usd=db.Column(db.DECIMAL(precision=10, scale=2, asdecimal=False))
    statut=db.Column(db.Boolean, default=True)
    operations=db.relationship('Operation', backref='taux_operation', lazy='dynamic')

class Annee(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    annee=db.Column(db.Integer)
    statut=db.Column(db.Boolean, default=True)
    operations=db.relationship('Operation', backref='operation_annee', lazy='dynamic')
    syntheses=db.relationship('Synthese', backref='synthese_annee', lazy='dynamic')
    soldes=db.relationship('Solde', backref='solde_annee', lazy='dynamic')

class Synthese(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    janvier=db.Column(db.DECIMAL(precision=10, scale=2, asdecimal=False))
    fevrier=db.Column(db.DECIMAL(precision=10, scale=2, asdecimal=False))
    mars=db.Column(db.DECIMAL(precision=10, scale=2, asdecimal=False))
    avril=db.Column(db.DECIMAL(precision=10, scale=2, asdecimal=False))
    mai=db.Column(db.DECIMAL(precision=10, scale=2, asdecimal=False))
    juin=db.Column(db.DECIMAL(precision=10, scale=2, asdecimal=False))
    juillet=db.Column(db.DECIMAL(precision=10, scale=2, asdecimal=False))
    aout=db.Column(db.DECIMAL(precision=10, scale=2, asdecimal=False))
    septembre=db.Column(db.DECIMAL(precision=10, scale=2, asdecimal=False))
    octobre=db.Column(db.DECIMAL(precision=10, scale=2, asdecimal=False))
    novembre=db.Column(db.DECIMAL(precision=10, scale=2, asdecimal=False))
    decmbre=db.Column(db.DECIMAL(precision=10, scale=2, asdecimal=False))
    procure=db.Column(db.DECIMAL(precision=10, scale=2, asdecimal=False))
    xaverien=db.Column(db.DECIMAL(precision=10, scale=2, asdecimal=False))
    eco_diocese=db.Column(db.DECIMAL(precision=10, scale=2, asdecimal=False))
    c_betanie=db.Column(db.DECIMAL(precision=10, scale=2, asdecimal=False))
    affectation=db.Column(db.Boolean, default=True)
    val_janvier=db.Column(db.DECIMAL(precision=10, scale=2, asdecimal=False))
    val_fevrier=db.Column(db.DECIMAL(precision=10, scale=2, asdecimal=False))
    val_mars=db.Column(db.DECIMAL(precision=10, scale=2, asdecimal=False))
    val_avril=db.Column(db.DECIMAL(precision=10, scale=2, asdecimal=False))
    val_mai=db.Column(db.DECIMAL(precision=10, scale=2, asdecimal=False))
    val_juin=db.Column(db.DECIMAL(precision=10, scale=2, asdecimal=False))
    val_juillet=db.Column(db.DECIMAL(precision=10, scale=2, asdecimal=False))
    val_aout=db.Column(db.DECIMAL(precision=10, scale=2, asdecimal=False))
    val_septembre=db.Column(db.DECIMAL(precision=10, scale=2, asdecimal=False))
    val_octobre=db.Column(db.DECIMAL(precision=10, scale=2, asdecimal=False))
    val_novembre=db.Column(db.DECIMAL(precision=10, scale=2, asdecimal=False))
    val_decmbre=db.Column(db.DECIMAL(precision=10, scale=2, asdecimal=False))
    valeur=db.Column(db.DECIMAL(precision=10, scale=2, asdecimal=False))
    communaute_id=db.Column(db.Integer, db.ForeignKey('communaute.id'), nullable=False)
    rubriquecommunaute_id=db.Column(db.Integer, db.ForeignKey('rubriquecommunaute.id'), nullable=False)
    annee_id=db.Column(db.Integer, db.ForeignKey('annee.id'), nullable=False)

class Rubriquecommunaute(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nom=db.Column(db.String(120))
    statut=db.Column(db.Boolean, default=True)
    affectation=db.Column(db.Boolean, default=True)
    rubrique_id=db.Column(db.Integer, db.ForeignKey('rubrique.id'), nullable=False)
    communaute_id=db.Column(db.Integer, db.ForeignKey('communaute.id'), nullable=False)
    operations=db.relationship('Operation', backref='rubriquecommunaute_operation', lazy='dynamic')
    syntheses=db.relationship('Synthese', backref='rubriquecommunaute_synthese', lazy='dynamic')

class Solde(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    recette=db.Column(db.DECIMAL(precision=10, scale=2, asdecimal=False))
    depense=db.Column(db.DECIMAL(precision=10, scale=2, asdecimal=False))
    solde=db.Column(db.DECIMAL(precision=10, scale=2, asdecimal=False))
    communaute_id=db.Column(db.Integer, db.ForeignKey('communaute.id'), nullable=False)
    annee_id=db.Column(db.Integer, db.ForeignKey('annee.id'), nullable=False)

class Source(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    designation=db.Column(db.String(120))
    operations=db.relationship('Operation', backref='source_operation', lazy='dynamic')



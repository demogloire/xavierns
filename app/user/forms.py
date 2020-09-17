from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_wtf.html5 import URLField
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField, IntegerField, DecimalField
from wtforms.validators import DataRequired, Length,Email, EqualTo, ValidationError, url
from wtforms.ext.sqlalchemy.fields import QuerySelectField


from ..models import User, Communaute



def communaute_select():
    return Communaute.query.all()

class AjoutUserForm(FlaskForm):
    nom= StringField('Nom', validators=[DataRequired("Completer le nom"),  Length(min=4, max=200, message="Veuillez respecté les caractères")])
    post_nom = StringField('Post', validators=[DataRequired("Completer le post-nom"),  Length(min=4, max=200, message="Veuillez respecté les caractères")])
    prenom= StringField('Prenom', validators=[DataRequired("Completer le prenom"),  Length(min=4, max=200, message="Veuillez respecté les caractères")])
    tel = StringField('Téléphone', validators=[DataRequired("Completer le numéro de téléphone"),  Length(min=4, max=200, message="Veuillez respecté les caractères")])
    password= PasswordField('Mot de passe', validators=[DataRequired('Veuillez completer votre mot de passe'), EqualTo('confirm','Le mot de passe ne pas le même')])
    confirm=PasswordField('Répeter le mot de passe')
    role= SelectField('Rôle',choices=[('Mère supérieure', 'Mère supérieure'), ('Gestionnaire', 'Gestionnaire') ], default="Choisir le rôle") 
    communaute=QuerySelectField(query_factory=communaute_select, get_label='nom', allow_blank=False, blank_text='Choisir la communaute')   
    submit = SubmitField('Ajouter')
    

class EditerUserForm(FlaskForm):
    nom= StringField('Nom', validators=[DataRequired("Completer le nom"),  Length(min=4, max=200, message="Veuillez respecté les caractères")])
    post_nom = StringField('Post', validators=[DataRequired("Completer le post-nom"),  Length(min=4, max=200, message="Veuillez respecté les caractères")])
    prenom= StringField('Prenom', validators=[DataRequired("Completer le prenom"),  Length(min=4, max=200, message="Veuillez respecté les caractères")])
    tel = StringField('Téléphone', validators=[DataRequired("Completer le numéro de téléphone"),  Length(min=4, max=200, message="Veuillez respecté les caractères")])
    role= SelectField('Rôle',choices=[('Mère supérieure', 'Mère supérieure'), ('Gestionnaire', 'Gestionnaire') ], default="Choisir le rôle") 
    communaute=QuerySelectField(query_factory=communaute_select, get_label='nom', allow_blank=False, blank_text='Choisir la communaute')   
    submit = SubmitField('Editer')

class SuperUserForm(FlaskForm):
    nom= StringField('Nom', validators=[DataRequired("Completer le nom"),  Length(min=4, max=200, message="Veuillez respecté les caractères")])
    post_nom = StringField('Post', validators=[DataRequired("Completer le post-nom"),  Length(min=4, max=200, message="Veuillez respecté les caractères")])
    prenom= StringField('Prenom', validators=[DataRequired("Completer le prenom"),  Length(min=4, max=200, message="Veuillez respecté les caractères")])
    tel = StringField('Téléphone', validators=[DataRequired("Completer le numéro de téléphone"),  Length(min=4, max=200, message="Veuillez respecté les caractères")])
    password= PasswordField('Mot de passe', validators=[DataRequired('Veuillez completer votre mot de passe'), EqualTo('confirm','Le mot de passe ne pas le même')])
    confirm=PasswordField('Répeter le mot de passe')
    role= SelectField('Rôle',choices=[('Mère supérieure', 'Mère supérieure') ], default="Choisir le rôle")  
    submit = SubmitField('Ajouter')


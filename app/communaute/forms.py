from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField, IntegerField, DecimalField
from wtforms.validators import DataRequired, Length,Email, EqualTo, ValidationError


from ..models import Communaute


class AjoutCommunauteForm(FlaskForm):
    nom= StringField('Nom', validators=[DataRequired("Completer le nom"),  Length(min=4, max=200, message="Veuillez respecté les caractères")])
    lieu = StringField('Lieu', validators=[DataRequired("Completer le lieu"),  Length(min=4, max=200, message="Veuillez respecté les caractères")])
    province= StringField('Province', validators=[DataRequired("Completer la province"),  Length(min=4, max=200, message="Veuillez respecté les caractères")])
    pays= StringField('Pays', validators=[DataRequired("Completer le pays"),  Length(min=4, max=200, message="Veuillez respecté les caractères")])
    submit = SubmitField('Ajouter')
    
    #Verification de l'existance
    def validate_nom(self, nom):
        com=Communaute.query.filter_by(nom=nom.data).first()
        if com:
            raise ValidationError("Cette communauté existe déjà")


class EditCommunauteForm(FlaskForm):
    nom= StringField('Nom', validators=[DataRequired("Completer le nom"),  Length(min=4, max=200, message="Veuillez respecté les caractères")])
    lieu = StringField('Lieu', validators=[DataRequired("Completer le lieu"),  Length(min=4, max=200, message="Veuillez respecté les caractères")])
    province= StringField('Province', validators=[DataRequired("Completer la province"),  Length(min=4, max=200, message="Veuillez respecté les caractères")])
    pays= StringField('Pays', validators=[DataRequired("Completer le pays"),  Length(min=4, max=200, message="Veuillez respecté les caractères")])
    submit = SubmitField('Editer')
    

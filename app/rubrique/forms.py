from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField, IntegerField, DecimalField
from wtforms.validators import DataRequired, Length,Email, EqualTo, ValidationError


from ..models import Rubrique


class AjoutRubriqueForm(FlaskForm):
    nom= StringField('Nom', validators=[DataRequired("Completer le nom"),  Length(min=4, max=200, message="Veuillez respecté les caractères")])
    submit = SubmitField('Ajouter')
    
    #Verification de l'existance
    def validate_nom(self, nom):
        rubrique=Rubrique.query.filter_by(nom=nom.data).first()
        if rubrique:
            raise ValidationError("Ce rubrique existe déjà")


class EditRubriqueForm(FlaskForm):
    nom= StringField('Nom', validators=[DataRequired("Completer le nom"),  Length(min=4, max=200, message="Veuillez respecté les caractères")])
    submit = SubmitField('Editer')
    

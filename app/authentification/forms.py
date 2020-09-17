from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_wtf.html5 import URLField
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField, IntegerField, DecimalField
from wtforms.validators import DataRequired, Length,Email, EqualTo, ValidationError, url
from wtforms.ext.sqlalchemy.fields import QuerySelectField



class LoginForm(FlaskForm):
    username= StringField('E-mail', validators=[DataRequired("Completer l'email"), Email('Adresse invalide')])
    password= PasswordField('Mot de passe', validators=[DataRequired()])
    remember = BooleanField('Souvenez-vous')
    submit = SubmitField('Connexion')

    def validate_username(self, username):
        user=User.query.filter_by(username=username.data).first()
        if user is None:
            raise ValidationError("Vous n'est pas reconnu")
        else:
            if user.statut==0:
                raise ValidationError("Vous êtes bloqué")
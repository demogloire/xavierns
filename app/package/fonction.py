import random
import string
import uuid
from ..models import User, Communaute
from .. import db


#Pour générer un mot de passe
def passwordString(length=7):
    #Code pour généer un mot de passe unique
    your_letters='abcdefghijklmnoprstqvwxyz0123456789@'
    return ''.join((random.choice(your_letters) for i in range(length)))

#Génération des utilisateur
def utilisateur(prenom=None,nom=None, user_pass=False):
    
    if prenom is None and nom is None:
        return None
    # requpete de vérification des utilsaiteur
    user_username=User.query.filter_by(statut=True).all()
    print(len(user_username))
    #Username
    user_name=f'{prenom}{nom[0]}{len(user_username)+1}@sr-xaverienne.cd'
    
    if user_pass is True:
        return user_name, passwordString()
    else:
        return user_name
    
#Rôle de l'utilisateur
def role_utilisateur(role_un):
    #Vérification de mère supérieur
    if role_un=='Mère supérieure':
        user_mere=User.query.filter_by(role=role_un).first()
        #Plus de d'une
        if user_mere is None:
            return role_un
        else:
            return None
    else:
        return role_un
    
        
        
        




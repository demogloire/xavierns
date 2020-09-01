from flask import Blueprint

user = Blueprint('user', __name__, url_prefix='/utilisateur')
# never forget 
from . import routes
from app.package.fonction import *
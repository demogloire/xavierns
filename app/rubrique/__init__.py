from flask import Blueprint

rubrique = Blueprint('rubrique', __name__, url_prefix='/rubrique')
# never forget 
from . import routes
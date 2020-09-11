from flask import Blueprint

auth = Blueprint('auth', __name__, url_prefix='/auth')
# never forget 
from . import views
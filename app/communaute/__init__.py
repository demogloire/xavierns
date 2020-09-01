from flask import Blueprint

communaute = Blueprint('communaute', __name__, url_prefix='/communaute')
# never forget 
from . import routes
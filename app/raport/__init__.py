#app/raport/__init__.py
from flask import Blueprint

main = Blueprint('main', __name__, template_folder='templates')

from app.raport import routes
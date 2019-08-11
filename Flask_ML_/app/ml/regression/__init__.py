from flask import Blueprint

regression = Blueprint('regression',__name__)

from . import regression_base
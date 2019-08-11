from flask import Blueprint

data_analyze = Blueprint('data_analyze',__name__)

from . import test_analyze

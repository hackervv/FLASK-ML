from flask_restplus import Api, Resource
from flask import Blueprint

api = Blueprint('api',__name__)

from . import titanic



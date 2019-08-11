from flask import Blueprint

cluster = Blueprint('cluster',__name__)

from . import cluster_base



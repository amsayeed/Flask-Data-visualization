from flask import Blueprint

bp = Blueprint('data_api', __name__)

from app.api_1_0 import routes

from flask import Blueprint

module = Blueprint('delivery', __name__)


@module.route('/', methods=['GET'])
def index():
    return "ok"

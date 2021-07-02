from flask import Blueprint, request

from app.validation import Validation

module = Blueprint('delivery', __name__)
validation = Validation()

@module.route('/', methods=['GET'])
def index():
    return "ok"

@module.route('/couriers', methods=['POST'])
def couriers():
    request_couriers = request.json
    status, bad_id, good_courier = validation.check_courier(request_couriers)
    if not status:
        return {'validation_error': {'couriers': bad_id}}, 400
    return {'status': 'ok'}, 200

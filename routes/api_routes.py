from flask import Blueprint, request, jsonify
from services.service import Service

logic_service = Service()
api_routes = Blueprint('api_routes', __name__)

# 1st endpoint: Echo the input JSON back to the user
@api_routes.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify(logic_service.echo(data)), 200

# 2nd endpoint: Respond with the algorithm name from the input JSON
@api_routes.route('/algorithm', methods=['POST'])
def algorithm():
    data = request.get_json()
    algorithm_name = logic_service.get_algorithm_name(data)
    return jsonify({'algorithm': algorithm_name}), 200

# 3nd endpoint: Test
@api_routes.route('/test', methods=['GET'])
def test():
    data = {'algorithm': 'Test Algorithm'}
    algorithm_name = logic_service.get_algorithm_name(data)
    return jsonify({'algorithm': algorithm_name}), 200


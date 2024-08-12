from flask import Blueprint,jsonify,session,Response
import json
import os
from .auth import *

views = Blueprint('views', __name__)

@views.before_request
def make_session_permanent():
    session.permanent = True

@views.route('/fetch-data', methods=['GET'])
def get_items():
    json_dir = "Mock_Data"
    all_data  = {}
    for filename in os.listdir(json_dir):
        if filename.endswith('.json'):  
            file_path = os.path.join(json_dir, filename)
            with open(file_path, 'r') as json_file:
                session['file_data'] = json.load(json_file)
                all_data[filename] = session['file_data']
                
    return jsonify(all_data)

@views.route('/processed-data', methods=['GET'])
def processed_data():
    
    if 'file_data' in session:
        processed_data = {}
        file_data = session['file_data']
        uppercased_data = convert_to_uppercase(file_data)
        total_price_sum = sum_total_prices(file_data)
        processed_data = {
                    "uppercased_data": uppercased_data,
                    "total_price_sum": total_price_sum
                }
        return jsonify(processed_data)
    else:
        error_data= "Data is not Processed"
        return Response(error_data)
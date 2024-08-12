from flask import Blueprint

auth = Blueprint('auth', __name__)


def convert_to_uppercase(data):
    if isinstance(data, dict):
        return {key: convert_to_uppercase(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [convert_to_uppercase(item) for item in data]
    elif isinstance(data, str):
        return data.upper()
    else:
        return data
    
def sum_total_prices(data):
    total_sum = 0.0
    if isinstance(data, dict):
        for key, value in data.items():
            if key == 'price':
                total_sum += float(value)
            total_sum += sum_total_prices(value)
    elif isinstance(data, list):
        for item in data:
            total_sum += sum_total_prices(item)
    return total_sum

    


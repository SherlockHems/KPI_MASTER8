from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
import gzip
import json
import os

app = Flask(__name__)
CORS(app)


def gzip_response(data):
    return gzip.compress(json.dumps(data).encode('utf-8'))


@app.route('/api/sales_data', methods=['GET'])
def get_sales_data():
    # Load and process your sales data here
    # For now, we'll use dummy data
    data = {
        'salesPerson': ['Alice', 'Bob', 'Charlie', 'David'],
        'cumulativeIncome': [100000, 80000, 120000, 90000]
    }

    if 'gzip' in request.headers.get('Accept-Encoding', ''):
        response = app.response_class(
            response=gzip_response(data),
            status=200,
            mimetype='application/json'
        )
        response.headers['Content-Encoding'] = 'gzip'
        return response
    else:
        return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 8000)))
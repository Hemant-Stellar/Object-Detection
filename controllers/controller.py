from app import app
from flask import request, jsonify, send_file
from models.handler import handler
obj = handler()

@app.route('/upload', methods=['POST'])
def upload(request=request):
    try:
        return obj.upload_handler(request)
    except Exception as e:
        return jsonify({'error': str(e)}), 400
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
    

@app.route('/download', methods=['GET'])
def download():
    try:
        return obj.send_file('uploads/processed.jpg')
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    

@app.route('/mirror',methods=['POST'])
def mirror():
    try:
        return obj.mirror_handler(request)
    except Exception as e:
        return jsonify({'error': str(e)}), 400
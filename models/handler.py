import json
from flask import make_response, jsonify
import os
good = 200
class handler():
    def __init__(self):
        pass
    def upload_handler(self,request):
        try:
            file = request.files['file']
            new_filename = 'processing' 
            split_filename = file.filename.split(".") 
            ext_pos = len(split_filename)-1 
            ext = split_filename[ext_pos] 
            # db_path = f"uploads/{new_filename}.{ext}"
            file.save(f"uploads/{new_filename}.{ext}")
            return {"message":"File uploaded successfully"}
        except Exception as e:
            print(e)
            return make_response({'message':str(e)},400)
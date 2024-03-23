import json
from flask import make_response, jsonify , send_file
import os
from io import BytesIO


class handler():
    def __init__(self):
        pass


    def upload_handler(self,request):

        try:
            if 'file' not in request.files:
                return make_response({'message':'No file part'},400)
            

            file = request.files['file']
            new_filename = 'processing' 
            split_filename = file.filename.split(".") 
            ext_pos = len(split_filename)-1 
            ext = split_filename[ext_pos] 
            file.save(f"uploads/{new_filename}.{ext}")
            return {"message":"File uploaded successfully"}
        
        except Exception as e:
            print(e)
            return make_response({'error':str(e)},400)
    

    def send_file(self,filename):
        try:
            return send_file(filename, as_attachment=True)
        
        except Exception as e:
            return make_response({'error':str(e)},400)
        
    
    # send back same file as response without saving
    def mirror_handler(self,request):
        if 'file' not in request.files:
            return 'No file part'

        file = request.files['file']

        if file.filename == '':
            return 'No selected file'

        if file:
        # Read the image data from the file object
            image_data = file.read()

            # Set appropriate content type for the response
            content_type = file.content_type

            # Create an in-memory file-like object
            file_like_object = BytesIO()
            file_like_object.write(image_data)
            file_like_object.seek(0)

            # Return the file-like object as response
            return send_file(
                file_like_object,
                mimetype=content_type,
                as_attachment=True,
                download_name=file.filename
            )
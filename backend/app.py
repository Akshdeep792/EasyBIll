from flask import Flask, request,jsonify,send_file
import datetime 
from PIL import Image
import base64
import io
x = datetime.datetime.now() 
from end_to_end_data_extraction import extractcsv
  
# Initializing flask app 
app = Flask(__name__) 
  
  
# Route for seeing a data 
@app.route('/uploadFile', methods=['GET', 'POST']) 
def get_time(): 
  
    # Returning an api for showing in  reactjs 
    directory = './uploadedImage'
    image_file = request.files['file']
    filename = image_file.filename
    image_file.save(filename)

    # Calling model to convert png into structured data
    extractcsv(f"./{filename}", 1)
    
    return send_file('./final.csv',
        as_attachment=True)
  
      
# Running app 
if __name__ == '__main__': 
    app.run(port=8000, debug=True)
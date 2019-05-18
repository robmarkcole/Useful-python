from flask import Flask, render_template, request
import pandas as pd
import cv2
import numpy as np
import base64
from PIL import Image
from io import BytesIO
import re

app = Flask(__name__)

@app.route('/predict_by_bytes', methods=['GET', 'POST'])
def add_face():
    if request.method == 'POST':
        #  read encoded image
        image_data = re.sub('^data:image/.+;base64,', '', request.form['image_bytes'])
        image = Image.open(BytesIO(base64.b64decode(image_data)))
        image.save('img_saved.png')
        
        np_im = np.array(image)
        return f"image saved with shape {np_im.shape}"

if __name__ == '__main__':
    app.run(debug=True, port=5000)

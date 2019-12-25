from flask import Blueprint, render_template, request
import os
import numpy as np
import tensorflow as tf
import re
import random
import string

dir_path = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = 'uploads'
STATIC_FOLDER = 'static'

# Load model
model = tf.keras.models.load_model(STATIC_FOLDER + '/' + 'model_vgg.h5')

IMAGE_SIZE = 200

# Preprocess an image
def preprocess_image(image):
    image = tf.image.decode_jpeg(image, channels=3)
    image = tf.image.resize(image, [IMAGE_SIZE, IMAGE_SIZE])
    image /= 255.0  # normalize to [0,1] range

    return image

# Read the image from path and preprocess
def load_and_preprocess_image(path):
    image = tf.io.read_file(path)
    return preprocess_image(image)

# Predict & classify image
def prediction(model, image_path):

    preprocessed_imgage = load_and_preprocess_image(image_path)
    preprocessed_imgage = tf.reshape(preprocessed_imgage, (1,IMAGE_SIZE ,IMAGE_SIZE ,3))

    prob = model.predict(preprocessed_imgage)
    label = "Dog" if prob >= 0.5 else "Cat"
    classified_prob = prob if prob >= 0.5 else 1 - prob
    
    return label, classified_prob

# create a random string for file name
def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

classify = Blueprint('classify', __name__)

@classify.route('/classify', methods=['POST'])
def upload_file():

    file = request.files["image"]
    file.filename = randomString() + '.jpg'
    upload_image_path = os.path.join(UPLOAD_FOLDER, file.filename)
    print(upload_image_path)
    file.save(upload_image_path)

    label, prob = prediction(model, upload_image_path)

    prob = round((prob[0][0] * 100), 2)

    return render_template('classify.html', image_file_name = file.filename, label = label, prob = prob, path = upload_image_path)

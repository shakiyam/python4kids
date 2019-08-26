import glob
import os

import cv2

from jinja2 import Environment, FileSystemLoader, select_autoescape

import numpy


def get_gray_resized_image(image_path):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_resized_image = cv2.resize(gray_image, (500, 500))
    return gray_resized_image


def get_label(path):
    return int(path.split(os.sep)[2].split('_')[0])


def get_label_name(path):
    return path.split(os.sep)[2].split('_')[1]


label_and_names = {
    get_label(path): get_label_name(path) for path in glob.glob('./src/*')
}

train_images = []
train_labels = []
for image_path in glob.glob('./train/*/*.jpg'):
    train_images.append(get_gray_resized_image(image_path))
    train_labels.append(get_label(image_path))
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(train_images, numpy.array(train_labels))

test_results = []
for image_path in glob.glob('./test/*/*.jpg'):
    image_name = os.path.basename(image_path)
    gray_resized_image = get_gray_resized_image(image_path)
    predicted_label, confidence = recognizer.predict(gray_resized_image)
    test_results.append(
        (image_path,
         label_and_names[predicted_label],
         confidence,
         get_label_name(image_path))
    )

env = Environment(
    loader=FileSystemLoader('./templates'),
    autoescape=select_autoescape()
)
template = env.get_template('02.html')
template.stream(test_results=test_results).dump('output.html')

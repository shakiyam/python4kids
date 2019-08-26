import glob
import os

import cv2

import numpy


def get_gray_resized_image(image_path):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_resized_image = cv2.resize(gray_image, (500, 500))
    return gray_resized_image


def get_label(path):
    return int(path.split(os.sep)[2].split('_')[0])


train_images = []
train_labels = []
for image_path in glob.glob('./train/*/*.jpg'):
    train_images.append(get_gray_resized_image(image_path))
    train_labels.append(get_label(image_path))
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(train_images, numpy.array(train_labels))

for image_path in glob.glob('./test/*/*.jpg'):
    image_name = os.path.basename(image_path)
    gray_resized_image = get_gray_resized_image(image_path)
    predicted_label, confidence = recognizer.predict(gray_resized_image)
    image_label = get_label(image_path)
    print(f'Image: {image_name}', end='\t')
    print(f'Predicted: {predicted_label}', end='\t')
    print(f'Confidence: {confidence:3.1f}', end='\t')
    print(f'Anser: {image_label}')

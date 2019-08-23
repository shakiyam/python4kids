import glob
import os

import cv2

cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml'
cascade = cv2.CascadeClassifier(cascade_path)
WHITE = (255, 255, 255)

for image_path in glob.glob('./src/*.jpg'):
    image_name = os.path.basename(image_path)
    print(f'image_path: {image_path} image_name: {image_name}')

    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_list = cascade.detectMultiScale(
        gray_image, 1.1, 5, minSize=(100, 100))

    if len(face_list) > 0:
        print(face_list)
        for x, y, w, h in face_list:
            face_image = image[y: y + h, x: x + w]
            face_path = f'./face/{ image_name[:-4] }_{ x }-{ y }.jpg'
            cv2.imwrite(face_path, face_image)
        for x, y, w, h in face_list:
            cv2.rectangle(image, (x, y), (x + w, y + h), WHITE, 2)
    cv2.imwrite('./face_rectangle/' + image_name, image)

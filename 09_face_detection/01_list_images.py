import glob
import os

for image_path in glob.glob('./src/*.jpg'):
    image_name = os.path.basename(image_path)
    print(f'image_path: {image_path} image_name: {image_name}')

import glob
import random
import shutil

for image_path in glob.glob('./src/*/*.jpg'):
    if random.random() <= 0.8:
        shutil.copy(image_path, image_path.replace('./src/', './train/', 1))
    else:
        shutil.copy(image_path, image_path.replace('./src/', './test/', 1))

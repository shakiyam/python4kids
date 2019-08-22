import glob
import os

SRC_PATH = 'src'

for image_file in glob.glob(os.path.join(SRC_PATH, '*.jpg')):
    print(image_file)

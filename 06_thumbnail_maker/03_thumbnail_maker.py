import glob
import os
import shutil

import cv2

SRC_PATH = 'src'
DEST_PATH = 'dest'
RENAME_FORMAT = 'image'
THUMBNAIL_SIZE = 100

for i, image_file in enumerate(glob.glob(os.path.join(SRC_PATH, '*.jpg')), 1):
    renamed_file = f'{RENAME_FORMAT}_{i:03}.jpg'
    print(f'{os.path.basename(image_file)} -> {renamed_file}')
    shutil.copy(image_file, os.path.join(DEST_PATH, renamed_file))

    image = cv2.imread(image_file, cv2.IMREAD_COLOR)
    height, width = image.shape[:2]
    thumbnail_file = f'{RENAME_FORMAT}_{i:03}_thumb.jpg'
    scale = min(THUMBNAIL_SIZE / height, THUMBNAIL_SIZE / width)
    if scale < 1:
        thumbnail_image = cv2.resize(image, dsize=None, fx=scale, fy=scale)
        cv2.imwrite(
            os.path.join(DEST_PATH, thumbnail_file),
            thumbnail_image)
    else:
        shutil.copy(image_file, os.path.join(DEST_PATH, thumbnail_file))

import glob
import os
import shutil

import cv2

SRC_PATH = 'Desktop/line'
DEST_PATH = 'Desktop/line2'
RENAME_FORMAT = '190811'
THUMBNAIL_T_SIZE = (67, 89)
THUMBNAIL_Y_SIZE = (97, 72)
IMAGE_PATH = 'album/2019'
ALTERNATIVE_TEXT = '190721_夏キャンプ準備'

i = 1
for image_file in glob.glob(os.path.join(SRC_PATH, '*.jpg')):
    image = cv2.imread(image_file, cv2.IMREAD_COLOR)
    height, width = image.shape[:2]
    if height >= width:
        renamed_file = f'{RENAME_FORMAT}t({i}).jpg'
        thumbnail_file = f'{RENAME_FORMAT}t({i})tn.jpg'
        thumbnail = cv2.resize(image, THUMBNAIL_T_SIZE)
    else:
        renamed_file = f'{RENAME_FORMAT}y({i}).jpg'
        thumbnail_file = f'{RENAME_FORMAT}y({i})tn.jpg'
        thumbnail_image = cv2.resize(image, THUMBNAIL_Y_SIZE)
    print(f'<a href="{IMAGE_PATH}/{renamed_file}"><img src="{IMAGE_PATH}/{thumbnail_file}" class="photo-small-y" alt="{ALTERNATIVE_TEXT}"></a>')
    shutil.copy(image_file, os.path.join(DEST_PATH, renamed_file))
    cv2.imwrite(
        os.path.join(DEST_PATH, thumbnail_file),
        os.path.join(DEST_PATH, thumbnail_image))
    i = i + 1

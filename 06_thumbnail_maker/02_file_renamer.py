import glob
import os
import shutil

SRC_PATH = 'src'
DEST_PATH = 'dest'
RENAME_FORMAT = 'image'

for i, image_file in enumerate(glob.glob(os.path.join(SRC_PATH, '*.jpg')), 1):
    renamed_file = f'{RENAME_FORMAT}_{i:03}.jpg'
    print(f'{os.path.basename(image_file)} -> {renamed_file}')
    shutil.copy(image_file, os.path.join(DEST_PATH, renamed_file))

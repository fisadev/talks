import sys
from pathlib import Path

import numpy as np
from PIL import Image


def get_image_data(image_path, image_size):
    """
    Extract pixels from one particular image.
    """
    image = Image.open(str(image_path))
    image = image.crop((80, 0, 560, 480))  # make it square, discarding laterals
    image = image.resize((image_size, image_size), Image.ANTIALIAS)
    return np.array(image.getdata()).reshape(image_size, image_size, 3)


def load_images(images_path, image_size, excludes=None):
    """
    Find all image files in a directory, and extract their pixels as a dataframe.
    """
    sorted_images = list(sorted(images_path.glob('*.jpg')))

    images = []
    for image_path in sorted_images:
        if excludes is None or all(exclude not in image_path.name for exclude in excludes):
            images.append(get_image_data(image_path, image_size))

    return np.array(images)


if __name__ == '__main__':
    if '-h' in sys.argv or len(sys.argv) < 4:
       print('Usage:')
       print('python3 generate_set.py PATH_TO_IMAGES_DIR IMAGE_SIZE PATH_TO_RESULT [EXCLUDE EXCLUDE EXCLUDE...]')
       print('Example:')
       print('python3 generate_set.py /home/fisa/bird_images/ 32 ./images.pkl crow eagle')
       print('(EXCLUDEs are texts that the files must *not* have in their names. Just a simple way of excluding certain files from the set.)')
       sys.exit()

    images_path = Path(sys.argv[1])
    image_size = int(sys.argv[2])
    pkl_path = Path(sys.argv[3])
    if len(sys.argv) > 4:
        excludes = sys.argv[4:]
    else:
        excludes = None

    imgs = load_images(images_path, image_size, excludes)
    print(imgs.shape)
    np.save(open(pkl_path, 'wb'), imgs)

import random
from scipy import ndarray
import skimage as sk
from skimage import transform
import skimage.io
from skimage import util
import os
from PIL import Image

# data directory containing subdirectories
data_path = 'slim/train/'
target_data_path = 'skimage_augmented/'
for class_dir in os.listdir(data_path):
    class_path = os.path.join(data_path, class_dir)
    for image_name in os.listdir(class_path):
        image_path = os.path.join(class_path, image_name)
        # read image as an two dimensional array of pixels
        image = sk.io.imread(image_path)
        noised = sk.util.random_noise(image)
        inverted = util.invert(image)
        image_name = image_name[:image_name.index('.')] + '.png'
        # write image to the disk
        noised_path = os.path.join(target_data_path, class_dir, 'noised_' + image_name)
        sk.io.imsave(noised_path, noised)
        inverted_path = os.path.join(target_data_path, class_dir, 'inverted_' + image_name)
        sk.io.imsave(inverted_path, inverted)
        print(image_name)


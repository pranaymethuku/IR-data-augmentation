# NOTE: Cannot run this file any time, need some manual setup before every run (in detail below)
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.4,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')

# dimensions of our images.
img_width, img_height = 500, 500
train_data_dir = 'slim/train'
# directory for storing augmented class data
save_dir = 'augmented/English_Cocker_Spaniel'
batch_size = 32

# making this work is a bit inconvenient
# it requires the directory to have subdirectories for each class,
#   but it combines all images into one target directory
# so hack is to have only one subdirectory of one class at a time, and storing
#   all images for that one class in the target directory
# do this for every class
train_generator = datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode=None,
    save_to_dir=save_dir,
    save_prefix='augmented',
    save_format='jpg',
    follow_links=True,
    interpolation='lanczos')

i = 0
for batch in train_generator:
    i += 1
    if i > 5:
        break  # otherwise the generator would loop infinitely

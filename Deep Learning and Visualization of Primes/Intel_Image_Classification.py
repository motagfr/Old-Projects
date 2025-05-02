# !kaggle datasets download -d titanic
#!unzip titanic.zip

# %% imports
import os
import shutil

import cv2
import matplotlib.image as mpimage
import matplotlib.pyplot as plt
import numpy as np
import PIL.Image
import tensorflow as tf

keras = tf.keras
import random

from keras import Sequential  # the same as keras.models.Sequential()
from keras.layers import Normalization, Rescaling

# from tf.keras.preprocessing.image import ImageDataGenerator #This has been deprecated, instead use below.
from keras.utils import image_dataset_from_directory

# %% The first cell
# Set the path to your dataset

data_dir = "C:\\Users\\M\\Desktop\\Deep Learning\\Intel_Image_Dataset"
fnames = os.listdir(data_dir)
fnames
output_dir = os.path.join(data_dir, "Train_Validation")
os.makedirs(output_dir, exist_ok=True)
output_validation_dir = os.path.join(output_dir, "validation")
os.makedirs(output_validation_dir, exist_ok=True)
output_train_dir = os.path.join(output_dir, "train")
os.makedirs(output_train_dir, exist_ok=True)

train_root_dir = os.path.join(data_dir, fnames[2])
train_categ = os.listdir(train_root_dir)

# region This is a good region

list_files = []
for i in range(0, 6):
    folder_name = os.listdir(train_root_dir)[i]
    folder_dir = os.path.join(train_root_dir, folder_name)
    list_files += [os.listdir(folder_dir)]

print(list_files)

len(list_files)
# endregion


# %% The second cell (should be run only once)
#! Deprecated method, do not use
# ? search how to do it
# todo: I must change this
# // this is the function
# * Important to notice the difference
# @ MyParam is the parameter of the function


# for i in range(0, len(list_files)):
#     for j in range(0, int(0.8 * len(list_files[i]))):
#         src = os.path.join(
#             train_root_dir, os.listdir(train_root_dir)[i], list_files[i][j]
#         )
#         des = os.path.join(
#             output_train_dir, os.listdir(train_root_dir)[i], list_files[i][j]
#         )
#         des_dir = os.path.join(output_train_dir, os.listdir(train_root_dir)[i])
#         os.makedirs(des_dir, exist_ok=True)
#         shutil.copyfile(src, des)


# for i in range(0, len(list_files)):
#     for j in range(int(0.8 * len(list_files[i])), len(list_files[i])):
#         src = os.path.join(
#             train_root_dir, os.listdir(train_root_dir)[i], list_files[i][j]
#         )
#         des = os.path.join(
#             output_validation_dir, os.listdir(train_root_dir)[i], list_files[i][j]
#         )
#         des_dir = os.path.join(output_validation_dir, os.listdir(train_root_dir)[i])
#         os.makedirs(des_dir, exist_ok=True)
#         shutil.copyfile(src, des)


# %% Show some images
np.random.randint(5, 6)
fig, ax = plt.subplots(6, 3, figsize=(8, 16))
for i in random.sample(range(0, 6), 6):
    k = 0
    for j in random.sample(range(1, 100), 3):
        image_path = os.path.join(train_root_dir, train_categ[i], list_files[i][j])
        test_image = mpimage.imread(image_path)
        ax[i, k].imshow(test_image)
        ax[i, k].set_xticks([])
        ax[i, k].set_yticks([])
        k += 1
plt.tight_layout()
plt.show()


# test_image = cv2.imread(image_path)
# test_image=cv2.cvtColor(test_image, cv2.COLOR_BGR2RGB)
# plt.imshow(test_image)
# plt.show()

# test_image2 = cv2.imread(image_path, cv2.IMREAD_COLOR)
# plt.imshow(test_image2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# import PIL
# image_3=PIL.Image.open(image_path)
# image_3

# %% ImageDataGenerator for Train-Test-Validation
# data=ImageDataGenerator() #This is deprecated
image_path = os.path.join(train_root_dir, train_categ[2], list_files[2][2])
test_image = mpimage.imread(image_path)
print("Data shape is:", test_image.shape)

train_ds = tf.keras.utils.image_dataset_from_directory(
    directory=output_train_dir,
    labels="inferred",
    label_mode="categorical",
    batch_size=32,
    image_size=(150, 150),
    shuffle=True,
    seed=123,
)
# I didn't need to create the train and val sets there is an argument for this: subsets = "training" or "validation".It is in the tf.keras.utils.image_dataset_from_directory()


val_ds = tf.keras.utils.image_dataset_from_directory(
    directory=output_validation_dir,
    labels="inferred",
    label_mode="categorical",
    batch_size=32,
    image_size=(150, 150),
    shuffle=False,
    seed=123,
)

output_test_dir = os.path.join(data_dir, "seg_test")
test_ds = tf.keras.utils.image_dataset_from_directory(
    directory=output_test_dir,
    labels="inferred",
    label_mode="categorical",
    batch_size=32,
    image_size=(150, 150),
    shuffle=False,
)


# Create preprocessing layers
# And incorporate additional normalization into the code
# Calculate mean and standard deviation from training data to apply to the test dataset.

train_ds_iter = iter(train_ds)
first_batch = next(train_ds_iter)
image_batch, label_batch = first_batch
mean = tf.reduce_mean(image_batch, axis=(0, 1, 2))
std = tf.math.reduce_std(image_batch, axis=(0, 1, 2))

data_augmentation = Sequential(
    [
        keras.layers.Rescaling(1.0 / 255),
        keras.layers.RandomFlip("horizontal_and_vertical"),
        keras.layers.RandomRotation(0.2),
        keras.layers.RandomZoom(0.2),
    ]
)

# Create normalization layer
# normalization = Normalization(mean=mean, variance=std**2)


# @tf.function
def apply_augmentation_training(image, label):
    image = data_augmentation(image)
    normalization = Normalization(mean=mean, variance=std**2)
    image = normalization(image, training=True)
    return image, label


train_ds = train_ds.map(apply_augmentation_training)


# @tf.function
def apply_augmentation_valid(image, label):
    normalization = Normalization(mean=mean, variance=std**2)
    image = normalization(image, training=False)
    return image, label


val_ds = val_ds.map(apply_augmentation_valid)


# Rescale the test dataset
rescale = keras.layers.Rescaling(1.0 / 255)


# @tf.function
def rescale_and_normalize_image(image, label):
    image = rescale(image)
    normalization = Normalization(mean=mean, variance=std**2)
    image = normalization(image, training=False)
    return image, label


test_ds = test_ds.map(rescale_and_normalize_image)

print(f"validation radio={2810/11224}, test ratio=3000/11224")

# Get a batch of images and labels
images, labels = next(iter(train_ds))

# # Visualize a few images
# # plot_images(images, labels)
# plt.imshow(images[2][0])

# Calculate and print class distribution
class_counts = np.sum(labels, axis=0)
print("class distribution:", class_counts)
print("Shape of resulting images:", images[0].shape)

# %% Summary of data Agmentation
data_augmentation.summary()

# %% Model Architecture
from keras import layers, models

model = models.Sequential(
    [
        layers.Input(shape=(150, 150, 3)),
        layers.Conv2D(64, (3, 3), activation="relu"),
        layers.BatchNormalization(),
        layers.MaxPool2D((2, 2)),
        layers.Conv2D(128, (3, 3), activation="relu"),
        layers.BatchNormalization(),
        layers.MaxPool2D(2, 2),
        layers.Conv2D(256, (3, 3), activation="relu"),
        layers.BatchNormalization(),
        layers.MaxPool2D(2, 2),
        layers.Flatten(),
        layers.Dense(256, activation="relu"),
        layers.Dense(128, activation="relu"),
        layers.Dense(6, activation="softmax"),
    ]
)



# %% Model Summary
model.summary()

# %% Compile and Fit-train

model.compile(
    optimizer=keras.optimizers.Adam(),
    loss=keras.losses.CategoricalCrossentropy(),
    metrics=[keras.metrics.Accuracy()],
)
my_callbacks = [
    keras.callbacks.EarlyStopping(patience=2),
    keras.callbacks.ModelCheckpoint(filepath="model.{epoch:02d}-{val_loss:.2f}.h5"),
    keras.callbacks.TensorBoard(log_dir="./logs"),
]
model.fit(
    train_ds, epochs=10, batch_size=32, validation_data=val_ds, callbacks=my_callbacks
)


# %%
"""
Common Colormap Categories
Sequential: Colors progress from low to high values (e.g., viridis, plasma, inferno).
Diverging: Colors diverge from a central value (e.g., coolwarm, RdBu, BrBG).
Qualitative: Colors are distinct and unrelated (e.g., Pastel1, Set1, tab10).
Experimenting with Colormaps
Python
import matplotlib.pyplot as plt
import numpy as np

# Sample data (replace with your data)
data = np.random.randn(10, 10)

# List of colormaps to try
colormaps = ['viridis', 'plasma', 'inferno', 'coolwarm', 'RdBu', 'BrBG', 'Pastel1', 'Set1', 'tab10']

# Create subplots for comparison
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(12, 12))

# Iterate through colormaps and plot
for i, cmap in enumerate(colormaps):
    ax = axes[i // 3, i % 3]
    im = ax.imshow(data, cmap=cmap)
    ax.set_title(cmap)
    fig.colorbar(im, ax=ax)

plt.tight_layout()
plt.show()
"""
# for category in train_categ:
#     cat_sdir = os.path.join(train_root_dir, category)
#     cat_desdir = os.path.join(output_train_dir, category)
#     os.makedirs(cat_desdir, exist_ok=True)
#     Samples = [f"{i}.jpg" for i in range(0, int(0.8 * len(os.listdir(cat_sdir))))]
#     for file in Samples:
#         src = os.path.join(cat_sdir, file)
#         des = os.path.join(cat_desdir, file)
#         if os.path.exists(src):
#             print(src + "to" + des)
#             shutil.copyfile(src, des)
# print("----------------------")
# for category in train_categ:
#     cat_sdir = os.path.join(train_root_dir, category)
#     cat_desdir = os.path.join(output_validation_dir, category)
#     os.makedirs(cat_desdir, exist_ok=True)
#     Samples = [
#         f"{i}.jpg"
#         for i in range(int(0.8 * len(os.listdir(cat_sdir))), len(os.listdir(cat_sdir)))
#     ]
#     for file in Samples:
#         src = os.path.join(cat_sdir, file)
#         des = os.path.join(cat_desdir, file)
#         if os.path.exists(src):
#             print(src + "to" + des)
#             shutil.copyfile(src, des)

'''
# #Create train Test and Validation folders first

# def create_directories(data_dir):
#   """
#   Creates the necessary directories for training, validation, and test sets.

#   Args:
#     data_dir: The root directory of the dataset.
#   """

#   subdirs = ['train', 'validation', 'test']
#   for subdir in subdirs:
#     path = os.path.join(data_dir, subdir)
#     if not os.path.exists(path):
#       os.makedirs(path)
# create_directories(data_dir)
'''
# Image size
img_height, img_width = 150, 150

# Create an ImageDataGenerator for data augmentation (optional)
train_datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True,
    fill_mode="nearest",
)

# Create training and validation generators
train_generator = train_datagen.flow_from_directory(
    os.path.join(output_dir, "train"),
    target_size=(img_height, img_width),
    batch_size=32,
    class_mode="categorical",
)
validation_generator = train_datagen.flow_from_directory(
    os.path.join(output_dir, "validation"),
    target_size=(img_height, img_width),
    batch_size=32,
    class_mode="categorical",
)


for x, y in train_generator:
    # x is a batch of images (numpy array)
    # y is a batch of labels (one-hot encoded)
    print(x.shape, y.shape)
    break

import os
import random
import shutil


def split_data(source_dir, output_dir, split_ratio=0.8):
    """
    Splits data into training and validation sets.

    Args:
      source_dir: The directory containing the original data.
      output_dir: The directory where the split folders will be created.
      split_ratio: The proportion of data for the training set.
    """
    input_folder = os.path.join(
        data_dir, "seg_train"
    )  # Replace with your input directory
    output_folder = os.path.join(data_dir, "seg_train") + "output"
    # Create output directories
    train_dir = os.path.join(output_dir, "train")
    val_dir = os.path.join(output_dir, "val")
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(val_dir, exist_ok=True)

    # Get a list of all files in the source directory
    files = os.listdir(os.path.join(data_dir, "seg_train"))
    random.shuffle(files)

    # Split files into train and validation sets
    split_index = int(len(files) * split_ratio)
    train_files = files[:split_index]
    val_files = files[split_index:]

    # Copy files to respective directories
    for file in train_files:
        source_file = os.path.join(source_dir, file)
        dest_file = os.path.join(train_dir, file)
        shutil.copy(source_file, dest_file)

    for file in val_files:
        source_file = os.path.join(source_dir, file)
        dest_file = os.path.join(val_dir, file)
        shutil.copy(source_file, dest_file)


# Example usage:
source_dir = "path/to/your/images"
output_dir = "output"
split_data(source_dir, output_dir, split_ratio=0.8)


"""
import splitfolders
# Split with a ratio.
# To only split into training and validation set, set a tuple to `ratio`, i.e, `(.8, .2)`.
splitfolders.ratio("input_folder", output="output",
    seed=1337, ratio=(.8, .1, .1), group_prefix=None, move=False) # default values

# Split val/test with a fixed number of items, e.g. `(100, 100)`, for each set.
# To only split into training and validation set, use a single number to `fixed`, i.e., `10`.
# Set 3 values, e.g. `(300, 100, 100)`, to limit the number of training values.
splitfolders.fixed("input_folder", output="output",
    seed=1337, fixed=(100, 100), oversample=False, group_prefix=None, move=False) # default values"""


#THIS IS A FUNCTIONAL MODEL

'''
inputs = keras.Input(shape=(32, 32, 3), name="img")
x = layers.Conv2D(32, 3, activation="relu")(inputs)
x = layers.Conv2D(64, 3, activation="relu")(x)
block_1_output = layers.MaxPooling2D(3)(x)

x = layers.Conv2D(64, 3, activation="relu", padding="same")(block_1_output)
x = layers.Conv2D(64, 3, activation="relu", padding="same")(x)
block_2_output = layers.add([x, block_1_output])

x = layers.Conv2D(64, 3, activation="relu", padding="same")(block_2_output)
x = layers.Conv2D(64, 3, activation="relu", padding="same")(x)
block_3_output = layers.add([x, block_2_output])

x = layers.Conv2D(64, 3, activation="relu")(block_3_output)
x = layers.GlobalAveragePooling2D()(x)
x = layers.Dense(256, activation="relu")(x)
x = layers.Dropout(0.5)(x)
outputs = layers.Dense(10)(x)

model = keras.Model(inputs, outputs, name="toy_resnet")
model.summary()
'''
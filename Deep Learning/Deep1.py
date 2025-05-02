import matplotlib.pyplot as plt
import numpy as np
import PIL


###############################
# pip install tensorflow
# pip show tensorflow

# import tensorflow

# model=tensorflow
#####################################

a = plt.imread("./stop1.jpg")
a
type(a)
a.shape
ch1, ch2, ch3 = a.shape  # Tuple unpacking
ch1
a.ndim
plt.imshow(a)
a[100, 100]
a[100, 100] = (100, 200, 100)  # Error
a = np.array(a)
a[200:400, 400:600] = (100, 200, 100)
plt.imshow(a)
a[1:5, 1:3]
a[:, :, 1] = 0  # this makes channel 1 which is green 0
a[:, :, 2] = 0  # this makes channel 2 which is blue 0
plt.imshow(a)

a = plt.imread("./stop1.jpg")
gray_im=a[:,:,0]//3+a[:,:,1]//3+a[:,:,2]//3
plt.imshow(gray_im)
plt.imshow(gray_im,cmap='gray')
gray_im.shape

# pip install opencv-python

###############################
import numpy as np
import matplotlib.pyplot as plt
# import cv2 #this is openCV
import tensorflow as tf
keras = tf.keras

fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels),\
    (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
train_images.shape
test_images.shape
np.max(train_images)
np.min(train_images)
train_labels
len(train_labels)
np. unique(train_labels,return_counts=True)
train_images[0]
train_images[0][7]
train_images[0].shape

plt.imshow(train_images[0],cmap='gray')

plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
plt.show()

plt.imshow(train_images[3])

train_images = train_images / 255.0
test_images = test_images / 255.0

plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
plt.show()

from keras import Sequential
from keras.layers import Dense,Dropout,Flatten
model=Sequential([
    Flatten(input_shape=(28,28)),
    Dense(70,activation='relu'),
    Dense(50,activation='relu'),
    Dropout(0.5),
    Dense(10)
])
model.summary()
model.compile(optimizer='adam',
              metrics=['accuracy'],
              loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True))

history=model.fit(train_images,train_labels,epochs=50,
          batch_size=50,validation_split=.2)

history.history.keys()

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.legend(['loss','val_loss'])


test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
print('\nTest accuracy:', test_acc)

probability_model = tf.keras.Sequential([model, 
                                         tf.keras.layers.Softmax()])

predictions = probability_model.predict(test_images)

predictions[0]

np.argmax(predictions[0])

test_labels[0]

# Define functions to graph the full set of 10 class predictions.


def plot_image(i, predictions_array, true_label, img):
  true_label, img = true_label[i], img[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])

  plt.imshow(img, cmap=plt.cm.binary)

  predicted_label = np.argmax(predictions_array)
  if predicted_label == true_label:
    color = 'blue'
  else:
    color = 'red'

  plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                100*np.max(predictions_array),
                                class_names[true_label]),
                                color=color)

def plot_value_array(i, predictions_array, true_label):
  true_label = true_label[i]
  plt.grid(False)
  plt.xticks(range(10))
  plt.yticks([])
  thisplot = plt.bar(range(10), predictions_array, color="#777777")
  plt.ylim([0, 1])
  predicted_label = np.argmax(predictions_array)

  thisplot[predicted_label].set_color('red')
  thisplot[true_label].set_color('blue')

i = 0
plt.figure(figsize=(6,3))
plt.subplot(1,2,1)
plot_image(i, predictions[i], test_labels, test_images)
plt.subplot(1,2,2)
plot_value_array(i, predictions[i],  test_labels)
plt.show()

i = 12
plt.figure(figsize=(6,3))
plt.subplot(1,2,1)
plot_image(i, predictions[i], test_labels, test_images)
plt.subplot(1,2,2)
plot_value_array(i, predictions[i],  test_labels)
plt.show()

# Plot the first X test images, their predicted labels, and the true labels.
# Color correct predictions in blue and incorrect predictions in red.
num_rows = 5
num_cols = 3
num_images = num_rows*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
for i in range(num_images):
  plt.subplot(num_rows, 2*num_cols, 2*i+1)
  plot_image(i, predictions[i], test_labels, test_images)
  plt.subplot(num_rows, 2*num_cols, 2*i+2)
  plot_value_array(i, predictions[i], test_labels)
plt.tight_layout()
plt.show()

# Finally, use the trained model to make a prediction about a single image.

# Grab an image from the test dataset.
img = test_images[1]
print(img.shape)
# Add the image to a batch where it's the only member.
img = (np.expand_dims(img,0))
print(img.shape)
predictions_single = probability_model.predict(img)
print(predictions_single)

plot_value_array(1, predictions_single[0], test_labels)
_ = plt.xticks(range(10), class_names, rotation=45)
plt.show()

plt.figure(figsize=(5,5))
plt.subplot(2,3)
plt.show()

predict=model.predict(test_images) #It gives a vecto only hard to interpret.

##########################


#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)

plt.show()
###################################

import matplotlib.pyplot as plt
import numpy as np

x=np.arange(-2*np.pi,2*np.pi, .1)

fig,axes=plt.subplots(2,2,constrained_layout=True)
fig.suptitle('Comparison',fontsize=25)
fig.dpi=1000
fig.set_facecolor('gray')
axes[0,0].plot(x,np.sin(x), color='black')
axes[0,0].set_xlabel('X')
axes[0,0].set_ylabel('Y')
axes[0,0].set_title('Sin(X)')
axes[0,0].set_xticks(np.arange(-2*np.pi,2*np.pi,2))
axes[0,0].grid()
axes[0,0].set_facecolor('blue')

axes[0,1].plot(x,np.cos(x), color='yellow')
axes[0,1].set_xlabel('X')
axes[0,1].set_ylabel('Y')
axes[0,1].set_title('Cos(X)')
axes[0,1].set_xticks(np.arange(-2*np.pi,2*np.pi,2))
axes[0,1].grid()
axes[0,1].set_facecolor('red')

axes[1,1].plot(x,np.log(x), color='blue')
axes[1,1].set_xlabel('X')
axes[1,1].set_ylabel('Y')
axes[1,1].set_title('Log(X)')
# axes[1,1].set_xticks(np.arange(-2*np.pi,2*np.pi,2))
axes[1,1].grid()
axes[1,1].set_facecolor('green')

axes[1,0].plot(x,np.exp(-x**2), color='yellow')
axes[1,0].set_xlabel('X')
axes[1,0].set_ylabel('Y')
axes[1,0].set_title('Exp(X)')
# axes[1,1].set_xticks(np.arange(-2*np.pi,2*np.pi,2))
axes[1,0].grid()
axes[1,0].set_facecolor('purple')

plt.show()

fig.savefig('savedthroughJupyter.jpg',dpi=1000)

# !pip cache clean --all
# !pip install ipympl
!pip show ipyml  

%matplotlib widget
fig=plt.figure(constrained_layout=True)
fig.set_size_inches(10,10)
ax=plt.axes(projection='3d')
ax.set_title('Surface Area')
x=np.linspace(-10,10,100)
y=np.linspace(-10,10,100)
X,Y=np.meshgrid(x,y)
Z=np.sin(X)+np.cos(Y)
ax.plot_surface(X,Y,Z,cmap='Spectral')
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
# ax.view_init(azim=0,elev=40)
# ax.view_init(azim=0,elev=120)
# fig.tight_layout()
plt.show()

#history=model.fit(),\ history.params *history is a callback which is in every keras model.
#########################################

g=(i for i in  range(10)) #generator object
next(g)
f=[i for i in  range(10)]
f

#Below is LIST COMPREHENSION
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
#############################################
a=input(print('Enter a number:'))
print(a)
#####################################
#a generator function for fibbonacci series
def gen():
  a=0
  b=1
  while True:
    yield a+b
    a,b=b,a+b # In python variable swapping is easily done by a,b=b,a
g=gen()

next(g) #Press enter several times

for _ in gen(): #Here the fibbonacci list is not entirely made but each element is produced as iterated over then discarded.
  if _<10000:
    print(_)
  else: 
    break

def gen():
  a=0
  b=1
  yield a+b
  a,b=b,a+b
g=gen()

next(g)#Here on second enter there is an error.why?

import os,shutil

base_dir='E://REGISTEREDCOURSES/Data Scientist Ja/17/Test'
os.mkdir(base_dir)

second_dir=os.path.join(base_dir,'1')
os.mkdir(second_dir)
third_dir=os.path.join(base_dir,'2')
os.mkdir(third_dir)
fourth_dir=os.path.join(base_dir,'3')
os.mkdir(fourth_dir)

a=10
f'print {a}'
f'print {a**10}'
names=[f'dog{i}.jpg' for i in range(10)]
names

for name in names:
  source=os.path.join(base_dir,name)
  destination=os.path.join(second_dir,name)
  shutil.copyfile(destination,source)
  
  
  
##############################

    
https://github.com/Alireza-Akhavan/deeplearning-tensorflow2-notebooks/tree/master/homework

# import numpy as np

# # Create a NumPy array
# arr = np.array([1, 2, 3, 2, 4, 1, 3, 4, 4, 4])

# # Get the unique values and their counts
# unique_values, counts = np.unique(arr, return_counts=True)

# # Print the results
# for value, count in zip(unique_values, counts):
#     print(f"{value} occurs {count} times"



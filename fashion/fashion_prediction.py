#python libray
import os
import cv2 
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

print("wHELL COME TO MY NOTEBOOK PROJECT")

train_new_model = True

if train_new_model:
    fashion = tf.keras.datasets.fashion_mnist
    (X_train, y_train), (X_test, y_test) = fashion.load_data()

    #normalize the data

    X_train = tf.keras.utils.normalize(X_train, axis = 1)
    X_test = tf.keras.utils.normalize(X_test, axis = 1)

    #create a neural network model
    #let train the model

    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(units=128, activation = tf.nn.relu))
    model.add(tf.keras.layers.Dense(units=128, activation = tf.nn.relu))
    model.add(tf.keras.layers.Dense(units=10, activation = tf.nn.softmax))

    #compile the model
    model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics=(['accuracy']))

    #fit the model for training

    model.fit(X_train, y_train,batch_size=128, epochs= 10)

    #Evaluate the model
    val_loss = model.evaluate(X_test,y_test)
    print(val_loss)

    #saving the model
    model.save('fasion model.keras')
else:
    #load the model
    model = tf.keras.models.load_model('fasion model.model')


# Load an external image for prdiction
image_path = 'dress.png'
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Preprocess the image to match the input shape of the model
img = cv2.resize(img, (28, 28))
img = np.invert(img)
img = img / 255.0
img = img.reshape(1, 28, 28, 1)

# Use the model to predict the image
prediction = model.predict(img)
predicted_digit = np.argmax(prediction)

print(f'The label number is probably a {predicted_digit}')
plt.imshow(img[0], cmap=plt.cm.binary)
plt.show()


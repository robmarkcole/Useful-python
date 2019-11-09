# https://datasciencechalktalk.com/2019/10/28/interactive-convolutional-neural-network/
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np

# import pydot_ng as pydot
import streamlit as st

st.title("Convolutional Neural Network")

st.header("Dataset: cifar10")

# spending a few lines to describe our dataset
st.text(
    """Dataset of 50,000 32x32 color training images, 
        labeled over 10 categories, 
        and 10,000 test images."""
)

from keras.datasets import cifar10

# I'm dividing my data into training and test set

(x_train, y_train), (x_test, y_test) = cifar10.load_data()


if st.checkbox("Show images sizes"):
    st.write(f"X Train Shape: {x_train.shape}")
    st.write(f"X Test Shape: {x_test.shape}")
    st.write(f"Y Train Shape: {y_train.shape}")
    st.write(f"Y Test Shape: {y_test.shape}")

class_names = [
    "airplane",
    "automobile",
    "bird",
    "cat",
    "deer",
    "dog",
    "frog",
    "horse",
    "ship",
    "truck",
]

st.subheader("Inspecting dataset")

if st.checkbox("Show random image from the train set"):
    num = np.random.randint(0, x_train.shape[0])
    image = x_train[num]
    st.image(
        image, caption=class_names[y_train[num][0]], width=64, use_column_width=False
    )

st.subheader("Set some hyperparameters")
batch_size = st.selectbox("Select batch size", [32, 64, 128, 256])
epochs = st.selectbox("Select number of epochs", [3, 10, 50, 100, 250])
loss_function = st.selectbox(
    "Loss function",
    ["categorical_crossentropy", "mean_squared_error", "mean_absolute_error"],
)
optimizer = st.selectbox("Optimizer", ["Adam", "SGD", "RMSprop"])

st.subheader("Building your CNN")
model = tf.keras.Sequential()

act1 = st.selectbox(
    "Activation function for first layer: ", ["relu", "tanh", "softmax"]
)
model.add(
    tf.keras.layers.Conv2D(
        32, kernel_size=(3, 3), activation=act1, input_shape=(32, 32, 3)
    )
)

model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))

if st.checkbox("Add drop layer?"):
    drop1 = st.selectbox("Which drop rate?", [0.1, 0.2, 0.5])
    model.add(tf.keras.layers.Dropout(drop1))
model.add(tf.keras.layers.Flatten())

act2 = st.selectbox(
    "Activation function for Dense layer: ", ["relu", "tanh", "softmax"]
)
model.add(tf.keras.layers.Dense(1024, activation=act2))

act3 = st.selectbox(
    "Activation function for Dense layer: ", ["relu", "tanh", "softmax"]
)
model.add(tf.keras.layers.Dense(10, activation=act3))

model.compile(loss=loss_function, optimizer=optimizer, metrics=["accuracy"])

if st.checkbox("Fit model"):
    history = model.fit(
        x_train[0:1000] / 255.0,
        tf.keras.utils.to_categorical(y_train[0:1000]),
        batch_size=batch_size,
        shuffle=True,
        epochs=epochs,
        validation_data=(
            x_test[0:1000] / 255.0,
            tf.keras.utils.to_categorical(y_test[0:1000]),
        ),
    )

    # Plot training & validation accuracy values
    plt.plot(history.history["accuracy"])
    plt.plot(history.history["val_accuracy"])
    plt.title("Model accuracy")
    plt.ylabel("Accuracy")
    plt.xlabel("Epoch")
    plt.legend(["Train", "Test"], loc="upper left")
    st.pyplot()

    predictions = model.predict(x_test / 255.0)
    scores = model.evaluate(x_test / 255.0, tf.keras.utils.to_categorical(y_test))

    st.write(f"loss: {round(scores[0],2)}")
    st.write(f"accuracy: {round(100*scores[1],2)}%")

st.subheader("Visualizing results")


def plot_pred(i, predictions_array, true_label, img):
    predictions_array, true_label, img = (
        predictions_array[i],
        true_label[i : i + 1],
        img[i],
    )
    plt.grid(False)
    plt.title(class_names[true_label[0][0]])
    plt.xticks([])
    plt.yticks([])

    plt.imshow(img)


def plot_bar(i, predictions_array, true_label):
    predictions_array, true_label = predictions_array[i], true_label[i]
    plt.grid(False)
    plt.yticks([])
    plt.xticks(np.arange(10), class_names, rotation=40)

    thisplot = plt.bar(range(10), predictions_array, color="grey")
    plt.ylim([0, 1])
    predicted_label = np.argmax(predictions_array)

    if predicted_label == true_label:
        color = "green"
    else:
        color = "red"

    thisplot[predicted_label].set_color(color)


if st.checkbox("Show random prediction results"):
    num2 = np.random.randint(0, len(y_test))
    plt.figure(figsize=(15, 6))
    plt.subplot(1, 2, 1)
    plot_pred(num2, predictions, y_test, x_test)
    plt.subplot(1, 2, 2)
    plot_bar(num2, predictions, y_test)
    st.pyplot()

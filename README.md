# Hindi Handwriting Recognition

## Introduction
The aim of this project is to build a model that can recognize handwritten Hindi characters. The dataset used for this project is [Devanagari Handwritten Character Dataset](https://archive.ics.uci.edu/ml/datasets/Devanagari+Handwritten+Character+Dataset) from UCI Machine Learning Repository. The dataset contains 92000 images of size 32x32. The dataset is divided into 46 classes, each class representing a character in Devanagari script. The dataset is divided into training, validation and test sets. The training set contains 78200 images, validation set contains 13800 images and test set contains 23000 images. The dataset is balanced, i.e., each class has equal number of images.

## Building the Model
The model is built using Convolutional Neural Networks (CNNs). The model is built using Keras with Tensorflow backend. The model is trained for 10 epochs with a batch size of 128. The model is trained on Google Colab. The model is trained on a GPU for faster training. The model is trained using Adam optimizer with a learning rate of 0.001. The model is trained using categorical cross entropy as the loss function. The model is trained using accuracy as the metric. The model is trained using early stopping with patience of 5. The model is trained using model checkpoint to save the best model.

## Run the Server
To run the server, run the following command in the terminal:

* Install the dependencies
```bash
python -m pip install -r requirements.txt
```

* Run the server
```
python main.py
```

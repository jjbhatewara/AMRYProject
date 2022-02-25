
from keras.models import Model, load_model
import os
import cv2
import numpy as np
import tensorflow as tf
import pandas as pd
from keras.models import Model, load_model
from skimage.morphology import label
import pickle
import tensorflow.keras.backend as K
from matplotlib import pyplot as plt
from tqdm import tqdm_notebook
import random
from skimage.io import imread, imshow, imread_collection, concatenate_images
from matplotlib import pyplot as plt
import h5py
model = load_model('app\Roads\my_model_dropout.h5', compile=False)
def dice_coef_loss(y_true, y_pred):
    smooth = 1
    y_true_f = tf.compat.v1.layers.flatten(y_true)
    y_pred_f = tf.compat.v1.layers.flatten(y_pred)
    intersection = tf.reduce_sum(y_true_f * y_pred_f)
    return (1.0 - (2. * intersection + smooth) / (tf.reduce_sum(y_true_f) + tf.reduce_sum(y_pred_f) + smooth) )
model.compile(optimizer='adam', loss=dice_coef_loss, metrics=['accuracy'])
image_size=128


def Roads(path):
    print(path)
    image = cv2.imread(path)
    image = cv2.resize(image, (image_size, image_size))
    image = image/255.0
    image = tf.expand_dims(image, axis=0)
    image = np.array(image)
    print(image)
    result = model.predict(image)
    print(result)
    return path
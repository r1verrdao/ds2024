import numpy as np
import os 
from PIL import Image
import tensorflow as tf 
from tensorflow.keras import layers
from tensorflow.keras import Model
from tensorflow.keras.applications import vgg16
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split

# load model VGG16
based_model = vgg16.VGG16(weights = 'imagenet',
                    include_top = False,
                    input_shape = (img_rows, img_cols, 3))

# Freeze layers, not training these layers
for layer in based_model.layers:
    layer.trainable = False 

# Summary model 
based_model.summary()
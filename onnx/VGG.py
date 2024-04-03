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
                    input_shape = (224, 224, 3))

# Freeze layers, not training these layers
for layer in based_model.layers:
    layer.trainable = False 

# Summary model 
print("The base model: ")
based_model.summary()

def layer_added(output_based_network, num_classes):
  x = output_based_network
  x = layers.Flatten()(x)
  x = layers.Dense(1024, activation='relu')(x)
  x = layers.Dense(256, activation='relu')(x)
  x = layers.Dense(num_classes, activation='softmax')(x)

  return x

num_classes = 19
output_based_network = based_model.output 
output_layer = layer_added(output_based_network, num_classes)
model = Model(based_model.input, output_layer)
print("The model after add output layers: \n")
model.summary()
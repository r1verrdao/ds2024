# import libraries
import os
import tensorflow as tf
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np
import onnxruntime

#img path
img_path: str = 'ade20k.jpg'

# load the image
img = image.load_img(img_path, target_size=(224, 224))

x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

# define a simple model
model = ResNet50(weights='imagenet')

preds = model.predict(x)
print('Keras Predicted:', decode_predictions(preds, top=3)[0])
model.save(os.path.join("/tmp", model.name))
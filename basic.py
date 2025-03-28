from tensorflow.keras.preprocessing import image
import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model("blood_group_classifier.keras")

img_path = r"c:\Users\LENOVO\Downloads\augmented_cluster_0_16.BMP"  # Replace with an actual image path
img = image.load_img(img_path, target_size=(224, 224))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)  
img_array = img_array / 255.0  

prediction = model.predict(img_array)
print("Prediction Output:", prediction)

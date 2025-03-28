from flask import Flask, request, jsonify , render_template
import tensorflow as tf
import numpy as np
from io import BytesIO
from tensorflow.keras.preprocessing import image

# Initialize Flask app
app = Flask(__name__)



# Load the model
model = tf.keras.models.load_model("blood_group_classifier.keras")  # Ensure the model is in the same directory

@app.route('/')
def home():
    return render_template('home.html')  # Replace with the correct HTML file name
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/scan')
def scan():
    return render_template('scan.html')
@app.route('/results')
def results():
    return render_template('results.html')
@app.route('/faq')
def faq():
    return render_template('faq.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Define a route for inference
@app.route('/predict', methods=['POST'])
def predict():
    try:
        file_stream = request.files['file']

        img_file = BytesIO()

        file_stream.save(file_stream)

        img_file.seek(0)
        
        # Preprocess the image
        img = image.load_img(img_file, target_size=(128, 128))  # Change (224, 224) to (128, 128)
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)  # Convert to batch format
        img_array = img_array / 255.0  # Normalize (modify if needed)

        # Make prediction
        prediction = model.predict(img_array)

        # Convert prediction to a readable format
        result = prediction.tolist()  # Convert NumPy array to list for JSON serialization
        
        return jsonify({'prediction': result})

    except Exception as e:
        return jsonify({'error': str(e)})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
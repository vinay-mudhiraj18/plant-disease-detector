from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)
model = load_model("plant_disease_model.h5")
UPLOAD_FOLDER = "static/uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

class_labels = [
    'Pepper__bell___Bacterial_spot', 'Pepper__bell___healthy', 'PlantVillage',
    'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy',
    'Tomato_Bacterial_spot', 'Tomato_Early_blight', 'Tomato_Late_blight',
    'Tomato_Leaf_Mold', 'Tomato_Septoria_leaf_spot',
    'Tomato_Spider_mites_Two_spotted_spider_mite', 'Tomato__Target_Spot',
    'Tomato__Tomato_YellowLeaf__Curl_Virus', 'Tomato__Tomato_mosaic_virus',
    'Tomato_healthy'
]

remedies = {
    'Tomato_Bacterial_spot': 'Use copper-based fungicides.',
    'Tomato_Early_blight': 'Apply chlorothalonil fungicide.',
    'Tomato_Late_blight': 'Destroy infected plants.',
    'Tomato_Leaf_Mold': 'Ensure airflow, use fungicide.',
    'Tomato_Septoria_leaf_spot': 'Remove debris, apply mancozeb.',
    'Tomato_Spider_mites_Two_spotted_spider_mite': 'Use neem oil.',
    'Tomato__Target_Spot': 'Apply fungicides.',
    'Tomato__Tomato_YellowLeaf__Curl_Virus': 'Control whiteflies.',
    'Tomato__Tomato_mosaic_virus': 'Disinfect tools.',
    'Tomato_healthy': 'Plant is healthy!',
    'Potato___Early_blight': 'Use certified seeds, fungicide.',
    'Potato___Late_blight': 'Spray copper-based fungicides.',
    'Potato___healthy': 'Plant is healthy!',
    'Pepper__bell___Bacterial_spot': 'Use copper sprays.',
    'Pepper__bell___healthy': 'Plant is healthy!',
    'PlantVillage': 'Placeholder class — review image.'
}

def predict_disease(img_path):
    img = image.load_img(img_path, target_size=(128, 128))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    class_idx = np.argmax(prediction)
    confidence = round(100 * np.max(prediction), 2)
    disease = class_labels[class_idx]
    remedy = remedies.get(disease, "No remedy available.")
    
    return disease, confidence, remedy

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["image"]
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            disease, confidence, remedy = predict_disease(file_path)
            return render_template("index.html", prediction=disease, confidence=confidence, remedy=remedy, img_path=file_path)

    return render_template("index.html", prediction=None)

if __name__ == "__main__":
    app.run(debug=True)

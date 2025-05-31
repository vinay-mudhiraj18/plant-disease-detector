# 🌿 Plant Leaf Disease Detection System

This is a Plant Disease Detection Web Application built using deep learning. It allows users to upload images of plant leaves and predicts the disease (if any) using a trained AI model. The project contributes to agricultural sustainability by helping farmers detect and act on plant diseases early.

---

## 📌 Project Overview

- ✅ Built from scratch using TensorFlow/Keras  
- ✅ Trained on the PlantVillage dataset (16 classes)  
- ✅ Trained model saved as `plant_disease_model.h5`  
- ✅ Flask-based web interface for easy usage  
- ✅ User uploads an image and gets instant disease predictions  
- ✅ Hosted on GitHub for public access and deployment  

---

## 📁 Project Structure

PlantDiseaseWebApp/
├── app.py # Flask web server
├── plant_disease_model.h5 # Trained CNN model
├── requirements.txt # Project dependencies
├── templates/
│ └── index.html # Web interface
├── static/
│ └── uploads/ # Stores uploaded images
└── README.md # Project documentation

---

## 📊 Dataset Details

- **Source**: [PlantVillage Dataset on Kaggle](https://www.kaggle.com/datasets/emmarex/plantdisease)
- **Total Classes**: 16
- **Images**: ~5,000
- **Example Classes**:
  - Tomato_Early_blight  
  - Tomato_Late_blight  
  - Potato_healthy  
  - Pepper__bell___Bacterial_spot  
  - Tomato__Tomato_YellowLeaf__Curl_Virus  
  - And more...

---

## 🤖 Model Training Summary

- **Framework**: TensorFlow / Keras  
- **Input Shape**: 128x128 RGB images  
- **Architecture**: CNN with Conv2D, MaxPooling2D, Dense, Dropout  
- **Accuracy Achieved**: ~97% on validation  
- **Epochs**: 10  
- **Optimizer**: Adam  
- **Loss**: Categorical Crossentropy  

> Training was done in Google Colab with GPU acceleration.  
> The final trained model is saved as `plant_disease_model.h5`.

---

## ✅ Steps to Run the Project from GitHub

### 🔧 Requirements

- Python 3.7 or higher installed  
- `git` installed and added to your system PATH  
- Internet connection (for downloading dependencies)

---

### 🚀 Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/vinay-mudhiraj18/plant-disease-detector.git
cd plant-disease-detector

# 2. (Optional but recommended) Create and activate a virtual environment
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# 3. Install the required packages
pip install -r requirements.txt

# 4. Run the Flask application
python app.py
Open your browser and go to:
👉 http://127.0.0.1:5000/

From there, you can upload a plant leaf image and the system will predict its disease!

📜 License
This project is licensed under the MIT License.

🙌 Acknowledgements
PlantVillage Dataset

TensorFlow / Keras

Flask

Google Colab

👤 Author
Vinay Mudhiraj
🔗 GitHub Profile

Potato Disease Classifier 🍟🌱

A deep learning-based image classifier for potato types using PyTorch** and efficientNet-B0.  
The project allows training a model on your potato dataset and predicting the class of new images.

1. Contents

- Project Structure
- Features
- Installation
- Dataset
- Training
- Usage
- Contributing
- License

2. Project Structure

potato_demo/
├── classifier/
│ ├── datasets/ # Potato image dataset (organized by class)
│ ├── ml_models/ # Saved trained models
│ ├── urls.py
│ ├── views.py
│ ├── utils.py # Prediction code
├── media/ # Uploaded images for prediction
├── train_model.py # Script to train the model
├── manage.py # Django entry point
├── db.sqlite3 # Database
└── README.md

3. Features

- Train a custom EfficientNet-B0 model for potato classification.
- Image preprocessing with augmentation for robust training.
- Integration with a Django web app for real-time image prediction.
- Easy interface to upload and classify potato images.

4. Installation

1. Clone the repository:

git clone https://github.com/aathithiyan45/potato_demo.git
cd potato_demo
Create and activate a Python virtual environment:

python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

Install required dependencies:
pip install torch torchvision timm pillow django
Dataset

Place your dataset in classifier/datasets/

Example structure:

markdown
Copy code
datasets/
├── Red/
│   ├── img1.jpg
│   └── ...
├── Russet/
│   ├── img1.jpg
│   └── ...
└── YukonGold/
    ├── img1.jpg
    └── ...
Training
Run the training script:

python train_model.py
Model will be saved automatically in:
classifier/ml_models/potato_classifier.pth

Training uses 5 epochs by default (adjustable in train_model.py).

Usage
Start the Django server:

python manage.py runserver

Open your browser at:

http://127.0.0.1:8000/
Upload a potato image to get predictions.

Contributing
Contributions, suggestions, and bug reports are welcome!
Open an issue or submit a pull request.

License
This project is licensed under the MIT License. See LICENSE file for details.

Author: Aathithiyan P(@aathithiyan45)

If you want, I can also add badgesike PyTorch version, Python version, or “Training Status” to make it look even more like a polished professional GitHub repo.  







# Potato Disease Classifier 🍟🌱

A deep learning-based image classifier for potato types using **PyTorch** and **EfficientNet-B0**.  
This project allows training a model on your potato dataset and predicting the class of new images.

---

## Features

- Train a custom **EfficientNet-B0** model for potato classification.
- Image preprocessing with augmentation for robust training.
- Integration with a **Django web app** for real-time image prediction.
- Easy interface to upload and classify potato images.

---

## Installation

1. Clone the repository:

- git clone https://github.com/aathithiyan45/Potato-Classifier.git
- cd Potato-Classifier
  
2. Create and activate a Python virtual environment:

- python3 -m venv venv
- source venv/bin/activate   # macOS/Linux
- venv\Scripts\activate      # Windows
  
4. Install required dependencies:

- pip install torch torchvision timm pillow django
  
5. Dataset
   
- Place your dataset in classifier/datasets/ with subfolders for each class.

6. python train_model.py

- The trained model will be saved automatically at:
- classifier/ml_models/potato_classifier.pth

- Default training is 5 epochs (adjustable in train_model.py).

7. Usage

- Start the Django server:

- python manage.py runserver

8. Open your browser at:

- http://127.0.0.1:8000/

9. Upload a potato image to get predictions.

Contributing
Contributions, suggestions, and bug reports are welcome!
Please open an issue or submit a pull request.

License
This project is licensed under the MIT License. See LICENSE file for details.

Author: Aathithiyan P (@aathithiyan45)


If you want, I can also **add badges** for Python version, PyTorch, and License so your README looks **more professional and portfolio-ready**.  

Do you want me to do that next?

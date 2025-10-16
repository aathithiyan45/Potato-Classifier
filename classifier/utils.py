# classifier/utils.py
from PIL import Image
import torch
from torchvision import transforms
import timm

device = 'cuda' if torch.cuda.is_available() else 'cpu'
MODEL_PATH = 'classifier/ml_models/potato_classifier.pth'
class_names = ['Red', 'Russet', 'YukonGold']

# Load model once
model = timm.create_model('efficientnet_b0', pretrained=False, num_classes=len(class_names))
model.load_state_dict(torch.load(MODEL_PATH, map_location=device))
model.to(device)
model.eval()

def predict_potato(image_path):
    img = Image.open(image_path).convert("RGB")
    transform = transforms.Compose([
        transforms.Resize((224,224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485,0.456,0.406],[0.229,0.224,0.225])
    ])
    img_t = transform(img).unsqueeze(0).to(device)
    with torch.no_grad():
        outputs = model(img_t)
        _, pred = torch.max(outputs, 1)
    return class_names[pred.item()]

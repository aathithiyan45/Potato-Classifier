from django.shortcuts import render
from .utils import predict_potato
import os

def home(request):
    result = ''
    if request.method == 'POST' and request.FILES.get('image'):
        uploaded_file = request.FILES['image']
        file_path = os.path.join('media', uploaded_file.name)
        os.makedirs('media', exist_ok=True)
        with open(file_path, 'wb+') as f:
            for chunk in uploaded_file.chunks():
                f.write(chunk)
        result = predict_potato(file_path)
    return render(request, 'classifier/home.html', {'result': result})

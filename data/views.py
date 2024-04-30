from django.shortcuts import render
from django.http import HttpResponse
from .models import Image
import pandas as pd

# Create your views here.


def load_csv(request):
    data = pd.read_csv('yourfile.csv')
    for index, row in data.iterrows():
        image = Image(
            image_name=row['image_name'],
            predicted_labels=row['predicted_labels'],
            dominant_color=row['dominant_color'],
            confidence=row['confidence']
        )
        image.save()
    return HttpResponse("CSV data loaded successfully")
from django.db import models

# Create your models here.
class Image(models.Model):
    image_name = models.CharField(max_length=255)
    predicted_labels = models.CharField(max_length=255)
    dominant_color = models.CharField(max_length=7)
    confidence = models.FloatField()
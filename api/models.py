from django.db import models

# Create your models here.
class Creator(models.Model) :
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=100)
    bio = models.CharField(max_length=100)
    Specialty = models.TextChoices('Specialty',
        'Renders',
        'Layout',
        'Digital modelling',
        'Real models',
        'Presentation'
        )
    specialty = models.CharField(blank=True, choices=Specialty.choices, max_length=3)
    freelance = models.BooleanField(max_length=100)

class Showpiece(models.Model) :
    created_by=models.models.ForeignKey(Creator, on_delete=models.CASCADE)
    name =models.CharField(max_length=50)
    about= models.TextField(max_length=500)
    Subject_matter=models.TextChoices('Subject_matter', 'renders','drawings','display_models','fullpresentation')
    drawings=models.TextField(blank=True,max_length=500)
    renders=models.TextField(blank=True,max_length=500)
    display_models=models.TextField(blank=True,max_length=500)
    full_presentaion=models.TextField(blank=True,max_length=500)

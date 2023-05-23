from django.db import models

class Cake(models.Model):
    name=models.CharField(max_length=200)
    flavour=models.CharField(max_length=300)
    prize=models.PositiveIntegerField()
    shape=models.CharField(max_length=200)
    description=models.CharField(max_length=500)
    number=models.CharField(max_length=200,unique=True)
    weight=models.CharField(max_length=200)
    cake_image=models.ImageField(upload_to="images",null=True,blank=True)

    def __str__(self) -> str:
      return self.name 
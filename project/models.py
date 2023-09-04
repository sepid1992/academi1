from django.db import models

# Create your models here.
class  shop (models.Model):
    onvan=models.CharField(max_length=30)
    price=models.IntegerField()
    ax=models.ImageField(upload_to="ax")
    tosif=models.TextField()
    noe=models.IntegerField(default=1)
    def __str__(self):
        return self.onvan
    


class contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    phone_number=models.CharField(max_length=20)
    msg_subject=models.CharField(max_length=500)
    def __str__(self):
        return self.name


    
    
    

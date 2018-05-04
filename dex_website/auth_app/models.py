from django.db import models

# Create your models here.
class UpdateSubscribe(models.Model):
    email=models.EmailField(unique=True)
    def __str__(self):
        return str(self.email)


class contactData(models.Model):
    id=models.BigAutoField(primary_key=True)
    firstName=models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email=models.EmailField(null=False)
    company= models.CharField(max_length=70)
    def __str__(self):
        return str(self.id)
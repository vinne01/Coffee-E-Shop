from django.db import models

# # Create your models here.

class Coffee(models.Model):
    name=models.CharField(max_length=100)
    amount=models.CharField(max_length=100)
    email=models.CharField(max_length=100,default="example@example.com")
    payment_id=models.CharField(max_length=100)
    paid=models.BooleanField(default=False)
    
     # New fields added
    coffee_type = models.CharField(max_length=100,default='Indian')  # Store the type of coffee
    quantity = models.IntegerField(default=1)       # Store the quantity ordered


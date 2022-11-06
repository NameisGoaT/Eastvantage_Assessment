from django.db import models

# Create your models here.

    
class AddressB(models.Model):
    user_name = models.CharField(max_length=60)
    Address_Line1= models.CharField(max_length=200)
    Landmark= models.CharField(max_length=60)
    Pincode=models.IntegerField()
    State= models.CharField(max_length=40)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '{}        {}'.format(self.user_name, self.created)
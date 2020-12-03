from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)
    
    
    def __str__(self):
        return 'Message from ' + self.name 
    
class Email(models.Model):
    no = models.AutoField(primary_key=True)
    nm = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    
    def __str__(self):
        return 'Email address of ' + self.nm + ' is ' + self.address
    
    
class WhatsApp(models.Model):
    cid = models.AutoField(primary_key=True)
    contact = models.CharField(max_length=100)
    number = PhoneNumberField()
    
    def __str__(self):
        return 'Contact Number of ' + self.contact + ' is ' + str(self.number)
    
from django.db import models
from django.urls import reverse
# Create your models here.

class Contact(models.Model):
    name    = models.CharField(max_length=255)
    email   = models.EmailField(max_length=255)
    phone   = models.CharField(max_length=11)
    message = models.TextField()
    date_recieved = models.DateTimeField(auto_now_add=True)
    date_updated  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  self.email

    class Meta:
        ordering = ('-date_recieved',)

    
    # def get_absolute_url(self):
    #     return reverse("message-detail", args=[str(self.id)])
from django.db import models

# Create your models here.

class Partner(models.Model):

    STATUS_CHOICES = (
        ('gov', 'Governmental'),
        ('ngo', 'Non-Governmental'),
        ('pro', 'Profit'),
        ('npro', 'Non-Profit'),
        ('ind', 'Individual')
    )
    name            = models.CharField(max_length=100, unique=True)
    acronym         = models.CharField(max_length=10, unique=True, blank=True, null=True)
    email           = models.EmailField(max_length=50, unique=True)
    phone           = models.CharField(max_length=12, unique=True)
    website         = models.URLField(null=True, blank=True, unique= True)
    country         = models.CharField(max_length=50)
    state           = models.CharField(max_length=50)
    lga             = models.CharField('LGA', max_length=50)
    status          = models.CharField(max_length=30, choices=STATUS_CHOICES, default='ngo')
    picture         = models.ImageField(upload_to='partner/logo/', blank=True, null=True)
    about           = models.TextField()
    date_created    = models.DateTimeField(auto_now_add=True)
    date_updated    = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
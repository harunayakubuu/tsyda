from django.db import models
from partner.models import Partner
from blog.models import Category
# Create your models here.


class Project(models.Model):
    PROJECT_STATUS_CHOICES = (
        ('completed', 'Completed'),
        ('inprogress', 'In Progress'),
        # ('pending', 'Pending'),
        # ('terminated', 'Terminated')
    )
    project_title       = models.CharField(max_length=50, unique=True)
    categories          = models.ManyToManyField(Category)
    image               = models.ImageField(upload_to='portfolio/pictures/', null=True, blank=True)
    project_leader      = models.CharField(max_length=50)
    estimated_duration  = models.PositiveSmallIntegerField(default=0, help_text = "Number in weeks")
    estimated_budget    = models.FloatField(editable=True)
    total_amount_spent  = models.FloatField(editable=True)
    about_project       = models.TextField()
    sponsors            = models.ManyToManyField(Partner)
    beneficiaries       = models.PositiveSmallIntegerField(default=0)
    previous_project    = models.ForeignKey('self', related_name = 'previous', on_delete = models.SET_NULL, blank = True, null = True)
    next_project        = models.ForeignKey('self', related_name = 'next', on_delete = models.SET_NULL, blank = True, null = True)
    completed           = models.BooleanField(default=False)
    date_completed      = models.DateField(null = True, blank = True)

    def __str__(self):
        return self.project_title

    class Meta:
        ordering = ("-id",)
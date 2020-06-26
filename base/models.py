from django.db import models

class FaqQuestion(models.Model):
    question = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.question

class FaqAnswer(models.Model):
    question  = models.ForeignKey(FaqQuestion, on_delete=models.CASCADE)
    answer = models.CharField(max_length=225)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-created',)
        
    def __str__(self):
        return self.answer
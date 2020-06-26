from django.contrib import admin
from .models import FaqQuestion, FaqAnswer

@admin.register(FaqQuestion)
class FaqQuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'created', 'updated')

@admin.register(FaqAnswer)
class FaqAnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'created', 'updated')
from django.urls import path
from .views import index, about, faq, privacy_policy,terms_and_conditions, thank_you


urlpatterns = [
    path('', index, name='index'),
    path('about-us/', about, name='about'),
    path('privacy-policy/', privacy_policy, name='privacy-policy'),
    path('faqs/', faq, name='faqs'),
    path('terms-and-conditions/', terms_and_conditions, name='terms-and-conditions'),
    path('thank-you/', thank_you, name='thank-you'),
]
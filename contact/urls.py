from django.urls import path
from .views import (
    contact,
    contact_messages_list,
    contact_message_detail,
    contact_message_delete
)


urlpatterns = [
    path('contact-us/', contact, name='contact'),
    path('contact/messages/',contact_messages_list, name='message-list'),
    path('contact/message/<id>/',contact_message_detail, name='message-detail'),
    path('contact/message/<id>/delete/',contact_message_delete, name='message-delete'),
]
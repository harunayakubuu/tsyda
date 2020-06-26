from django.urls import path
from . views import (
    partners_view, #PartnersView,
    partner_list_view, #PartnerListView,
    partner_detail_view,
    partner_create_view,
    partner_update_view,
    partner_delete_view
)


urlpatterns = [
    path('', partners_view, name='partners'),
    path('list/', partner_list_view, name='partner-list'),
    path('<int:id>/', partner_detail_view, name='partner-detail'),
    path('add/', partner_create_view, name='partner-create'),
    path('<int:id>/update/', partner_update_view, name='partner-update'),
    path('<int:pk>/delete/', partner_delete_view.as_view(), name='partner-delete'),
]
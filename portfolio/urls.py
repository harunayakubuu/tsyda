from django.urls import path
from .views import (
    project_list,
    project_detail,

    portfolios,
    portfolio_detail,
    project_create,
    portfolio_update,
    portfolio_delete
)

urlpatterns = [
    path('projects/', project_list, name='project-list'),
    path('projects/<id>/', project_detail, name='project-detail'),
    
    path('project/list/', portfolios, name='portfolio-list'),
    path('project/add/', project_create, name='portfolio-create'),
    path('project/<id>/', portfolio_detail, name='portfolio-detail'),
    path('project/<id>/update/', portfolio_update, name='portfolio-update'),
    path('project/<pk>/delete/', portfolio_delete.as_view(), name='portfolio-delete'),
]
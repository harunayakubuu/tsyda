from django.urls import path
from .views import (
    dashboard,
    user_list,
    user_detail,

    profile,
    profile_update
)

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('user/list/', user_list, name='user-list'),
    path('member/<username>/', user_detail, name='user-detail'),

	path('profile/', profile, name = 'profile'),
	path('profile/update/', profile_update, name='profile-update')
]
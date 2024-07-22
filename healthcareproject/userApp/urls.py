from django.urls import path, include, re_path
from userApp import views as vw


urlpatterns = [
    re_path(r'my_profile/(?P<user_id>\d+)/', vw.myProfile, name='my_profile'),
    re_path(r'edit_profile/(?P<user_id>\d+)/', vw.editProfile, name='edit_profile'),
    re_path(r'deactivate/(?P<user_id>\d+)/', vw.deactivate, name='deactivate'),
    path('all_users/<str:status>/', vw.displayUsers, name='all_users'),
    path('delete_user/<str:status>/', vw.deleteUser, name='delete_users'),

]
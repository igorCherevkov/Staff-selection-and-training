from django.urls import path
from users.views import userRegistration, userLogin, userLogout, userProfile, createResume

app_name = 'users'

urlpatterns = [
    path('userLogin/', userLogin, name='userLogin'),
    path('userRegistration/', userRegistration, name='userRegistration'),
    path('userLogout/', userLogout, name='userLogout'),
    path('userProfile/', userProfile, name='userProfile'),
    path('createResume/', createResume, name='createResume')
]

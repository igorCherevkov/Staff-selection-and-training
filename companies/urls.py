from django.urls import path
from companies.views import companyRegistration, companyProfile, vacancyInfo, addInitialTest, initialTest

app_name = 'companies'

urlpatterns = [
    path('companyRegistration/', companyRegistration, name='companyRegistration'),
    path('companyProfile/', companyProfile, name='companyProfile'),
    path('vacancy<int:id>/', vacancyInfo, name='vacancyInfo'),
    path('addInitialTest<int:id>/', addInitialTest, name='addInitialTest'),
    path('initialTest<int:id>/', initialTest, name='initialTest')
]

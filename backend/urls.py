from django.contrib import admin
from django.urls import path, include
from companies.views import mainPage
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainPage, name='mainPage'),
    path('users/', include('users.urls', namespace='users')),
    path('companies/', include('companies.urls', namespace='companies'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
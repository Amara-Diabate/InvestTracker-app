from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('portfolios/', include('portfolios.urls')),
    path('investments/', include('investments.urls')),
    path('corporates/', include('corporates.urls')),
    path('documents/', include('documents.urls')),
]

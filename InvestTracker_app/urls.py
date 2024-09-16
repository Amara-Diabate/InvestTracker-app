from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('Users.urls')),
    path('portfolios/', include('Portfolios.urls')),
    path('investments/', include('Investments.urls')),
    path('corporates/', include('Corporates.urls')),
    path('documents/', include('Documents.urls')),
]

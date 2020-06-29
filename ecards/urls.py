from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include('ecard_app.urls')),
    #path('about/', include('ecard_app.urls')),
]
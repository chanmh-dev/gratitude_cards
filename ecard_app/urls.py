from django.urls import path
from ecard_app import views as ecard_views

urlpatterns = [
    path('', ecard_views.index, name = 'index'),
    path('index', ecard_views.index, name = 'index'),
    #path('ecard', ecard_views.ecard, name = 'ecard'),
    #path('about', ecard_views.about, name = 'about'),
]
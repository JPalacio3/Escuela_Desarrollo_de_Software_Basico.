from django.urls import path

# Views
from . import views

#Config URL
urlpatterns = [
    path('', views.profile, name='profile'),
]

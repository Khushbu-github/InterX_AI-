
from django.urls import path, include

from . import views

urlpatterns = [


    path('', views.public_chat,name='gc'),
]

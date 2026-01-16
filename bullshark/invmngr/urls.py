from django.urls import path 

from . import views 

urlpatterns = [
    path('', views.blsk_index, name='blsk_index'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('events/<int:pk>', views.event_detail, name='event_detail'),
    path('events/new', views.event_create, name='event_create'),
]
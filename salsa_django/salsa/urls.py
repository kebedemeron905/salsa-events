from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list),
    path('events/<int:pk>', views.event_detail),
]
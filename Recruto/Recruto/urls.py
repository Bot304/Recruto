from django.urls import path
from RecrutoWeb import views
 
urlpatterns = [
    path("", views.index),
]

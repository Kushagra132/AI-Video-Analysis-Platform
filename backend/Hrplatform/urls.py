from django.urls import path,re_path
from . import views

urlpatterns = [
    path('audio',views.Audio_store),
    path('result',views.result)
]

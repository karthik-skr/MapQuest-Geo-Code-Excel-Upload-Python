from django.urls import path

from . import views

app_name = "geo_code_app"

urlpatterns = [
    path('', views.index, name='index'),
]
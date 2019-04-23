from django.urls import path
from . import views

urlpatterns = [
    path('all', views.get_all_informations),
    path('detail/<id>', views.get_information_by_id),
]
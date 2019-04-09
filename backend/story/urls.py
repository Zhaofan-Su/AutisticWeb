from django.urls import path
from . import views

urlpatterns = [
    path('all', views.get_all_stories),
    path('detail/<id>', views.search_by_id),
]

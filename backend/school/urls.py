from django.urls import path
from school import views

urlpatterns = [
    path('province/', views.get_by_province),
    path('<province>/city/', views.get_by_city),
]
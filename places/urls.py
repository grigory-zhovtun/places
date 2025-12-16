from django.urls import path
from . import views

urlpatterns = [
    path('<int:place_id>/', views.place_detail, name='place_detail'),
]
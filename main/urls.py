from . import views
from django.urls import include, path

urlpatterns = [
    path('api/search/', views.search),
]

from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.ExperienceList.as_view(), name='experience_list'),
    path('<int:pk>/', views.ExperienceDetail.as_view(),
         name='experience_detail')
]

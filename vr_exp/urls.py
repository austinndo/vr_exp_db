from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.experiences, name='experiences'),
    path('experiences/', views.ExperienceList.as_view(), name='experience_list'),
    path('experiences/<int:pk>', views.ExperienceDetail.as_view(),
         name='experience_detail')
]

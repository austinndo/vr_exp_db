from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('experiences/', views.ExperienceList.as_view(), name='experience_list'),
    path('experiences/<int:pk>/', views.ExperienceDetail.as_view(),
         name='experience_detail')
]

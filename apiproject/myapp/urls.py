from django.urls import path
from myapp import views

urlpatterns = [
    path('myapi/', views.BlocktList.as_view()),
    path('details/<int:pk>/', views.ApiDetail.as_view()),

]
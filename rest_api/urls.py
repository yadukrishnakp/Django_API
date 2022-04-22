from django.urls import path
from . import views

urlpatterns = [
    # path('', views.Show_Employee, name="show-employees")
    path('create_employee/', views.Create_Employee, name="create-employee")
]
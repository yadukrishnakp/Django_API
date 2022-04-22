from django.urls import path
from . import views

urlpatterns = [
    # path('', views.Show_Employee, name="show-employees")
    path('create_employee/', views.Create_Employee, name="create-employee"),
    path('show_all_employees/', views.Show_all_Employees, name="show-all-employee"),
    path('show_employee/<str:pk>', views.Show_Employee, name="create-employee"),
]
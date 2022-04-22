from django.urls import path
from . import views

urlpatterns = [
    path('create_employee/', views.Create_Employee, name="create-employee"),
    path('show_all_employees/', views.Show_all_Employees, name="show-all-employee"),
    path('show_employee/<str:pk>', views.Show_Employee, name="create-employee"),
    path('update_employee/<str:pk>', views.Update_Employee, name="update-employee"),
    path('delete_employee/<str:pk>', views.Delete_Employee, name="create-employee"),
]
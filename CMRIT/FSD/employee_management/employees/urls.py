from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('edit_employee/<int:pk>/', views.edit_employee, name='edit_employee'),
    path('employee_list/', views.employee_list, name='employee_list'),
]

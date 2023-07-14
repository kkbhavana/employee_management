from django.urls import path

from .views import EmployeeListView, EmployeeUpdateView, EmployeeDeleteView, EmployeeDetailView

urlpatterns = [
    path('emp_list/', EmployeeListView.as_view(), name='list'),
    path('emp-update/<int:pk>/',EmployeeUpdateView.as_view(),name='update'),
    path('emp-delete/<int:pk>/',EmployeeDeleteView.as_view(),name='delete'),
    path('emp-detail/<int:pk>/',EmployeeDetailView.as_view(),name='details'),
]

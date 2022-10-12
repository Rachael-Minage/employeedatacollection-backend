from .views import RegisterAPI
from django.urls import path
from knox import views as knox_views
from .views import LoginAPI
from django.urls import path
from .views import employeeApi
from .views import csv_upload





urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path("employee/",employeeApi,name='employeeApi'),
    path('csv/',csv_upload,name='csv_upload')  ,

]



from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('perform_login',views.preform_login,name='perform_login'),
    path('delete',views.delete,name='delete'),
    path('admin_dashboard/',views.admin_dashboard,name='admin_dashboard'),
]

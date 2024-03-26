from django.urls import path
from .views import index, success, signup

urlpatterns = (
    path('', index, name='index'),
    path('success', success, name='success'),
    path('login', signup, name='login')

)
from django.urls import path
from .views import my_lambda, login, logged_out, index

urlpatterns = [
    path('my_lambda/', my_lambda, name='my_lambda'),
    path('login/', login, name='login'),
    path('logged_out/', logged_out, name='logged_out'),
    path('index/', index, name='index'),
]

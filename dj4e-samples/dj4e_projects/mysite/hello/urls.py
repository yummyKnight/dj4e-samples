from django.urls import path

from . import views

app_name = "hello"

urlpatterns = [
    # ex: /polls/
    path('', views.sess_fun, name='sess_fun'),

]

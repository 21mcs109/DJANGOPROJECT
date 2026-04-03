from django.urls import path
from .views import *

urlpatterns = [
    path("", homePageView, name="home"),
    path("first/", first, name='first'),
    path("members/", members, name='members'),
    path('members/details/<int:id>', details, name='details'),
    path('testing/',testing),

]

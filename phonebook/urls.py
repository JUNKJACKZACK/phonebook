from django.urls import path

from phonebook.views import index

urlpatterns = [
    path('', index, name="home")
]
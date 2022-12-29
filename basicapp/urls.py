from django.urls import path
from django.contrib import admin
from . import views

urlpatterns =[
	path('',views.index, name='index'),
	path('form',views.form_name_view, name='form_name_view')

]
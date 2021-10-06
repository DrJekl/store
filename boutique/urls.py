from django.urls import path

from . import views


urlpatterns = [
	path('', views.index, name='index'),
	path('register', views.register, name='register'),
	path('look/<str:item>', views.look, name='look'),
	path('create', views.create, name='create'),
	path('demand', views.demand, name='demand'),
	path('leave', views.demand, name='leave'),
	path('mystuff', views.mystuff, name='mystuff'),
]
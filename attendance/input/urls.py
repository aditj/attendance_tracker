from django.urls import path

from . import views

urlpatterns = [
    path('', views.input, name='input'),
    path('view',views.view,name='view'),
 path('update',views.webhook,name='webhook')
]

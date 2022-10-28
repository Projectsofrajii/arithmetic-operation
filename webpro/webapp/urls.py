from django.urls import path,include
from .import views

urlpatterns = [
    path('add/',views.Arithmeticop.addition,name='add'),
    path('sub/', views.Arithmeticop.subtraction, name='sub'),
    path('mul/', views.Arithmeticop.multiplication, name='mul'),
    path('div/', views.Arithmeticop.division, name='div'),

]
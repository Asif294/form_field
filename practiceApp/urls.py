from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home, name= "homepage"),
    path('about/',views.about, name = "aboutpage"),
    path('djangoform/',views.djangoForm, name= "djangoform")
    

]

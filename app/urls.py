from app import views
from django.urls import path,include

urlpatterns = [
    path('', views.signin, name='signin'),
    path("signup", views.signup, name="signup"),
    path("signin", views.signin, name="signin"),
    path("index", views.index, name="index"),
    path("addchat", views.addchat, name="addchat"),
    path('signout', views.signout, name='signout'),
]
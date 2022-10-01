from django.urls import path
from . import views

urlpatterns = [
    path('post/',views.postPage,name='post'),
    path('',views.homePage,name='home'),
    path('post/<int:pk>/update/',views.postUpdate,name='post-update')
]
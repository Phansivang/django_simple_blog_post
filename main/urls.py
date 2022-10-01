from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('users.urls')),
    path('',include('app.urls')),
    path('login/',user_views.LoginView.as_view(template_name='users/login.html'),name='login',),
    path('logout/',user_views.LogoutView.as_view(),name='logout'),
    path('reset_password/',user_views.PasswordChangeView.as_view(template_name='users/profile.html'),name='password')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
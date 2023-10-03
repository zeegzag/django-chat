from django.contrib import admin
from django.urls import path, include

from user.views import signup

urlpatterns = [
    path("chat/", include("chat.urls")),
    path("accounts/", include('django.contrib.auth.urls')),
    path('', include('user.urls')),
    path("admin/", admin.site.urls),
]

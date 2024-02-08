from django.contrib import admin
from django.urls import path
import authentication.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("logout/", authentication.views.logout_user, name="logout"),
]
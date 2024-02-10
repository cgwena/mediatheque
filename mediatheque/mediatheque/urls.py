from django.contrib import admin
from django.urls import path, include
import media, loans, users
from media import urls as media_urls
from loans import urls as loans_urls
from users import urls as users_urls
from authentication import urls as authentication_urls


import authentication.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", authentication.views.user_login, name="login"),
    path("home", media.views.home, name="home"),
    path("media/", include(media_urls)),
    path("loans/", include(loans_urls)),
    path("user/", include(users_urls)),
    path("authentication", include(authentication_urls))
]

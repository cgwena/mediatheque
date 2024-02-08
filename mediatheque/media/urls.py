from django.urls import path
import media.views

urlpatterns = [
    path("home", bibliothecaire.views.home, name="home"),
    path("media/", bibliothecaire.views.media, name="media"),
    path("media_detail/<int:id>", bibliothecaire.views.media_detail, name="media_detail"),
    path("jeu_detail/<int:id>/", bibliothecaire.views.jeu_detail, name="jeu_detail"),
    path("livre/add", bibliothecaire.views.livre_create, name="livre_create"),
    path("dvd_create/", bibliothecaire.views.dvd_create, name="dvd_create"),
    path("cd_create/", bibliothecaire.views.cd_create, name="cd_create"),
    path("jeu_create/", bibliothecaire.views.jeu_create, name="jeu_create"),
    path("livre_update/<int:id>/", bibliothecaire.views.livre_update, name="livre_update"),
    path("dvd_update/<int:id>/", bibliothecaire.views.dvd_update, name="dvd_update"),
    path("cd_update/<int:id>/", bibliothecaire.views.cd_update, name="cd_update"),
    path("jeu_update/<int:id>/", bibliothecaire.views.jeu_update, name="jeu_update"),
    path("livre_delete/<int:id>/", bibliothecaire.views.livre_delete, name="livre_delete"),
    path("dvd_delete/<int:id>/", bibliothecaire.views.dvd_delete, name="dvd_delete"),
    path("cd_delete/<int:id>/", bibliothecaire.views.cd_delete, name="cd_delete"),
    path("jeu_delete/<int:id>/", bibliothecaire.views.jeu_delete, name="jeu_delete"),
]
from django.urls import path
import media.views

urlpatterns = [
    
    path("media/", media.views.media, name="media"),
    path("detail/<int:id>", media.views.media_detail, name="media_detail"),
    path("jeu_detail/<int:id>/", media.views.jeu_detail, name="jeu_detail"),
    path("livrecreate", media.views.livre_create, name="livre_create"),
    path("dvd_create/", media.views.dvd_create, name="dvd_create"),
    path("cd_create/", media.views.cd_create, name="cd_create"),
    path("jeu_create/", media.views.jeu_create, name="jeu_create"),
    path("livre_update/<int:id>/", media.views.media_update, name="media_update"),
    path("jeu_update/<int:id>/", media.views.jeu_update, name="jeu_update"),
    path("media_delete/<int:id>/", media.views.media_delete, name="media_delete"),
    path("jeu_delete/<int:id>/", media.views.jeu_delete, name="jeu_delete"),
]
from django.contrib import admin

from media.models import Livre, Dvd, Cd, JeuDePlateau, Media
from users.models import User
from loans.models import Loan


class LivreAdmin(admin.ModelAdmin):
    list_display = ("name", "auteur")


class UserAdmin(admin.ModelAdmin):
    list_display = ("username",)


class MediaAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(User, UserAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(Livre, LivreAdmin)
admin.site.register(Dvd)
admin.site.register(Cd)
admin.site.register(JeuDePlateau)
admin.site.register(Loan)

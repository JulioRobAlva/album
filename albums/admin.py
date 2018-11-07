from django.contrib import admin
from albums.models import Artista, ArtistaAdmin, Album, AlbumAdmin, Cancion

admin.site.register(Artista, ArtistaAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Cancion)
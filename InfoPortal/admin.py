from django.contrib import admin
from . import models
#from django_markdown.admin import MarkdownModelAdmin

class EntryAdmin(admin.ModelAdmin):
    list_display = ("title" , "created","author")
    prepopulated_fields = {"slug" : ("title", )}

admin.site.register(models.Entry, EntryAdmin)

class SagarPostAdmin(admin.ModelAdmin):
    list_display = ("title" , "created","author")
    prepopulated_fields = {"slug" : ("title", )}
	
admin.site.register(models.SagarPost, SagarPostAdmin)

class HimgiriPostAdmin(admin.ModelAdmin):
    list_display = ("title" , "created","author")
    prepopulated_fields = {"slug" : ("title", )}
	
admin.site.register(models.HimgiriPost, HimgiriPostAdmin)

class VasundharaPostAdmin(admin.ModelAdmin):
    list_display = ("title" , "created","author")
    prepopulated_fields = {"slug" : ("title", )}
	
admin.site.register(models.VasundharaPost, VasundharaPostAdmin)

class SrishtiPostAdmin(admin.ModelAdmin):
    list_display = ("title" , "created","author")
    prepopulated_fields = {"slug" : ("title", )}
	
admin.site.register(models.SrishtiPost, SrishtiPostAdmin)


class MunSocPostAdmin(admin.ModelAdmin):
    list_display = ("title" , "created","author")
    prepopulated_fields = {"slug" : ("title", )}
	
admin.site.register(models.MunSocPost, MunSocPostAdmin)


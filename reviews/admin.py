from django.contrib import admin

# Register your models here.
from . import models

@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):

    """ Review Admin Definition """
    list_display = ("__str__", "rating_average")

from django.contrib import admin
from . import models

admin.site.site_header = "Michael's Portfolio"
# Register your models here.
admin.site.register(models.Project)
admin.site.register(models.Achievement)


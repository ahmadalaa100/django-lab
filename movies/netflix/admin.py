from django.contrib import admin
from .models import movie,country,rate, category
# Register your models here.


class MovieInline(admin.StackedInline):
    model = movie
    extra = 4
    max_num = 10



class CoutnryAdmin(admin.ModelAdmin):
    inlines = [MovieInline]



class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "overview", "year")
    # list_filter = ("year",)

admin.site.register(movie, MovieAdmin)

admin.site.register(country, CoutnryAdmin)
admin.site.register(rate)
admin.site.register(category)
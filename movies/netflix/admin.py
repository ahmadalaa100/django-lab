from django.contrib import admin
from .models import movie,category,country,rate

# Register your models here.
class MovieInline(admin.TabularInline):
    model = movie
    extra = 1 
    max_num = 10


class CountryAdmin(admin.ModelAdmin):
    inlines = [MovieInline]



class MovieAdmin(admin.ModelAdmin):
    list_display=('title','overview','year')
    list_filter=('year')



admin.site.register(movie,MovieAdmin)
admin.site.register(category)
admin.site.register(country,CountryAdmin)
admin.site.register(rate)
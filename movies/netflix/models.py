from django.db import models

# Create your models here.

class category(models.model):
    name = models.CharField(max_length=50,null=True)


    def __str__(self):
        return str(self.name)

class country(models.model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return str(self.name)


class rate(models.Model):
    rate = models.IntegerField(null=True,blank=True)
    def __str__(self):
        return str(self.rate)



class movie(models.model):
    title = models.CharField(max_length=100),
    overview = models.TextField(max_length=500),
    year = models.DateField(),
    poster = models.ImageField(upload_to="movies/posters"),
    video = models.FileField(upload_to="movies/video"),
    categories= models.ManyToManyField(category),
    country = models.ForeignKey(country,null=True,on_delete=models.SET_NULL)
    rate = models.OneToOneField(rate,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.name)



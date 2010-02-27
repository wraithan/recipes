from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.name

class Ingredient(models.Model):
    data = models.CharField(max_length=255)
    optional = models.BooleanField()

    def __unicode__(self):
        return self.data

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    submitter = models.ForeignKey(User)
    author = models.CharField(max_length=50)
    ingredients = models.ManyToManyField(Ingredient)
    instructions = models.TextField()
    min_time = models.PositiveIntegerField()
    max_time = models.PositiveIntegerField()
    categories = models.ManyToManyField(Category)
    slug = models.SlugField(editable=False)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)

        super(test, self).save(*args, **kwargs)

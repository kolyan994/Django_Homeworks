from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    image = models.CharField(max_length=255)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_slug(self.name)
        super().save(*args, **kwargs)


def generate_slug(name):
    return slugify(name)


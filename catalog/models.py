from django.db import models

from .enums import CategoryEnum


class Catalog(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.IntegerField(choices=CategoryEnum.choices, default=CategoryEnum.SERVICE)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to="catalogs", blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Catalogs"
        ordering = ["-is_featured", "-is_popular", "-is_new", "name"]
        get_latest_by = "created_at"

    def __str__(self):
        return self.name

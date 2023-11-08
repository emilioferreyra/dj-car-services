from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save
from django.dispatch import receiver


class UserTimestampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='created_records',
        null=True,
        blank=True
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='updated_records',
        null=True,
        blank=True
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.created_by:
            self.created_by = self.updated_by
        super(UserTimestampMixin, self).save(*args, **kwargs)


@receiver(pre_save)
def set_updated_by(sender, instance, **kwargs):
    if hasattr(instance, 'created_by') and hasattr(instance, 'updated_by'):
        instance.updated_by = instance.created_by

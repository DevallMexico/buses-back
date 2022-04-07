from django.db import models
from django.contrib.auth.models import User


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserProfile(TimeStampedModel):
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name="profile")
    phone = models.CharField(null=True, max_length=15)

    def __str__(self):
        return self.user.get_full_name() or str(self.pk)



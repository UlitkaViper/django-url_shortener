from django.db import models

# Create your models here.


class URL(models.Model):
    full_url = models.URLField()
    short_url = models.URLField()
    time_created = models.DateTimeField(auto_now_add=True)
    used_count = models.IntegerField(default=0)

    def __str__(self):
        return self.full_url

    class Meta:
        verbose_name = 'Ссылки'
        verbose_name_plural = 'Ссылка'

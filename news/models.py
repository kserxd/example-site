from django.db import models


class Articles(models.Model):
    title = models.CharField('Name', max_length=50)
    anons = models.CharField('Annons', max_length=250)
    full_text = models.TextField('Article')
    date = models.DateTimeField('Data and time')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/news/{self.id}"

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

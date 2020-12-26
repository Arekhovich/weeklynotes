from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from slugify import slugify




class Note(models.Model):
    class Meta:
        ordering = ['date']
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, primary_key=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    text = models.TextField(max_length=200, null=True, verbose_name='Описание')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='main_notes')

    def __str__(self):
        return f"{self.title}"

    def save(self, **kwargs):
        if self.slug == "":
            self.slug = slugify(self.title)
        try:
            super().save(**kwargs)
        except:
            self.slug += str(self.date)
            super().save(**kwargs)

    def get_absolute_url(self):
        return reverse('note-detail', args=[self.slug])


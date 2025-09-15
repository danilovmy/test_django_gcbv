from django.db import models

# Create your models here.

class Comment(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()

    def get_absolute_url(self):
        return f'/{self.pk}'
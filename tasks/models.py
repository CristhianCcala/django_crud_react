from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    done = models.BooleanField(default=False)
    def __str__(self):
        tex = "{0} [{1}] ({2})"
        return tex.format(self.title, self.description, self.done)
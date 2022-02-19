from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=128)
    complete = models.BooleanField(default=False)
    modified_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete', '-modified_on']


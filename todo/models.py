from django.db import models


class ToDo(models.Model):
    action = models.TextField(max_length=100)
    done = models.BooleanField()

    def save(self, **kwargs):
        if self.done is None:
            self.done = False
        super().save()

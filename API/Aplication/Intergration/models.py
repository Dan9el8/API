from django.db import models

class UseModel(models.Model):
    client_ip = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    greetings = models.CharField(max_length=200)

    def __str__(self):
        return self.title
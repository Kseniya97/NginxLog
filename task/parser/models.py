from django.db import models


class LogModel(models.Model):
    ip_adress = models.GenericIPAddressField()
    data = models.DateTimeField()
    http_method = models.CharField(max_length=200)
    URI_request = models.URLField()
    code_answer = models.IntegerField()
    size_answer = models.IntegerField()

    def __str__(self):
        return self.ip_adress

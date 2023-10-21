from django.db import models


class Journal(models.Model):
    posted_at = models.DateTimeField(auto_now_add=True)
    source_ip = models.CharField(max_length=100)
    input_data = models.CharField(max_length=100)
    checking_results = models.BooleanField()

from django.db import models

class Ad(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    price = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    category_name = models.CharField(max_length=255, null=True, blank=True)
    images_url =  models.TextField()
    phone_number =  models.CharField(max_length=255, null=True, blank=True)
    user =  models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

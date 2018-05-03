from django.db import models

class userprofile(models.Model):
    userid=models.integetrField(primary_key=True)
    username=models.charField(max_length=20)
    password=models.charField(max_length=20)
    email=models.EmailField()


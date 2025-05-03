from django.db import models

class Form(models.Model):
    assignment=models.TextField()
    work=models.TextField()

from django.db import models

# Create your models here.
class details(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='pictures')
    desc = models.TextField()

    def __str__(self):
        return self.name

class team(models.Model):
    teamname = models.CharField(max_length=250)
    pic = models.ImageField(upload_to='pictures')
    desciption = models.TextField()

    def __str__(self):
        return self.teamname

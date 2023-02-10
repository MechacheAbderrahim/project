from django.db import models

# Create your models here.
class Progression(models.Model):
    enseigant = models.CharField(max_length=40)
    module = models.CharField(max_length=40)
    email_en = models.CharField(max_length=100)
    intitulé = models.CharField(max_length=100, default='Module namme')
    prog = models.IntegerField()
    description = models.TextField()

    def __str__(self) :
        return str(self.module) +" " + str(self.prog)+" " + str(self.enseigant)
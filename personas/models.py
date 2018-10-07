from django.db import models

# Create your models here.

class Persona(models.Model):
    legajo = models.IntegerField()
    nombre = models.CharField(max_length=50)
    CUIT = models.CharField(primary_key=True,max_length=11)

    def __str__(self):
        def formatear_cuit(cuit):
            return "{}-{}-{}".format(cuit[:2],cuit[2:10], cuit[10:])

        return "{} - {} - {}".format(formatear_cuit(self.CUIT), self.legajo, self.nombre)
        
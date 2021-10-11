from django.db import models


# Create your models here.

class Alumno(models.Model):
    apellidoPaterno = models.CharField(max_length=35)
    apellidoMaterno = models.CharField(max_length=35)
    Nombres = models.CharField(max_length=50)
    DNI = models.CharField(max_length=10)
    FechaNacimiento = models.DateField()
    sexos = [
        ("F", "Femenino"),
        ("M", "Masculino")
    ]
    sexo = models.CharField(max_length=1, choices=sexos, default="M")

    def NombreCompleto(self):
        cadena = "{0} {1}, {2}"
        return cadena.format(self.apellidoPaterno, self.apellidoMaterno, self.Nombres)

    def __str__(self):
        return self.NombreCompleto()

from django.db import models


class PagosARS(models.Model):
    cedula = models.PositiveIntegerField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)

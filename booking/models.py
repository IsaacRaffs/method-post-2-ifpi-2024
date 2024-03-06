from django.db import models

# Create your models here.

class Lote(models.Model):
    area = models.PositiveIntegerField(null=False, blank=False, default=0)
    valor = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    localizacao = models.CharField(max_length=250, null=False, blank=False)

    def __str__(self) -> str:
        return f'Area: {self.area} | Valor: {self.valor} | Localização: {self.localizacao}'
        
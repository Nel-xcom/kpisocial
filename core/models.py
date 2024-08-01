from django.db import models

# MODELOS DE DATOS CAJA, EXPERTAS, COORDINACION, TRADE, OS Y STOCK
class cajaKpi(models.Model):
    FARMACIA_CHOICES = [(f'FS{i:02d}', f'FS{i:02d}') for i in range(1, 26)]
    TAREA_CHOICES = [
        ('Nota de credito', 'Nota de crédito'),
        ('Anulacion de temporales', 'Anulación de temporales'),
        ('Ecommerce Entrega', 'Ecommerce Entrega'),
        ('Ecommerce retirado', 'Ecommerce retirado'),
        ('Consumidor final', 'Consumidor final'),
        ('999999', '999999'),
        ('Diferencia de caja', 'Diferencia de caja')
    ]
    GESTIONADO_CHOICES = [
        ('Si', 'Sí'),
        ('No', 'No')
    ]

    farmacia = models.CharField(max_length=5, choices=FARMACIA_CHOICES)
    legajo = models.PositiveIntegerField()
    tarea = models.CharField(max_length=50, choices=TAREA_CHOICES)
    fecha = models.DateField()
    cantidad = models.PositiveIntegerField()
    gestionado = models.CharField(max_length=2, choices=GESTIONADO_CHOICES)

    def __str__(self):
        return f'{self.farmacia} - {self.legajo} - {self.tarea}'
   

class stockKpi(models.Model):
    FARMACIA_CHOICES = [(f'FS{i:02d}', f'FS{i:02d}') for i in range(1, 26)]
    TAREA_CHOICES = [
        ('Recepcion (tiempo)', 'Recepcion (tiempo)'),
        ('Compras(drog externa)', 'Compras(drog externa)'),
        ('Ajuste de stock', 'Ajuste de stock'),
        ('Negativos', 'Negativos'),
        ('Ecom cambio deestado', 'Ecom cambio de estado'),
        ('Revision GPS', 'Revision GPS'),
        ('Pedidos pendientes', 'Pedidos pendientes'),
        ('Vales', 'Vales')
    ]
    GESTIONADO_CHOICES = [
        ('Si', 'Sí'),
        ('No', 'No')
    ]

    farmacia = models.CharField(max_length=5, choices=FARMACIA_CHOICES)
    legajo = models.PositiveIntegerField()
    tarea = models.CharField(max_length=50, choices=TAREA_CHOICES)
    fecha = models.DateField()
    cantidad = models.PositiveIntegerField()
    gestionado = models.CharField(max_length=2, choices=GESTIONADO_CHOICES)

    def __str__(self):
        return f'{self.farmacia} - {self.legajo} - {self.tarea}'
    

class expertasKpi(models.Model):
    FARMACIA_CHOICES = [(f'FS{i:02d}', f'FS{i:02d}') for i in range(1, 26)]
    TAREA_CHOICES = [
        ('Vencidos', 'Vencidos'),
        ('Blotters', 'Blotters'),
        ('Ofertas', 'Ofertas'),
        ('Orden y limpieza', 'Orden y limpieza')
    ]
    GESTIONADO_CHOICES = [
        ('Si', 'Sí'),
        ('No', 'No')
    ]

    farmacia = models.CharField(max_length=5, choices=FARMACIA_CHOICES)
    legajo = models.PositiveIntegerField()
    tarea = models.CharField(max_length=50, choices=TAREA_CHOICES)
    fecha = models.DateField()
    cantidad = models.PositiveIntegerField()
    gestionado = models.CharField(max_length=2, choices=GESTIONADO_CHOICES)

    def __str__(self):
        return f'{self.farmacia} - {self.legajo} - {self.tarea}'
    

class tradeKpi(models.Model):
    FARMACIA_CHOICES = [(f'FS{i:02d}', f'FS{i:02d}') for i in range(1, 26)]
    TAREA_CHOICES = [
        ('Vencimientos', 'Vencimientos'),
        ('Señalizacion', 'Señalizacion'),
        ('Descuentos', 'Descuentos'),
        ('Mercaderia a disposicion', 'Mercaderia a disposicion'),
        ('Actualizacion', 'Actualizacion')
    ]
    GESTIONADO_CHOICES = [
        ('Si', 'Sí'),
        ('No', 'No')
    ]

    farmacia = models.CharField(max_length=5, choices=FARMACIA_CHOICES)
    legajo = models.PositiveIntegerField()
    tarea = models.CharField(max_length=50, choices=TAREA_CHOICES)
    fecha = models.DateField()
    cantidad = models.PositiveIntegerField()
    gestionado = models.CharField(max_length=2, choices=GESTIONADO_CHOICES)

    def __str__(self):
        return f'{self.farmacia} - {self.legajo} - {self.tarea}'


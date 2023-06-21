from django.db import models


class Car(models.Model):
    COLOR_CHOICES = (
        ('black', 'Negro'),
        ('white', 'Blanco'),
        ('silver', 'Plata'),
        ('gray', 'Gris'),
        ('red', 'Rojo'),
        ('blue', 'Azul'),
        ('green', 'Verde'),
        ('yellow', 'Amarillo'),
        ('orange', 'Naranja'),
        ('brown', 'Marrón'),
        ('purple', 'Morado'),
        ('pink', 'Rosado'),
        ('gold', 'Dorado'),
        ('beige', 'Beige'),
        ('teal', 'Turquesa'),
        ('navy', 'Azul Marino'),
        ('burgundy', 'Burdeos'),
        ('champagne', 'Champán'),
        ('olive', 'Oliva'),
        ('cream', 'Crema'),
    )

    BRAND_CHOICES = (
        ('toyota', 'Toyota'),
        ('ford', 'Ford'),
        ('chevrolet', 'Chevrolet'),
        ('honda', 'Honda'),
        ('fiat', 'Fiat'),
        ('audi', 'Audi'),
        ('bmw', 'BMW'),
        ('mercedes', 'Mercedes-Benz'),
        ('volkswagen', 'Volkswagen'),
        ('nissan', 'Nissan'),
        ('subaru', 'Subaru'),
        ('mazda', 'Mazda'),
        ('hyundai', 'Hyundai'),
        ('kia', 'Kia'),
        ('volvo', 'Volvo'),
        ('jaguar', 'Jaguar'),
        ('landrover', 'Land Rover'),
        ('porsche', 'Porsche'),
        ('lexus', 'Lexus'),
        ('cadillac', 'Cadillac'),
    )

    main_color = models.CharField(max_length=50,choices=COLOR_CHOICES)
    model = models.CharField(max_length=100)
    brand = models.CharField(max_length=50, choices=BRAND_CHOICES)
    value = models.IntegerField()
    production_costs = models.IntegerField()
    transportation_costs = models.IntegerField()

    @property
    def total(self):
        return self.production_costs + self.transportation_costs

    def __str__(self):
        return f'{self.brand} {self.model}'

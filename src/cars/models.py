from django.db import models


class Car(models.Model):
    COLOR_CHOICES = (
        ('black', 'Black'),
        ('white', 'White'),
        ('silver', 'Silver'),
        ('gray', 'Gray'),
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('yellow', 'Yellow'),
        ('orange', 'Orange'),
        ('brown', 'Brown'),
        ('purple', 'Purple'),
        ('pink', 'Pink'),
        ('gold', 'Gold'),
        ('beige', 'Beige'),
        ('teal', 'Teal'),
        ('navy', 'Navy'),
        ('burgundy', 'Burgundy'),
        ('champagne', 'Champagne'),
        ('olive', 'Olive'),
        ('cream', 'Cream'),
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

    id = models.AutoField(primary_key=True)
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
        return f'{self.id} {self.brand} {self.model}'

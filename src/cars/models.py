from django.db import models


class Car(models.Model):
    MODEL_CHOICES = (
        ('sedan', 'Sedan'),
        ('suv', 'SUV'),
        ('hatchback', 'Hatchback'),
    )

    BRAND_CHOICES = (
        ('toyota', 'Toyota'),
        ('ford', 'Ford'),
        ('chevrolet', 'Chevrolet'),
        ('honda', 'Honda'),
    )

    main_color = models.CharField(max_length=50)
    model = models.CharField(max_length=50, choices=MODEL_CHOICES)
    brand = models.CharField(max_length=50, choices=BRAND_CHOICES)
    value = models.IntegerField()
    production_costs = models.IntegerField()
    transportation_costs = models.IntegerField()

    @property
    def total(self):
        return self.production_costs + self.transportation_costs

    def __str__(self):
        return f'{self.brand} {self.model}'

from django.db import models

class Flight(models.Model):
    NACIONAL = 'Nacional'
    INTERNACIONAL = 'Internacional'
    FLIGHT_TYPES = [
        (NACIONAL, 'Nacional'),
        (INTERNACIONAL, 'Internacional'),
    ]

    name = models.CharField(max_length=100)
    flight_type = models.CharField(max_length=15, choices=FLIGHT_TYPES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
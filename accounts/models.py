from django.db import models

from django.contrib.auth.hashers import make_password, check_password

class AgriUser(models.Model):
    STATUS_CHOICES = [
        ('farmer', 'Farmer'),
        ('labor', 'Labor'),
    ]

    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile_no = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=128)  # This will store the hashed password
    address = models.TextField()
    status = models.CharField(max_length=6, choices=STATUS_CHOICES)
    amount_of_land = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.full_name

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Material(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=20)  # тонна, м3, кг и т.д.
    image = models.ImageField(upload_to='materials/', blank=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.price}/{self.unit})"

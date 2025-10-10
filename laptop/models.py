from django.db import models

class Laptop(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    price_per_day = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='laptops/', null=True, blank=True)  # field gambar

    def price_formatted(self):
        return "{:,.0f}".format(self.price_per_day).replace(",", ".")

    def __str__(self):
        return f"{self.brand} {self.name}"

class Booking(models.Model):
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    customer_address = models.TextField()
    rental_date = models.DateField()
    location_pin = models.CharField(max_length=20)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Booking {self.customer_name} - {self.laptop}"

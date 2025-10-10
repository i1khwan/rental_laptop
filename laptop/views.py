from django.shortcuts import render, get_object_or_404, redirect
from .models import Laptop, Booking
from django.http import HttpResponse

# Halaman utama
def home(request):
    return render(request, 'laptop/home.html')

# Daftar semua laptop
def laptop_list(request):
    laptops = Laptop.objects.all()
    return render(request, 'laptop/laptop_list.html', {'laptops': laptops})

# Halaman booking laptop
def booking(request, laptop_id):
    laptop = get_object_or_404(Laptop, id=laptop_id)
    
    if request.method == "POST":
        customer_name = request.POST.get("customer_name")
        customer_address = request.POST.get("customer_address")
        rental_date = request.POST.get("rental_date")
        location_pin = request.POST.get("location_pin")

        Booking.objects.create(
            laptop=laptop,
            customer_name=customer_name,
            customer_address=customer_address,
            rental_date=rental_date,
            location_pin=location_pin,
        )
        return HttpResponse("Booking berhasil! Menunggu persetujuan admin.")
    
    return render(request, 'laptop/booking.html', {'laptop': laptop})

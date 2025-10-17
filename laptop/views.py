from django.shortcuts import render, get_object_or_404, redirect
from .models import Laptop, Booking
from django.http import HttpResponse
from .forms import BookingForm
from django.contrib import messages


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

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.laptop = laptop
            booking.save()

            # Tambahkan pesan sukses
            messages.success(request, f"Pemesanan laptop {laptop.name} berhasil!")

            # Tidak redirect, tetap di halaman yang sama
            form = BookingForm()  # kosongkan form setelah submit
    else:
        form = BookingForm()

    return render(request, 'laptop/booking.html', {'form': form, 'laptop': laptop})


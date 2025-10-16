1. Buat folder baru. Contoh: ***mkdir project***
2. Masuk ke folder project. ***cd project/***
3. Clone repositori ini. ***git clone https://github.com/i1khwan/rental_laptop.git***
4. Masuk ke folder rental_laptop. ***cd rental_laptop***
5. Aktifkan virtual environment. ***source myenv/bin/activate***
6. Install paket yang diperlukan. ***pip install -r requirements.txt***
7. Cek file setting.py. Buat tabel rental_laptop pada mysql. Sesuaikan user, password, dan port database.
   Lokasi file: rental_laptop/rental_laptop/settings.py
8. Buat migrasi. ***python manage.py makemigrations***
9. Migrasi ke database. ***python manage.py migrate***
10. Jalankan server. ***python manage.py runserver***

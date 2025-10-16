1. Buat folder baru. Contoh: ***mkdir project***
2. Masuk ke folder project. ***cd project/***
3. Clone repositori ini. ***git clone https://github.com/i1khwan/rental_laptop.git***
4. Cek file setting.py. Buat tabel rental_laptop pada mysql. Sesuaikan user, password, dan port database.
   Lokasi file: rental_laptop/rental_laptop/settings.py
5. Buat migrasi. ***python manage.py makemigrations***
6. Migrasi ke database. ***python manage.py migrate***
7. Aktifkan virtual environment. ***source myenv/bin/activate***
8. Install paket yang diperlukan. ***pip install -r requirements.txt***
9. Jalankan server. ***python manage.py runserver***

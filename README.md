🎓 LMS-SPADA Course Scraper

Script Python sederhana berbasis BeautifulSoup dan Requests untuk melakukan pemetaan (mapping) serta pengumpulan data judul mata kuliah secara otomatis dari platform LMS-SPADA Indonesia berdasarkan rentang Course ID.

Dibuat untuk membantu eksplorasi materi perkuliahan secara efisien tanpa harus mengubah URL parameter secara manual satu per satu.

🚀 Fitur Utama

Automatic Range Scraper: Mengambil data course berdasarkan rentang ID (contoh: ID 4435 – 4467).

Graceful Delay (time.sleep): Menerapkan jeda waktu pada setiap request agar tidak membebani server target dan tetap mematuhi etika web scraping.

Export to CSV: Menyimpan daftar hasil scraping secara otomatis ke dalam file .csv.

Google Colab Friendly: Dapat langsung dijalankan di Google Colab tanpa konfigurasi environment lokal yang rumit.

🛠️ Prasyarat & Instalasi

Pastikan kamu sudah menginstal library berikut jika dijalankan di environment lokal:

pip install beautifulsoup4 requests pandas


Jika menggunakan Google Colab, library tersebut umumnya sudah tersedia secara bawaan.

📖 Cara Penggunaan

Buka file notebook di Google Colab atau jalankan script Python lokal.

Tentukan rentang Course ID yang ingin di-scrap pada bagian looping:

for course_id in range(4435, 4468):
    # Logika scraping


Jalankan script. Hasil rekapitulasi akan langsung ditampilkan dalam bentuk tabel dan otomatis mengunduh file lms_spada_courses.csv.

⚠️ Disclaimer & Etika penggunaan

Educational Purpose: Project ini dibuat murni untuk tujuan pembelajaran teknis (web scraping, data parsing) serta efisiensi navigasi materi perkuliahan pribadi.

Rate Limiting: Script ini sengaja dilengkapi dengan penundaan waktu (time.sleep(1)) untuk menghormati kapasitas server LMS-SPADA dan mencegah tingkah laku menyerupai bot spam.

Privacy & Copyright: Repositori ini hanya berisi kode program (logika scrapper). Tidak ada data sensitif, kredensial pengguna, maupun file materi berhak cipta yang disimpan di dalam repositori ini.

📄 Lisensi

Proyek ini berada di bawah lisensi MIT License.

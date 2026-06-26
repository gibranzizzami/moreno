import os
import time
import requests

# Konfigurasi
START_ID = 7684
END_ID = 75000  
DOWNLOAD_DIR = "biblios"
DELAY_SECONDS = 2  # Jeda waktu

# Membuat folder penyimpanan
if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

print("Memulai pengunduhan buku...\n")

for book_id in range(START_ID, END_ID + 1):
    # Menggunakan URL alternatif teks UTF-8 yang stabil
    url = f"https://www.gutenberg.org/ebooks/{book_id}.txt.utf-8"
    filename = os.path.join(DOWNLOAD_DIR, f"book_{book_id}.txt")
    
    print(f"Mencoba mengunduh Buku ID {book_id}...")
    
    try:
        # Menambahkan User-Agent agar terlihat seperti browser biasa
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        
        # Jika status 200 artinya buku ditemukan dan berhasil diakses
        if response.status_code == 200:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(response.text)
            print(f"Sukses! Disimpan sebagai {filename}")
        elif response.status_code == 404:
            print(f"Buku ID {book_id} tidak ditemukan (404).")
        else:
            print(f"Gagal mengunduh ID {book_id}. Status code: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"Terjadi eror koneksi pada ID {book_id}: {e}")
    
    # Jeda waktu
    time.sleep(DELAY_SECONDS)

print("\nProses selesai!")
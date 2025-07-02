Berikut adalah isi file `README.md` untuk menjelaskan dan memandu penggunaan kode Modul A (Objek 2D) menggunakan PyOpenGL:

---

# 📐 Modul A - Objek 2D Interaktif dengan PyOpenGL

Tugas Besar UAS Grafika Komputer
**Topik:** Pengembangan Aplikasi Grafika 2D dan 3D Interaktif menggunakan **PyOpenGL**
**Modul A:** Objek 2D

---

## 🧩 Fitur Utama

Aplikasi ini memungkinkan pengguna untuk menggambar objek-objek 2D dasar secara interaktif menggunakan **mouse dan keyboard** di atas canvas OpenGL:

### ✅ Objek yang Dapat Digambar

* Titik (Point)
* Garis (Line)
* Persegi / Persegi Panjang (Rectangle)
* Elips (Ellipse)

### 🎨 Pengaturan Tambahan

* Pemilihan warna objek menggunakan tombol keyboard:

  * `R` → Merah
  * `G` → Hijau
  * `B` → Biru
* Pengaturan ketebalan garis:

  * `+` → Menambah ketebalan
  * `-` → Mengurangi ketebalan

### 🖱️ Kontrol Input

* **Klik kiri mouse (drag)**: menggambar objek dari titik awal ke titik akhir.
* **Tombol angka**:

  * `1` → Mode Titik
  * `2` → Mode Garis
  * `3` → Mode Persegi
  * `4` → Mode Elips

---

## 💻 Cara Menjalankan

### 1. Instalasi Dependensi

Pastikan Python 3 sudah terpasang, lalu instal pustaka yang dibutuhkan:

```bash
pip install PyOpenGL PyOpenGL_accelerate
```

### 2. Jalankan Program

```bash
python nama_file.py
```

*(Ganti `nama_file.py` dengan nama file Python Anda)*

---

## 🛠 Struktur Kode Utama

* `screen_to_gl(x, y)`
  Konversi koordinat mouse ke koordinat OpenGL (viewport).

* `mouse_func()`
  Menangani klik mouse untuk menentukan koordinat awal dan akhir objek.

* `keyboard_func()`
  Menangani input keyboard untuk mode gambar, warna, dan ketebalan.

* `display()`
  Fungsi utama untuk merender semua objek yang telah digambar.

---

## 🚀 Rencana Pengembangan Selanjutnya

Modul berikutnya dapat ditambahkan:

* Transformasi objek (translasi, rotasi, scaling)
* Windowing dan clipping menggunakan Cohen-Sutherland / Liang-Barsky
* Pembuatan objek 3D (Modul B)

---

## 🧑‍💻 Pengembang

* Tugas Besar UAS - Mata Kuliah **Grafika Komputer**
* Bahasa: **Python**
* Library: **PyOpenGL**, **GLUT**

---

Jika kamu ingin README ini dalam bentuk `.md` file atau disimpan dalam satu folder proyek, beri tahu saya.

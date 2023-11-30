# Dashboard Analisis Penyewaan Sepeda

Dashboard interaktif ini dibuat menggunakan Streamlit untuk analisis data penyewaan sepeda. Dashboard ini memungkinkan pengguna untuk melihat ringkasan data, visualisasi, dan analisis tren penyewaan sepeda berdasarkan berbagai faktor seperti waktu, cuaca, dan musim.


## URL streamlit cloud
```
https://dashboardsepeda-aku.streamlit.app/
```

![Dashboard Snapshot]([https://example.com/image.jpg](https://github.com/msfauzan/dashboard_sepeda/blob/main/Snapshot%20Dashboard.png?raw=true))


## Cara Menjalankan Dashboard

Untuk menjalankan dashboard ini di lingkungan lokal Anda, ikuti langkah-langkah di bawah ini:

### Prasyarat

Pastikan Anda telah menginstal Python di komputer Anda. Anda juga perlu menginstal beberapa paket Python tambahan untuk menjalankan dashboard ini. Berikut adalah perintah untuk menginstal semua paket yang diperlukan:

```
pip install streamlit pandas seaborn matplotlib plotly
```

### Langkah-langkah untuk Menjalankan

1. **Klon Repositori**: Pertama, klon repositori GitHub ini ke komputer lokal Anda menggunakan:

```
git clone https://github.com/msfauzan/dashboard_sepeda.git
```

2. **Buka Terminal**: Buka terminal atau command prompt di komputer Anda.

3. **Navigasi ke Direktori Proyek**: Ganti direktori ke folder tempat Anda menyimpan skrip dashboard:

```
cd path/to/dashboard
```

4. **Jalankan Aplikasi Streamlit**: Jalankan aplikasi Streamlit dengan perintah berikut:

```
streamlit run dashboard.py
```

5. **Buka Dashboard di Browser**: Setelah menjalankan, Streamlit akan membuka dashboard di browser web Anda secara otomatis.

## Fitur Dashboard

Dashboard ini menyediakan fitur-fitur berikut:

- Pilihan untuk memilih tipe data (harian atau jam-jaman).
- Pilihan untuk memilih variabel yang dianalisis.
- Filter data berdasarkan tanggal atau jam.
- Visualisasi data interaktif.
- Tampilan heatmap korelasi.
- Ringkasan statistik data.

## Kontribusi

Kontribusi untuk pengembangan dashboard ini sangat dihargai. Jika Anda ingin berkontribusi, silakan fork repositori ini, buat perubahan Anda, dan kirimkan pull request.

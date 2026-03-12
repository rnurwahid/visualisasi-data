# Materi 3: Eksplorasi dan Visualisasi Data dengan Python

Repositori ini berisi hasil pengerjaan modul **Eksplorasi dan Visualisasi Data** menggunakan Python.

---

## Struktur File

```
.
├── Hello.py                        # Modul 1: Hello World
├── HelloText.py                    # Modul 2: Variabel & String
├── HelloNumber.py                  # Modul 2: Variabel Number & Operasi Matematika
├── HelloList.py                    # Modul 2: List, Set, Sorting
├── LoadFilePandas.py               # Modul 3: Membaca data dengan Pandas
├── Latihan_Visualisasi_Tips.py     # Modul 4 LATIHAN: Visualisasi Dataset Tips
├── Visualisasi_ECommerce.py        # TUGAS 2: Visualisasi Dataset E-Commerce
└── tips.csv                        # Dataset Tips (dari modul)
```

---

## Penjelasan per Modul

### Modul 1 – Hello World (`Hello.py`)
Program pertama dengan Python menggunakan fungsi `print()`.

### Modul 2 – Sintaks Python
- **HelloText.py**: Mendefinisikan variabel string, assignment, dan operasi string.
- **HelloNumber.py**: Operasi aritmatika, pembagian floor, modulo, dan pembulatan.
- **HelloList.py**: List, Set, pengurutan ascending/descending, `min()`, `max()`, `count()`.

### Modul 3 – Membaca Data (`LoadFilePandas.py`)
Menggunakan library **Pandas** untuk:
- Membaca file CSV dengan `pd.read_csv()`
- Menampilkan 10 baris pertama dengan `.head(10)`
- Menampilkan info dan statistik deskriptif dataset

### Modul 4 – Visualisasi Data (Latihan)

**File:** `Latihan_Visualisasi_Tips.py`  
**Dataset:** `tips.csv` — data tips di restoran

#### Jawaban Latihan:
> *Tampilkan visualisasi sebaran laki-laki dan perempuan (dengan persentase) yang memberikan tips pada restoran*

Visualisasi yang dibuat:
1. **Pie Chart** — Sebaran gender (%) pemberi tips
2. **Bar Chart** — Rata-rata tip per gender
3. **Grouped Bar Chart** — Jumlah pemberi tips per hari & gender
4. **Scatter Plot** — Total tagihan vs tip (by gender)
5. **Box Plot** — Distribusi tip per hari
6. **Pie Chart** — Sebaran perokok vs non-perokok
7. **Bar Chart** — Total tips per waktu makan

#### Hasil / Insight:
- **70%** pemberi tips adalah **laki-laki**, 30% perempuan
- Rata-rata tip laki-laki **$3.29** vs perempuan **$2.54**
- Hari paling ramai: **Sabtu**
- Waktu terbanyak tips: **Dinner**

---

## Tugas 2 – Dataset Lain: E-Commerce Indonesia

**File:** `Visualisasi_ECommerce.py`  
**Dataset:** Simulasi data transaksi e-commerce Indonesia (500 transaksi, 2024)

### Variabel Dataset:
| Kolom | Keterangan |
|---|---|
| `kategori` | Kategori produk (Elektronik, Fashion, dll) |
| `kota` | Kota asal pembeli |
| `metode_bayar` | Metode pembayaran |
| `bulan` | Bulan transaksi |
| `harga` | Harga satuan (Rp) |
| `qty` | Jumlah pembelian |
| `revenue` | Total pendapatan |
| `rating` | Rating transaksi (1–5) |

### Visualisasi yang dibuat (8 chart):
1. **Bar Chart Horizontal** — Revenue per Kategori
2. **Pie Chart** — Distribusi Metode Pembayaran
3. **Bar Chart** — Revenue per Kota
4. **Line Chart** — Tren Revenue Bulanan
5. **Donut Chart** — Distribusi Quantity Pembelian
6. **Bar Chart Horizontal** — Rating per Kategori
7. **Scatter Plot** — Harga vs Revenue per Kategori
8. **Stacked Bar** — Metode Bayar per Kota

### Insight Utama:
- Kategori **Elektronik** menghasilkan revenue tertinggi (~Rp 822 juta)
- **QRIS** menjadi metode pembayaran paling populer (31.6%)
- **Jakarta** menjadi kota dengan revenue terbesar (~Rp 395 juta)
- Produk **Kecantikan** mendapatkan rating tertinggi (4.16/5.0)

---

## Library yang Digunakan

```bash
pip install pandas matplotlib seaborn
```

| Library | Kegunaan |
|---|---|
| `pandas` | Manipulasi & analisis data |
| `matplotlib` | Visualisasi data |
| `numpy` | Komputasi numerik |

---

## Cara Menjalankan

```bash
# Clone repository
git clone <url-repo>
cd <nama-folder>

# Install dependencies
pip install pandas matplotlib numpy

# Jalankan latihan modul
python Latihan_Visualisasi_Tips.py

# Jalankan visualisasi dataset kedua
python Visualisasi_ECommerce.py
```

---

## Referensi

- https://docs.python.org/3.13/tutorial/index.html
- https://www.dicoding.com/academies/86/tutorials/32963
- https://code.visualstudio.com/docs/python/python-tutorial
- https://www.geeksforgeeks.org/data-visualization-with-python/

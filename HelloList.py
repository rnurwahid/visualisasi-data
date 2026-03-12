# Contoh program untuk menampilkan list pada Python
contoh_list = [1, 3, 3, 5, 5, 5, 7, 7, 9]
print(contoh_list)
print(len(contoh_list))

# Contoh program untuk menampilkan Set pada Python
contoh_list = set([1, 3, 3, 5, 5, 5, 7, 7, 9])
print(contoh_list)
print(len(contoh_list))

# Menampilkan nilai Min dan Max pada list data
angka = [13, 7, 24, 5, 96, 84, 71, 11, 38]
print(min(angka))
print(max(angka))

# Menghitung kemunculan nilai 6 pada list
genap = [2, 4, 4, 6, 6, 6, 8, 10, 10]
print(genap.count(6))

# Mengurutkan nilai pada list secara ascending
kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort()
print(kendaraan)

# Mengurutkan nilai pada list secara descending
kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort(reverse=True)
print(kendaraan)

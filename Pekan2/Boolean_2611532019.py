# Buar file dengan nama Boolean_2611531021
# Nama variabel ditambah 4 digit nim terakhir contoh: nilai_1234
# Deklarasi variabel dengan tipe data Boolean
is_lulus_2019= True

# Menggunakan Boolean
nilai_Fabhian_2019 = 70
nilai_Harland_2019 = 80
batas_lulus_2019 = 75

# Menantukan nilai Boolean dari kondisi
status_kelulusan_Fabhian_2019 = nilai_Fabhian_2019 >= batas_lulus_2019 # Hasilnya akan True
status_kelulusan_Harland_2019 = nilai_Harland_2019 >= batas_lulus_2019

print("=== Check Kelulusan ===")
print("Nilai: ",nilai_Fabhian_2019)
print("Apakah lulus?: ",status_kelulusan_Fabhian_2019)
if status_kelulusan_Fabhian_2019 == True :
    print("Selamat, Fabhian anda lulus!")
else:
    print("Maaf, Fabhian anda tidak lulus")

print("Nilai: ",nilai_Harland_2019)
print("Apakah lulus?: ",status_kelulusan_Harland_2019)
if status_kelulusan_Harland_2019 == True :
    print("Selamat, Harland Anda lulus!")
else:
    print("Maaf, Harland Anda tidak lulus")
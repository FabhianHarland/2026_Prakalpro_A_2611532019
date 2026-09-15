angka1_2019 = int(input("Input angka ke-1 : "))
angka2_2019 = int(input("Input angka ke-2 : "))

#Penjumlahan 
hasil_2019 = angka1_2019 + angka2_2019
print("\nOperator Penjumlahan")
print("Hasil = ",hasil_2019)

#Penjumlahan 
hasil_2019 = angka1_2019 - angka2_2019
print("\nOperator Pengurangan")
print("Hasil = ",hasil_2019)

# Pembagian, pembagian bulat, dan sisa bagi
if angka2_2019 != 0:
    hasil_2019 = angka1_2019 / angka2_2019
    print("\nOperator Pembagian")
    print("Hasil = ",hasil_2019)

    hasil_2019 = angka1_2019 // angka2_2019
    print("\nOperator Pembagian Bulat")
    print("Hasil = ",hasil_2019)

    hasil_2019 = angka1_2019 % angka2_2019
    print("\nOperator Sisa Bagi")
    print("Hasil = ",hasil_2019)
else:
    print("Angka kedua tidak boleh bernilai 0")

# Pangkat
hasil_2019 = angka1_2019*angka2_2019
print("\nOperator Perkalian Bulat")
print("Hasil = ",hasil_2019)


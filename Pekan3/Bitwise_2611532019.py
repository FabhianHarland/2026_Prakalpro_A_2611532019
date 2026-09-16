print("\n===================")
print("3. OPERATOR BITWISE")
print("===================")

angka1_2019 = int(input("Masukkan angka bitwise-1: "))
angka2_2019 = int(input("Masukkan angka bitwise-2: "))

print("\nAngka dalam bentuk desimal dan biner")
print("angka1_2019 =", angka1_2019, "| biner", bin(angka1_2019))
print("angka2_2019 =", angka2_2019, "| biner", bin(angka2_2019))

# Bitwise AND
hasil_2019 = angka1_2019 & angka2_2019
print("\nBitwise AND (&)")
print(angka1_2019, "&", angka2_2019, "=", hasil_2019)
print("Biner hasil =", bin(hasil_2019))
print("Biner hasil (8 bit) =", format(hasil_2019, "08b"))

# Bitwise OR
hasil_2019 = angka1_2019 | angka2_2019
print("\nBitwise OR (|)")
print(angka1_2019, "|", angka2_2019, "=", hasil_2019)
print("Biner hasil =", bin(hasil_2019))
print("Biner hasil (8 bit) =", format(hasil_2019, "08b"))

# Bitwise XOR
hasil_2019 = angka1_2019 ^ angka2_2019
print("\nBitwise XOR (^)")
print(angka1_2019, "^", angka2_2019, "=", hasil_2019)
print("Biner hasil =", bin(hasil_2019))
print("Biner hasil (8 bit) =", format(hasil_2019, "08b"))

# Bitwise NOT
hasil_2019 = ~angka1_2019
print("\nBitwise NOT (~)")
print("~", angka1_2019, "=", hasil_2019)
print("Biner hasil =", bin(hasil_2019))
print("Biner hasil (8 bit) =", format(hasil_2019, "08b"))

# Bitwise geser kiri
jumlah_geser_2019 = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil_2019 = angka1_2019 << jumlah_geser_2019
print("\nBitwise geser kiri (<<)")
print(angka1_2019, "<<", jumlah_geser_2019, "=", hasil_2019)
print("Biner hasil =", bin(hasil_2019))
print("Biner hasil (8 bit) =", format(hasil_2019, "08b"))

# Bitwise geser kanan
hasil_2019 = angka1_2019 >> jumlah_geser_2019
print("\nBitwise geser kanan (>>)")
print(angka1_2019, ">>", jumlah_geser_2019, "=", hasil_2019)
print("Biner hasil =", bin(hasil_2019))
print("Biner hasil (8 bit) =", format(hasil_2019, "08b"))
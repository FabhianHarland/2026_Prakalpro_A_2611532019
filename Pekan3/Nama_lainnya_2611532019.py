print("=========================")
print("1. OPERATOR KEANGGOTAAN")
print("=========================")

#Input beberarpa data yang ingin dipisahkan dengan koma
input_data_2019 = print("Masukkan beberapa angka, pisahkan dengan koma : ")

# Mengubah input menjadi list integer
data_2019 = [int(angka.strip()) for angka in input_data_2019(",")]

nilai_dicari_2019 = int(input("Masukkan angka yang ingin dicari"))

# Operator in
hasil_2019 = nilai_dicari_2019 in data_2019
print("\nOperator keanggotaan IN")
print(nilai_dicari_2019,"in",data_2019,"=",hasil_2019)

#Operator not in
hasil_2019 = nilai_dicari_2019  not in data_2019
print("\nOperator keanggotaan not IN")
print(nilai_dicari_2019,"not in",data_2019,"=",hasil_2019)

print("=========================")
print("2. OPERATOR IDENTITAS")
print("=========================")

# objek1_2019 menggunakan list dari input pengguna
objek1_2019 = data_2019

# objek2_2019 merujuk pada objek yang sama dengan objek1_2019
objek2_2019 = objek1_2019

# objek3_2019 memiliki isi sama, tetapi merupakan objek baru
objek3_2019 = data_2019.copy()

print("objek1_2019 =", objek1_2019)
print("objek2_2019 =", objek2_2019)
print("objek3_2019 =", objek3_2019)

# Operator is
hasil_2019 = objek1_2019 is objek2_2019
print("\nOperator identitas IS")
print("objek1_2019 is objek2_2019 =", hasil_2019)

# Operator is not
hasil_2019 = objek1_2019 is not objek3_2019
print("\nOperator identitas IS NOT")
print("objek1_2019 is not objek3_2019 =", hasil_2019)

# Membandingkan identitas dan nilai
print("\nPerbandingan identitas dan nilai")
print("objek1_2019 is objek3_2019 =", objek1_2019 is objek3_2019)
print("objek1_2019 == objek3_2019 =", objek1_2019 == objek3_2019)

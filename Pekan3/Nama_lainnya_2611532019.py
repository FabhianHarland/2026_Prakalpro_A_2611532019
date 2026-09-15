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

# objek
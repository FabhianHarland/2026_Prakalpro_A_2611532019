domisili_2019 = """
Kampung Dalam, Pauh,
Pasar Baru, Padang,
Sumatera Barat,
Indonesia """

tokenpraktikum_2019 = (20 + 19j)

print("===== SISTEM REGISTRASI PRAKTIKUM ALPRO 2026 =====")
nama_2019 = str(input("Masukkan Nama anda : "))

while True:
    jeniskelamin_2019 = str(input("Masukkan jenis kelamin anda (L/P) : ")).lower()
    if jeniskelamin_2019 in ["l","p"]:
        break
    else :
        print("Hanya masukkan L/P")

umur_2019 = int(input("Masukkan umur anda : "))
skorawal_2019 = float(input("Masukkan skor awal anda : "))

print("\n===== DATA PRAKTIKUM DAN HASIL PEMERIKSAAN =====")
print(f"Nama : {nama_2019} | type class : {type(nama_2019).__name__}")
print(f"Domisili : {domisili_2019} | type class : {type(domisili_2019).__name__}")
print(f"Umur : {umur_2019} | type class : {type(umur_2019).__name__}")
print(f"Skor tes awal : {skorawal_2019} | type class : {type(umur_2019).__name__}")
print(f"ID Token Sinyal : {tokenpraktikum_2019} | type class : {type(tokenpraktikum_2019).__name__}")

print("===== STATUS KELULUSAN PRAKTIKUM =====")
print("Batas minimum nilai : 75") 
if skorawal_2019 >= 75 :
    skorawal_2019 = True
    print(f"Status Kelulusan : {skorawal_2019} | type class : {type(skorawal_2019).__name__}")
else :
    skorawal_2019 = False
    print(f"Status Kelulusan : {skorawal_2019} | type class : {type(skorawal_2019).__name__}")



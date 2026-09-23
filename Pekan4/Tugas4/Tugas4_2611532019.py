#Input data pengguna
print("====SISTEM LOKER WAHANA PRANSMART====")
print("Selamat datang di Wahana Pransmart")
nama_2019 = input("Masukkan nama anda : ")
umur_2019 = int(input("Masukkan umur anda : "))
sim_2019 = input("Apakah anda sudah memiliki Sim? (y/n) : ").strip().lower()
tiket_2019 = int(input("Berapa tiket anda? : "))
member_2019 = input("Apakah anda member? (y/n) : ").strip().lower()

#Untuk check apakah tiket valid atau tidak
if tiket_2019 > 0:
    print("Wahana apa yang ingin anda kunjungi?")
elif tiket_2019 == 0:
    print("Anda tidak memiliki tiket\nSilahkan beli tiket terlebih dahulu")
else :
    print("Masukkan angka yang valid (positif)")

#Wahana yang tersedia
print("\n====DAFTAR WAHANA====\n1. Roller Coaster\n2. Rumah Hantu\n3. Waterboom\n4. Bumper Car\n5. Bianglala\n6. Motor Cross\n7. All access pass (semua wahana)")
paket_wahana_2019 = input("Masukkan nomor wahana yang ingin anda kunjungi : ")

match paket_wahana_2019:
    case "1":
        harga_satuan_2019 = 50000
        print("Anda memilih wahana Roller Coaster | Harga Rp. 50.000")
    case "2":
        harga_satuan_2019 = 30000
        print("Anda memilih wahana Rumah Hantu | Harga Rp. 30.000")
    case "3":
        harga_satuan_2019 = 40000
        print("Anda memilih wahana Waterboom | Harga Rp. 40.000")
    case "4":
        harga_satuan_2019 = 20000
        print("Anda memilih wahana Bumper Car | Harga Rp. 20.000")
    case "5":
        harga_satuan_2019 = 25000
        print("Anda memilih wahana Bianglala | Harga Rp. 25.000")
    case "6":
        harga_satuan_2019 = 50000
        print("Anda memilih wahana Motor Cross | Harga Rp. 50.000")
    case "7":
        harga_satuan_2019 = 150000
        print("Anda memilih All access pass | Harga Rp. 150.000")
    case _:
        print("Wahana yang anda pilih tidak tersedia")

print("\n====KETENTUAN WAHANA====")
#check tinggi badan untuk roller coaster dan bianglala
if paket_wahana_2019 in ["1", "5"]:
    tinggi_2019 = int(input("Masukkan tinggi badan anda (cm) : "))
    if umur_2019 >= 14 and tinggi_2019 > 150 and tinggi_2019 < 200:
        print("Tinggi badan anda memenuhi syarat untuk wahana ini")
    elif umur_2019 >= 14 and tinggi_2019 <= 150:
        print("Tinggi badan anda terlalu pendek untuk masuk ke wahana ini")
    elif umur_2019 >= 14 and tinggi_2019 >= 200:
        print("Tinggi badan anda terlalu tinggi untuk masuk ke wahana ini")
    elif umur_2019 < 14 and tinggi_2019 > 150 and tinggi_2019 < 200:
        print("Umur anda belum cukup untuk masuk ke wahana ini")
    else:
        print("Umur dan tinggi badan anda belum memenuhi syarat untuk masuk ke wahana ini")

#check sim untuk bumper car, motor cross, dan all access pass
if paket_wahana_2019 in ["4","6","7"]:
    if umur_2019 >= 17 and sim_2019 == "y":
        print("Anda sudah dewasa dan memiliki sim, anda boleh mengendarai motor dan mobil di wahana ini")
    elif umur_2019 >= 17 and sim_2019 != "y":
        print("Anda sudah dewasa tetapi tidak memiliki SIM , anda boleh mengendarai motor dan mobil di wahana ini asalkan dengan pendamping/pengawas")
    elif umur_2019 < 17 and sim_2019 == "y":
        print("Anda belum cukup umur untuk memiliki SIM , anda tidak boleh mengendarai motor dan mobil di wahana ini karena identitas anda tidak valid")
    else:
        print("Anda belum cukup umur dan tidak memiliki SIM , anda tidak boleh mengendarai motor dan mobil di wahana ini dimohon untuk memilih wahana lain")
        print("wahana yang dapat anda pilih adalah wahana Roller Coaster, Rumah Hantu, Waterboom, dan Bianglala")

#check umur untuk rumah hantu dan waterboom
if paket_wahana_2019 in ["2","3"]:
    print("Wahana ini memiliki batasan umur minimal 10 tahun")
    if int(umur_2019) >= 10:
        print("Umur anda sudah cukup untuk masuk ke wahana ini")
    else:
        print("Umur anda belum cukup untuk masuk ke wahana ini")

subtotal_2019 = harga_satuan_2019 * tiket_2019

#ketentuan promo
promo_2019 = ["weekend","promo11.11"] #kode promo yang berlaku
print("\n====KETENTUAN PROMO====")
print("1. Weekend       : Diskon 15% untuk pembelian tiket di hari sabtu dan minggu")
print("2. Promo11.11    : Diskon 15% untuk pembelian tiket di tanggal 11 November")
kode_promo_2019 = input("Masukkan kode promo anda (jika ada) : ").strip().lower()

if kode_promo_2019 in promo_2019:
    kode_promo_2019 = True
    print("Kode promo : " + kode_promo_2019 + " | Kode promo anda valid")
else :
    kode_promo_2019 = False
    print("Kode promo anda tidak valid")

#pajak yang berlaku
pajak_2019 = 0.015 

#diskon yang berlaku
diskon_2019 = 0

if subtotal_2019 >= 200000:
    diskon_2019 =+ 0.1

if member_2019 == ["y","iya","ya"]:
    diskon_2019 += 0.05

if tiket_2019 >= 5:
    diskon_2019 += 0.05

if kode_promo_2019 == True:
    diskon_2019 += 0.15

#nominal total
total_diskon_2019 = subtotal_2019 * diskon_2019
pajak_2019 = subtotal_2019 * pajak_2019
total_2019 = subtotal_2019 - total_diskon_2019 + pajak_2019

print("\n====Rincian Pembayaran====")
print(f"Subtotal belanja    : Rp.{subtotal_2019:,}")
print(f"Diskon              : {diskon_2019:.0%} (Rp.{subtotal_2019 * diskon_2019:,})")
print(f"Pajak PPN           : Rp.{pajak_2019:,.0f}")
print(f"Total               : Rp.{subtotal_2019:,} - Rp.{total_diskon_2019:,} + Rp.{pajak_2019:,}\n                    : Rp.{total_2019:,.0f}")
if total_2019 > 300000 :
    print(f"Catatan Layanan     : Terima kasih {nama_2019} telah berkunjung ke Wahana Pransmart, anda mendapatkan souvenir dari kami karena total belanja anda melebihi Rp.300.000")
else :  
    print(f"Catatan Layanan     : Terima kasih {nama_2019} telah berkunjung ke Wahana Pransmart")
print("Program Selesei")

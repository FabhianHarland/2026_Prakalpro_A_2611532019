# ATURAN PENAMAAN VARIABEL & DICTIONARY BARANG
produk_2019 = {
    "1": {"nama": "Sabun", "harga": 5000},
    "2": {"nama": "Beras 5Kg", "harga": 70000},
    "3": {"nama": "Beras 10Kg", "harga": 130000},
    "4": {"nama": "Aqua 1L", "harga": 6000},
    "5": {"nama": "Milo Kaleng", "harga": 130000},
    "6": {"nama": "Indomie Goreng", "harga": 3500},
    "7": {"nama": "Indomilk Sachet", "harga": 130000},
}

# Ketentuan Tambahan
membership_fee_2019 = 30000
biaya_tambahan_2019 = 0

print("=== SISTEM TRANSAKSI TOKO ===\n")

# Data Pelanggan
nama_2019 = input("Masukkan Nama Pelanggan : ")
input_status_2019 = input(f"Selamat datang {nama_2019}\nApakah anda adalah member di toko kami? (member/nonmember) : ").strip().lower()

is_member_2019 = False

# Menentukan Member / Non-Member
if input_status_2019 in ["member", "ya", "y"]:
    is_member_2019 = True
    print("Wah ada member, nikmatin diskonnya ya!\n")
elif input_status_2019 in ["nonmember", "tidak", "n"]:
    minat_2019 = input("Apakah berminat berlangganan membership? (30Rb/bulan, diskon 10%): (Ya/Tidak) : ").strip().lower()
    if minat_2019 in ["ya", "iya", "y"]:
        is_member_2019 = True
        biaya_tambahan_2019 += membership_fee_2019  # Operator Augmented Assignment (+=)
        print("Selamat anda sudah menjadi member di toko kami!\n")
    else:
        is_member_2019 = False

# LOOPING PEMBELIAN BARANG DARI DICTIONARY

total_belanja_2019 = 0
total_item_2019 = 0
daftar_pembelian_2019 = []

menu_2019 = True
while menu_2019:
    print(f"\n{nama_2019}, mau beli apa? Ini daftarnya:")
    for nomor_2019, barang_2019 in produk_2019.items():
        print(f'{nomor_2019}. {barang_2019["nama"]} - Rp{barang_2019["harga"]}')

    pilihan_2019 = input("\nMasukkan nomor barang: ")
    if pilihan_2019 in produk_2019:
        jumlah_2019 = int(input("Masukkan jumlah barang: "))
        item_2019 = produk_2019[pilihan_2019]
        
        subtotal_2019 = item_2019["harga"] * jumlah_2019
        total_belanja_2019 += subtotal_2019
        total_item_2019 += jumlah_2019
        daftar_pembelian_2019.append(f"{item_2019['nama']} (x{jumlah_2019})")
        print(f"-> {item_2019['nama']} dimasukkan ke keranjang.")
    else:
        print("Nomor barang tidak valid!")

    tanya_2019 = input("\nApakah ingin membeli barang lain? (y/n): ").strip().lower()
    if tanya_2019 != 'y':
        menu_2019 = False

# Input Kode Promo
kode_promo_2019 = input("\nMasukkan Kode Promo : ").strip().upper()


# OPERATOR KEANGGOTAAN (MEMBERSHIP)

daftar_promo_2019 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]
promo_tersedia_2019 = kode_promo_2019 in daftar_promo_2019

# OPERATOR PERBANDINGAN & OPERATOR LOGIKA

syarat_belanja_2019 = total_belanja_2019 >= 200000
syarat_barang_2019 = total_item_2019 >= 3

# Evaluasi Logika
dapat_diskon_member_2019 = is_member_2019 and syarat_belanja_2019
dapat_promo_2019 = promo_tersedia_2019 or (syarat_barang_2019 and not is_member_2019)

# OPERATOR ARITMATIKA & OPERATOR PENUGASAN
persen_diskon_2019 = 0.0

if dapat_diskon_member_2019:
    persen_diskon_2019 += 0.10

if dapat_promo_2019 and kode_promo_2019 == "HEMAT10":
    persen_diskon_2019 += 0.10

besarnya_diskon_2019 = total_belanja_2019 * persen_diskon_2019
total_pembayaran_2019 = (total_belanja_2019 - besarnya_diskon_2019) + biaya_tambahan_2019
rata_rata_harga_2019 = total_belanja_2019 / total_item_2019 if total_item_2019 > 0 else 0

# OPERATOR IDENTITAS (IDENTITY: is, is not)

ref_member_2019 = True
cek_identitas_2019 = is_member_2019 is ref_member_2019

# OPERATOR BITWISE

BIT_MEMBER_2019     = 0b0001
BIT_TOTAL_200K_2019 = 0b0010
BIT_BARANG_3_2019   = 0b0100
BIT_PROMO_2019      = 0b1000

kode_status_2019 = 0b0000

# Bitwise OR (|)
if is_member_2019:
    kode_status_2019 |= BIT_MEMBER_2019
if syarat_belanja_2019:
    kode_status_2019 |= BIT_TOTAL_200K_2019
if syarat_barang_2019:
    kode_status_2019 |= BIT_BARANG_3_2019
if promo_tersedia_2019:
    kode_status_2019 |= BIT_PROMO_2019

# Bitwise AND (&)
cek_member_bit_2019 = kode_status_2019 & BIT_MEMBER_2019
cek_promo_bit_2019 = kode_status_2019 & BIT_PROMO_2019

# Bitwise XOR (^)
kode_referensi_2019 = 0b1011
hasil_xor_2019 = kode_status_2019 ^ kode_referensi_2019

# Bitwise Shift (<<)
hasil_shift_2019 = kode_status_2019 << 1



# OUTPUT HASIL SESUAI HAK AKSES & MODUL

print("\n=== DATA TRANSAKSI ===")
print(f"Nama Pelanggan        : {nama_2019}")
print(f"Status Pelanggan      : {'member' if is_member_2019 else 'nonmember'}")
print(f"Total Belanja         : Rp{int(total_belanja_2019)}")
print(f"Jumlah Barang         : {total_item_2019}")
print(f"Kode Promo            : {kode_promo_2019}")

print("\n=== HASIL VALIDASI ===")
print(f"Belanja >= Rp200000        : {syarat_belanja_2019}")
print(f"Jumlah Barang >= 3         : {syarat_barang_2019}")
print(f"Status Member              : {is_member_2019}")
print(f"Kode Promo Tersedia        : {promo_tersedia_2019}")
print(f"Mendapatkan Diskon         : {dapat_diskon_member_2019}")
print(f"Mendapatkan Promo          : {dapat_promo_2019}")

print("\n=== HASIL PERHITUNGAN ===")
print(f"Diskon                     : Rp{int(besarnya_diskon_2019)}")
print(f"Total Pembayaran           : Rp{int(total_pembayaran_2019)}")
print(f"Rata-rata Harga Barang     : Rp{rata_rata_harga_2019:.0f}")

print("\n=== HAK AKSES PELANGGAN ===")
print(f"Kode Hak Akses             : {bin(kode_status_2019)[2:].zfill(4)}")
print(f"Member Access              : {bool(cek_member_bit_2019)}")
print(f"Promo Access               : {bool(cek_promo_bit_2019)}")
print(f"Free Shipping Access       : {bool(kode_status_2019 & BIT_TOTAL_200K_2019)}")

print("\n=== OPERASI BITWISE ===")
print("=== Kode Status Transaksi ===")
print("0001 | 0010 | 0100 | 1000")
print(f"Kode Biner    : {bin(kode_status_2019)[2:].zfill(4)}")
print(f"Kode Desimal  : {kode_status_2019}")

print("\n=== Pemeriksaan Status ===")
print("Cek Member")
print(f"{bin(kode_status_2019)[2:].zfill(4)} & 0001")
print(f"Hasil Biner   : {bin(cek_member_bit_2019)[2:].zfill(4)}")
print(f"Hasil Desimal : {cek_member_bit_2019}")

print("\nCek Promo")
print(f"{bin(kode_status_2019)[2:].zfill(4)} & 1000")
print(f"Hasil Biner   : {bin(cek_promo_bit_2019)[2:].zfill(4)}")
print(f"Hasil Desimal : {cek_promo_bit_2019}")

print("\n=== Perbandingan Status ===")
print(f"Kode Transaksi : {bin(kode_status_2019)[2:].zfill(4)}")
print(f"Kode Referensi : {bin(kode_referensi_2019)[2:].zfill(4)}")
print(f"{bin(kode_status_2019)[2:].zfill(4)} ^ {bin(kode_referensi_2019)[2:].zfill(4)}")
print(f"Hasil Biner   : {bin(hasil_xor_2019)[2:].zfill(4)}")
print(f"Hasil Desimal : {hasil_xor_2019}")

print("\n=== Shift ===")
print(f"{bin(kode_status_2019)[2:].zfill(4)} << 1")
print(f"Hasil Biner   : {bin(hasil_shift_2019)[2:]}")
print(f"Hasil Desimal : {hasil_shift_2019}")

print("\n=== SELESAI ===")










#2611532019
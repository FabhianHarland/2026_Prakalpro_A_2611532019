print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")
n_2019 = int(input("Masukkan ukuran skala jam pasir (N): "))

# ===== Border Atas =====
print("#", end="")
for i_2019 in range(4 * n_2019 + 5):
    print("=", end="")
print("#")

# ===== Fase 1: Jam Pasir Atas (baris N turun ke 1) =====
for baris_2019 in range(n_2019, 0, -1):
    print("| ", end="")
    for kiri_2019 in range(2 * (n_2019 - baris_2019)):
        print(" ", end="")
    for angka_2019 in range(baris_2019, 0, -1):
        print(angka_2019, end=" ")
    print("<*>", end="")
    for angka_2019 in range(1, baris_2019 + 1):
        print(" ", end="")
        print(angka_2019, end="")
    for kanan_2019 in range(2 * (n_2019 - baris_2019)):
        print(" ", end="")
    print(" |")

# ===== Fase 2: Poros Titik Pusat =====
print("|", end="")
for kiri_2019 in range(2 * n_2019 + 1):
    print(" ", end="")
print("<*>", end="")
for kanan_2019 in range(2 * n_2019 + 1):
    print(" ", end="")
print("|")

# ===== Fase 3: Jam Pasir Bawah (baris 1 naik ke N) =====
for baris_2019 in range(1, n_2019 + 1):
    print("| ", end="")
    for kiri_2019 in range(2 * (n_2019 - baris_2019)):
        print(" ", end="")
    for angka_2019 in range(baris_2019, 0, -1):
        print(angka_2019, end=" ")
    print("<*>", end="")
    for angka_2019 in range(1, baris_2019 + 1):
        print(" ", end="")
        print(angka_2019, end="")
    for kanan_2019 in range(2 * (n_2019 - baris_2019)):
        print(" ", end="")
    print(" |")

# ===== Border Bawah =====
print("#", end="")
for i_2019 in range(4 * n_2019 + 5):
    print("=", end="")
print("#")
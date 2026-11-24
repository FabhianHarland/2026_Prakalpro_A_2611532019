menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []

# Baca data dengan nested loop
for day in range(1, number_of_days + 1):
    row = []
    for menu in menus:
        val = int(input(f"Day {day}, {menu}: "))
        row.append(val)
    sales.append(row)

# Cetak total porsi setiap hari (traversal per baris)
print("Total per day:")
for idx, row in enumerate(sales, start=1):
    print(f"Day {idx}: {sum(row)}")

# Hitung total setiap menu (traversal per kolom)
menu_totals = []
for col_idx, menu in enumerate(menus):
    total_menu = 0
    for row_idx in range(number_of_days):
        total_menu += sales[row_idx][col_idx]
    menu_totals.append((menu, total_menu))

print(f"Total per menu: {menu_totals}")

# Cari menu terlaris (jika sama, pilih yang muncul lebih dulu)
best_name = ""
best_total = -1
for name, total in menu_totals:
    if total > best_total:
        best_total = total
        best_name = name

print(f"Best seller: {best_name} ({best_total})")
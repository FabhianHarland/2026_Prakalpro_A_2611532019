number_of_rows = 4
seats_per_row = 5

# Buat denah 4 baris x 5 kursi dengan list terpisah per baris
seats = [["." for _ in range(seats_per_row)] for _ in range(number_of_rows)]

while True:
    for r_idx, row in enumerate(seats, start=1):
        print(f"Row {r_idx}: " + " ".join(row))

    row_input = int(input("Row (0 to stop): "))
    if row_input == 0:
        break

    seat_input = int(input("Seat: "))

    # Cek apakah di luar rentang
    if not (1 <= row_input <= number_of_rows and 1 <= seat_input <= seats_per_row):
        print("Invalid seat.")
        continue

    r = row_input - 1
    c = seat_input - 1

    # Cek apakah sudah terisi
    if seats[r][c] == "X":
        print("Seat already taken.")
    else:
        seats[r][c] = "X"
        print("Seat booked.")

seats_taken = sum(row.count("X") for row in seats)
print(f"Seats taken: {seats_taken}")
pass_score = 60 
excelent = 85

while True :
    student_count = int(input("Masukkan jumlah murid : "))
    if student_count < 1:
        print("invalid")
    else:
        break

total_score = 0
passed = 0
lowest_score = 100
excelent_count = 0

for student in range(1,student_count + 1):
    while True:
        score = int(input(f"Masukkan nilai siswa ke-{student} : "))
        if score < 0 or score > 100:
            print("Invalid")
        else: 
            break

    total_score += score
    if score >= pass_score:
        passed += 1
    if score < lowest_score:
        lowest_score = score
    if score >= excelent:
        excelent_count += 1

avarage_score = total_score / student_count

print(f"Nilai rata-rata Murid : {avarage_score}")
print(f"Jumlah murid yang lulus : {passed}")
print(f"Nilai Terendah : {lowest_score}")
print(f"Jumlah seluruh nilai murid : {total_score}")
print(f"Jumlah nilai sempurna : {excelent_count}")
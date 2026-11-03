result = 0
while True :
    number = int(input("Enter number  : "))
    if number < 0 :
        break
    if number == 0:
        continue
    print(f"Positif Number : {number}")
    result += number

    stop = input("apakah ingin lanjut (y/n)")
    if stop == "n":
        break
    
print(f"Result : {result}")

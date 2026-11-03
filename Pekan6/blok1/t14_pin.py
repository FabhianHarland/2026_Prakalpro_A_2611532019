attempt = 1
max_attemp = 3
correct_pin = "2019"
pin = input("Enter Pin: ")
if pin == correct_pin :
    print("Access granted")
else:
    print("Incorrect PIN")

while pin != correct_pin and attempt < max_attemp :
    pin= input("Enter pin: ")
    attempt += 1
print("Account Locked")

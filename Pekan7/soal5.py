#Nama : M.Fabhian Harland
#NIM : 2611532019
#Question 5 (A)

username = input("Username: ")


if len(username) < 5:
    print("Invalid : At least 5 characters")
elif not username.isalnum():
    print("Invalid : Letter and digits only")
elif not username.isalpha():
    print("Invalid : must start with a letter")
else:
    print("Valid")


#Question 5 (B)
nim = input("Nim : ")

if len(nim) < 10 :
    print("Invalid : At least 10 characters")
elif nim.isalpha():
    print("Invalid : Digits only")
else:
    print(f"Valid, intake years 20{nim[0:2]}")
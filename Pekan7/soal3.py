#Nama : M.Fabhian Harland
#NIM : 2611532019
#Question 3 (A)

text = "Informatika"
print(text[10])
print(text.upper())
print(text[0:20])

#Question 3 (B)

text = "M. Fabhian Harland".lower()
count = 0
for char in text:
    if char in "aiueo":
        count += 1 
print("Vowels:", count)

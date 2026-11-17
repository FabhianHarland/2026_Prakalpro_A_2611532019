#Nama : M.Fabhian Harland
#NIM : 2611532019
#Question 7

full_name = "m.fabhian harland"
nim = "2611532019"

clean_name = full_name.strip()
spasi = clean_name.find(" ")
if spasi == -1:
    first_name = spasi
else:
    first_name = clean_name[:spasi]

username = first_name.lower() + nim[-3:]

angkatan ="20" + nim[:2]

print("="*30)
print("STUDENT CENTER".center(30))
print("="*30)
print(f"{'Name ':<10} : {full_name.title()}")
print(f"{'Nim ':<10} : {nim}")
print(f"{'Username ':<10} : {username}")
print(f"{'Angkatan ':<10} : {angkatan}")
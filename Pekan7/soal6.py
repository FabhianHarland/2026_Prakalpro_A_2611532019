#Nama : M.Fabhian Harland
#NIM : 2611532019
#Question 6


# first_name  = "M."
# last_name   = "Fabhian Harland"
# nim = "2611532019"

# full_name   = first_name.strip() + " " + last_name.strip()
# print(full_name)
# print(full_name.title())

# print(full_name + " " + nim)

full_name = " M.Fabhian Harland "
nim = "2611532019"

clean_name = full_name.strip()
spasi = clean_name.find(" ")
if spasi == -1:
    first_name = spasi
else:
    first_name = clean_name[:spasi]

username = first_name.lower() + nim[-3:]
print(username)
umur_2019 = int(input("Input umur anda : "))
sim_2019 = input("Apakah anda sudah punya SIM c (y/t)")[0].lower()
if umur_2019 >= 17 and sim_2019 == "y":
    print("Anda sudah dewasa dan boleh bawa motor")

if umur_2019 >= 17 and sim_2019 != "y":
    print("Anda sudah dewasa tetapi tidak boleh bawa motor")

if umur_2019 < 17 and sim_2019 == "y":
    print("Anda belum cukup umur punya SIM")

if umur_2019 < 17 and sim_2019 != "y":
    print("Anda belum cukup umur bawa motor")


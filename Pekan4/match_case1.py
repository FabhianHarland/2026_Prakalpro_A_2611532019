bulan_2019 = int(input("Masukkan angka bulan (1-12) : "))

match bulan_2019:
    case 1:
        print("Januari")
    case 2:
        print("Februari")
    case 3:
        print("Maret")
    case 4:
        print("April")
    case 5:
        print("Mei")
    case 6:
        print("Juni")
    case 7:
        print("Juli")
    case 8:
        print("Agustus")
    case 9:
        print("Sebtember")
    case 10:
        print("November")
    case 11:
        print("Oktober")
    case 12:
        print("Desember")   
    case _:
        print("angka tidak valid")
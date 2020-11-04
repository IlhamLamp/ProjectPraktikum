a = input("Masukkan nilai a: ")
b = input("Masukkan nilai b: ")
print("Variabel a=",a)
print("Variabel b=",b)
print("Hasil penggabungan {1}&{0}=%s".format(a,b) %(b+a))

#konversi nilai variabel
a = int(a)
b = int(b)
print("Hasil penjumlahan {1}+{0}=%d".format(a,b) %(a+b))
print("Hasil pembagian {1}/{0}=%d".format(a,b) %(b/a))

"""
Karena jika saya menjalankan program pada baris ke-11

    print("Hasil pembagian {1}/{0}=%d".format(a,b) %(a/b))

Jika :
a adalah 10
b adalah 15

maka b/a=%d
    15/10=0.666 >> ini bukan hasilnya, karena 15/10 adalah 1.5

sedangkan bila a/b=%d
    10/15=0.666

Jadi saya menukar %(a/b) menjadi %(b/a)
"""

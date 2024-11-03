def cek_trio_ajaib(a, b, c):
    
    return (a + b == c) or (a + c == b) or (b + c == a)


angka1 = 3
angka2 = 5
angka3 = 8

if cek_trio_ajaib(angka1, angka2, angka3):
    print("Ini adalah trio ajaib!")
else:
    print("Bukan trio ajaib.")
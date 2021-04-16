print("______________________________________________________________________________________")
print("PERHITUNGAN RUMUS FISIKA DASAR")
print()
print("PERHITUNGAN  Kecepatan Akhir Benda pada GLBB")
#menggunakan fungsi numerik dengan metode sqrt
print()
print('Diket : ')
Vo = (float(input("Vo : ")))
s = (float(input("s : ")))
a = (float(input("a : ")))
import math
print("Jawab: ")
Vt = Vo**2 + 2*a*s
Hasil = math.sqrt(Vt)
print("Kecepatan benda adalah : ", Hasil)
print("Kecepatan benda setelah dibulatkan ke atas : ", math.ceil(Hasil))
print("Kecepatan benda setelah dibulatkan ke bawah : ", math.floor(Hasil))
print()
print("______________________________________________________________________________________")
print("MENENTUKAN TEKANAN BALOK")
print()
print()
import math
F = float(input("Gaya pada balok :"))
a = float(input("Luas Permukaan Balok 1 :"))
b = float(input("Luas Permukaan Balok 2 :"))
c = float(input("Luas Permukaan Balok 3 :"))
x = F/a
y = F/b
z = F/c
print()
print("Tekanan Balok 1 : ", x)
print("Tekanan Balok 2 : ", y)
print("Tekanan Balok 3 : ", z)
print()
print("Tekanan terbesar ", max(x,y,z))
print("Tekanan terkecil ", min(x,y,z))
p = "end"
q = p.center(200, '-')
print(q)

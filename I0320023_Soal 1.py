print("SELAMAT DATANG")
print()

# Merevisi penggunaan awal kalimat
sentence = (str(input("Kalimat awal : ")))
s = sentence.capitalize()

#mengubah format kalimat menjadi UPPER
x = sentence.upper()

#menghitung huruf pada kalimat
a = (str(input("Pilih huruf yang akan dihitung : ")))

#Mencari kata dalam kalimat
b = (str(input("Kata yang akan dicari : ")))

#Mengakhiri Pemograman
y = "Thankyou and Have a Nice Day"
z = y.center(50, '*')
print()
print("Kalimat setelah diperbaiki :", s)
print("Kalimat menjadi UPPER :", x)
print("Jumlah huruf : ", sentence.count(a))
print("kata terdapat pada index : ", sentence.find(b))
print("kata dalam index : ", sentence.index(b))
print()
print(z)

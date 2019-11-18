"""
NAMA: DHEVAN MUHAMAD ANTHAREZA
NIM: A11.2019.12293
KELOMPOK: A11.4118
TANGGAL: 18-11-2019
"""
#Menggunakan While
print ("\n==== Menggunakan While ========")
i = 0
while i <= 127 :
    print(chr(i), end=" ")
    i += 1
print ("\n==================================")



#Menggunakan For
print ("\n==== Menggunakan FOR ========")
for i in range(127) :
    print (chr(i),end=" ")
print ("\n==================================")



#Menggunakan Do - While
print ("\n==== Menggunakan Do - While ========")
a = 127
b = 0
while True :
    nilai_ascii = str(chr(b))
    print(nilai_ascii, end=" ")
    b += 1
    if b > a :
        break
print ("\n==================================")
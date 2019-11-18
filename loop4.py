"""
NAMA: DHEVAN MUHAMAD ANTHAREZA
NIM: A11.2019.12293
KELOMPOK: A11.4118
TANGGAL: 18-11-2019
"""
i = 0
data = []
banyak = int(input("Masukan banyak data yang anda mau: "))
while(i < banyak) :
    data.append(int(input("Masukan data ke-{}: ".format(i + 1))))
    i += 1
j=0
print("Data yang anda inputkan adalah = ", end="")
while(j < banyak) :
    print(data[j], end=" ")
    j += 1
print("")
"""
NAMA: DHEVAN MUHAMAD ANTHAREZA
NIM: A11.2019.12293
KELOMPOK: A11.4118
TANGGAL: 18-11-2019
"""
i = 1
jumlah = 0
count = 0
while(i <= 60):
    if(i % 3 == 0) :
        jumlah += i
        count += 1
    i += 1
print("Jumlah : ", jumlah)
print("Rata-rata : ", jumlah/count)
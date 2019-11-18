"""
NAMA: DHEVAN MUHAMAD ANTHAREZA
NIM: A11.2019.12293
KELOMPOK: A11.4118
TANGGAL: 18-11-2019
"""
jumlahAyam = 3
telurPerAyam = 3
hargaTelur = 14500
hargaAyam = 150000
perawatan = 200000
biayaYangDikeluarkan = hargaAyam * jumlahAyam
biayaYangDidapat = 0
bulanAwal = 3
bulanAkhir = 20
jumlahTelur = 0
for i in range(bulanAwal, bulanAkhir):
    if(i >= 4) :
        jumlahTelur += telurPerAyam * jumlahAyam * 30
        biayaYangDidapat += jumlahTelur/15 * hargaTelur
    biayaYangDikeluarkan += perawatan
    print("Bulan {} = {}".format(i-2, jumlahTelur))
print("Jumlah telur yang didapat = {} Kg".format(jumlahTelur/15))
print("Biaya yang masuk          = ", biayaYangDidapat)
print("Biaya yang keluar         = ", biayaYangDikeluarkan)
print("Keuntungan                = ", biayaYangDidapat - biayaYangDikeluarkan)

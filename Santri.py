santri = "Baihaki Al Biruni"
pelajaran = "Algoritma"
nilai = int(input("Masukan Nilai Anda : "))
# Variabel

#cetak data
#print("Nama Santri :",santri,
     # "\nMata Pelajaran :",pelajaran,
# "\nNilai :",nilai)
#----------------------------
#Fungsi If Biasa
#if (nilai >= 60):
#	print("Lulus")
#else:
#	print("Tidak Lulus")
#-----------------------------
#Tupple And List
#ket = ("Lulus","Gagal")[nilai <= 60]
# ---------------------------------------
#Ternary
# ket = "Lulus" if nilai >= 60 else "Gagal
# ----------------------------------------
#Kalau di dalam Taple nilai false dulu baru true
#Ternary
if(nilai >= 85 and nilai <= 100): grade = "A"
elif(nilai >= 75 and nilai <= 85): grade = "B"
elif(nilai >= 60 and nilai <= 75): grade = "C"
elif(nilai >= 50 and nilai <= 60): grade = "D"
else: grade= "E"

if(grade == "A"): pred = "IstriMewah"
elif(grade == "B"): pred = "Bagoes"
elif(grade == "C"): pred = "Mantulz"
elif(grade == "D"): pred = "Ashiapp"
else: pred = "Keluar Saja Dari Sekolah"

print("---------------------------"
	"\nNilai Saya :",nilai,
	"\nHasil Anda :",grade,
	"\nGrade Anda :",pred)
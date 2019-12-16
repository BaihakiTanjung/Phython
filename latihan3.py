print ("\t \t Aplikasi Perhitungan Gaji Karyawan")

print ("\t \t\t Isi Dulu ya")
print ("===============================================================================")
nama =input("Masukan Nama Karyawan \t: ")
print(" Manajer \n Superviser \n Staff")
jabatan = input("Masukan Jabatan \t: ")
print(" 1. Sudah Menikah \n 2. Belum Menikah")
status = int(input("Masukan Kode Status \t: ")) 
anak =int(input("Masukan Jumlah Anak \t: "))
agama = input("Masukan Agama Anda \t: ")


# Variable / Data 

# Fungsi
if(jabatan == "Manajer"): 
	gaji=10000000
elif(jabatan == "Superviser"): 
	gaji=7000000
elif(jabatan == "Staff"):
	gaji=3000000
else: gaji=""

# Fungsi1 
tunjab = gaji* 0.30

# # Fungsi2
tukel = (0,gaji*0.2)[status==1]

# # Fungsi3
if(anak >= 1 and anak <=3): hitungtunjab = 0.1 * gaji * anak
elif(anak > 3): hitungtunjab = 0.1 * gaji * 3
else: hitungtunjab = 0 


# # Fungsi4
if(agama == "Islam" and gaji >= 700000): zakat = 0.025 * gaji
else: zakat = 0

# Fungsi5 
gaber = int(gaji)+int(tunjab)+int(tukel)+int(hitungtunjab)-int(zakat)



print("Nama Saya : ",nama,
	"\n Jabatan Saya : ", jabatan,
	"\n Gaji Pokok Saya : ", gaji,
	"\n Tunjangan Gaji Pokok : ",tunjab,
	"\n Tunjangan Keluarga : ",tukel,
	"\n Tunjangan Anak : ",hitungtunjab,
	"\n Bayar Zakat : ", zakat,
	"\n Gaji Bersih : ", gaber)
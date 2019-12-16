nama = "I Gede Banget"
jabatan = "Manajer"
status = "Sudah Menikah"
anak = 2
agama = "Islam"


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
tukel = (0,gaji*0.2)[status=="Sudah Menikah"]

# # Fungsi3
if(status == "Sudah Menikah" and anak >= 1 and anak <=3): hitungtunjab = 0.1 * gaji * anak
elif(status == "Sudah Menikah" and anak > 3): hitungtunjab = 0.1 * gaji * 3
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
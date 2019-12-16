nama = "Muhammad Reza"
jabatan = "Human Resource Development"
status = "Menikah"
anak = 1
agama = "Islam"

#variable / table

#fungsi
if(jabatan == "Human Resource Development"):
	gaji=8000000
elif(jabatan == "Bagian Umum"):
	gaji=5500000
elif(jabatan == "Kabag Operasional"):
	gaji=4000000

#fungsi1
tunjab = gaji * 0.30

#fungsi2
tukel = (0,gaji * 0.2)[status=="Menikah"]

#fungsi3
if(status == "Menikah" and anak >= 1 and anak <= 3): hitungtunjab = 0.1 * gaji * anak
elif(status == "Menikah" and anak > 3): hitungtunjab = 0.1 * gaji * 3
else: hitungtunjab = 0

#fungsi4
if(agama == "Islam" and gaji >= 7000000): zakat = 0.025 * gaji

#fungsi5
gaber = int(gaji)+int(tunjab)+int(tukel)+int(hitungtunjab)-int(zakat)


print("Nama Saya : ",nama,
	"\nNama Jabatan : ",jabatan,
	"\nGaji Pokok Saya : ",gaji,
	"\nTunjangan Gaji Pokok : ",tunjab,
	"\nTunjangan Keluarga : ",tukel,
	"\nTunjangan Anak : ",hitungtunjab,
	"\nBayar Zakat : ",zakat,
	"\nGaji Bersih : ", gaber)	
#Data Variable
lokasi = "Pekanbaru"
skala = 4
dampak1 = "Bangunan Roboh" 
dampak2 = "Berpotensi Tsunami"
#Cetak Data
if(skala < 5):
	print(lokasi,"Terkena Gempa Dengan Kekuatan",skala, "Richter Yang Menyebabkan " ,dampak1)
else:
	print(lokasi,"Terkena Gempa Dengan Kekuatan",skala, "Skala Richter Yang Menyebabkan " ,dampak2)
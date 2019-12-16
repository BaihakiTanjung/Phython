#Data Variable
nama = "Baihaki Al Biruni"
produk = "TV"
harga = 20000
jumlahbeli = 2 
hargakotor = harga * jumlahbeli
diskon = harga * 0.2
ppn = (hargakotor - diskon) * 0.1
hargabersih = hargakotor - diskon + ppn 


#Cetak Data
print("Nama Pelanggan",nama,
	"\n Produk : ",produk,
	"\n Harga : ",harga,
	"\n Jumlah Beli : ",jumlahbeli,
	"\n Diskon 20% : ",diskon,
	"\n PPN 10 % : ", ppn,
	"\n Harga Bersih : ",hargabersih,
	)
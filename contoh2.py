#-------------------------------------------
#Program : Perhitungan Gaji
#Coded by : Didik Maryono
#NIM : L200144017
#-------------------------------------------

import os

def goto(linenum):
   global line
   line = linenum

def hitung() :
   global tun, uang_lembur, gator, gasih
   tun = int(jml_anak_a) * 200000
   uang_lembur = int(jml_lembur) * int(lembur)
   gator = int(gapok) + int(uang_lembur) + int(tun)
   gasih = int(gator) - ((int(gator) * 5) / 100)
  
def printout() :
   os.system("cls")
   print("")
   print("-------------------------------------")
   print("Gaji Karyawan")
   print("-------------------------------------")
   print("Nama Karyawan : ", nama)
   print("NIP : ", nip)
   print("Golongan : ", gol)
   print("Jumlah Anak : ", jml_anak, "anak")
   print("Jumlah Lembur : ", jml_lembur, "jam")
   print("")
   print("Jabatan :", jab)
   print("Gaji Pokok : Rp.", gapok)
   print("Gaji Lembur : Rp.", uang_lembur)
   print("Tunjangan : Rp.", tun)
   print("Gaji Kotor : Rp.", gator)
   print("Gaji Bersih : Rp.", gasih)

  line = 0
  while True:
    if line == 0:
      os.system("cls")
      print("------------------------------------")
      print("Perhitungan Gaji Karyawan")
      print("------------------------------------")
      print("")

      nama = input("Masukkan Nama : ")
      nip = input("Masukkan NIM : ")
      goto(1)

   elif line == 1 :
      gol = input("Masukkan Golongan : ")

   if gol == "1" :
gapok = 8000000
lembur = 100000
jab = "Direktur"
goto(2)
elif gol == "2" :
gapok = 6000000
lembur = 80000
jab = "Manajer"
goto(2)
elif gol == "3" :
gapok = 4000000
lembur = 60000
jab = "Supervisor"
goto(2)
elif gol == "4" :
gapok = 2000000
lembur = 40000
jab = "Operator"
goto(2)
else :
print("Tidak ada dalam pilihan golongan. Input ulang golongan anda.")
goto(1)

elif line == 2 :

jml_anak_a = input("Masukkan Jumlah Anak : ")
jml_anak = jml_anak_a
if int(jml_anak_a) > 3 :
jml_anak_a = 3

jml_lembur = input("Masukkan Jumlah Lembur : ")

hitung()
printout()
goto(3)

elif line == 3 :
print("")
ulang = input("Ulang perhitungan? (y/n) : ")
if ulang == "y" :
goto(0)
elif ulang == "n" :
exit(0)
else :
print("Tidak ada dalam pilihan")
goto(3)
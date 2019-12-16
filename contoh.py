
lagi='y'
while lagi=='y':



    print ("\t \t Aplikasi Perhitungan Gaji Karyawan")

    print ("\t \t\t WWW.PanduanCode.com")
    print ("===============================================================================")
    nip=input("Masukan No Induk Pegawai \t: ")
    nama=input("Masukan Nama Dosen/Staff \t: ")
    print ("1. Rektor \n2. Dekan \n3. Kepala Jurusan \n4. Sekjur \n5. Dosen \n6. Staff Lain")
    jabatan=input("Masukan Jabatan \t\t: ")
    alamat=input("Masukan Alamat \t\t\t: ")
    jml_anak=input("Masukan Jumlah Anak \t\t: ")
    if (jabatan=='1'):
        gaji_pokok=10000000
        jab="Rektor"
    elif(jabatan=='2'):
        gaji_pokok=8500000
        jab="Dekan"
    elif(jabatan=='3'):
        gaji_pokok=6000000
        jab="Kepala Jurusan"
    elif(jabatan=='4'):
        gaji_pokok=5000000
        jab="Sekjur"
    elif(jabatan=='5'):
        gaji_pokok=4000000
        jab="Dosen"
    else:
        gaji_pokok=3000000
        jab="Staff Lain"



    if(jml_anak>='5'):

        tunjangan=1000000
    elif(jml_anak <='3'):
        tunjangan=750000
    else:
        tunjangan=500000



    pajak= gaji_pokok *0.15

    gaji_bersih= gaji_pokok-pajak+tunjangan



    print ("")

    print ("\n")
    print ("===============================================================================")
    print ("\t\t\t WWW.PanduanCode.com")
    print ("\t\t\t Kota Banjar Patroman")
    print ("")
    print ("Nip \t\t: ",nip)
    print ("Nama \t\t: ",nama)
    print ("Jabatan \t: ",jab)
    print ("Alamat \t\t: ",alamat)
    print ("Gaji bersih \t: ",gaji_bersih)
    print ("")
    print ("===============================================================================")
    print ("")
    lagi=input("Ambil Data Lagi [y/n]? : ")


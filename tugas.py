# 1
bilangan = int(input("masukan bilangan yang diiinput: "))
if bilangan % 2 == 0:
    print(f"bilangan genap adalah {bilangan}")
else:
    print(f"bilangan ganjil adalah {bilangan}")

 
 # 2
angka = int(input("masukan angka: "))

if angka > 0:
    print("angka yg kamu masukan positif")
elif angka == 0:

    print("angka yg kamu masukan 0")

else:
    print("angka yg kamu masukan negatif")


# 3
nama = input("masukan nama anda: ")
jabatan = input("masukan jabatan anda: ")
jam_lembur = int(input("masukan jam lembur anda: "))
if jabatan == 'manager':
    upah_perjam = 30000
    hasil = jam_lembur*upah_perjam
elif jabatan == 'TU':
    upah_perjam = 15000
elif jabatan == 'staf':
    upah_perjam = 10000
elif jabatan == 'buruh':
    upah_perjam = 7000
hasil = jam_lembur*upah_perjam
print(f"upah anda adalah: {hasil:,}")

# 4
kode_mobil = input("masukan kode mobil: ")
lama_sewa = int(input("berapa lama sewanya: "))
if kode_mobil == 'M1' :
    jenis_mobil = 'fortuner/fajero'
    tarif = 500000
elif kode_mobil == 'M2':
    jenis_mobil = 'rush/terios'
    tarif = 400000
elif kode_mobil == 'M3':
    jenis_mobil = 'BRV/HRV'
    tarif = 350000
elif kode_mobil == 'M4':
    jenis_mobil = 'avanza/xenia'
    tarif = 300000
else:
    kode_mobil == 'M5'
    jenis_mobil = 'agya/alya'
    tarif = 250000
total_sewa = lama_sewa*tarif

if total_sewa >= 2500000:
    potongan = 0.15*total_sewa
else:
    potongan = 0.5*total_sewa

sisa_sewa=total_sewa-potongan
print(f"Nama Mobil: {jenis_mobil}")
print(f"Tarif Sewa:  Rp. {tarif:,}")
print("============================")
print(f"total sewa adalah: Rp. {total_sewa:,}")
print(f"dapat potongan sebesar: Rp. {potongan:,}")
print(f"sisa sewa adalah: Rp. {sisa_sewa:,}")

# 5
nama_mahasiswa = input(f"masukan nama mahasiswa: ")
ips = float(input(f"masukan ips: "))
if ips > 2.99:
    sks = 24 
elif ips > 2.49:
    sks = 21
elif ips > 1.99:
    sks = 18 
elif ips > 1.49:
    sks = 15 
else:
    sks = 12 
print(f"batas sks bisa diambil: {sks}")

# 6
nama_pegawai = input("masukan nama pegawai: ")
golongan = input("masukan golongan: ")
SK = input("status kawin Y/T: ")
JA = int(input("jumlah anak: "))

if golongan == 'I':
    gaji_pokok = 1200000
elif golongan == 'II':
    gaji_pokok = 1500000
elif golongan == 'III':
    gaji_pokok = 2000000
else:
    golongan == 'IV'
    gaji_pokok = 3000000
if SK == 'Y':
    tunjangan_istri = 0.15
else:
    tunjangan_istri = 0
if JA > 1:
    tunjangan_anak = 0.05+0.05
else:
     tunjangan_anak = 0
l = gaji_pokok*tunjangan_istri
k = gaji_pokok*tunjangan_anak
hasil = gaji_pokok+l+k
print(f"atas nama: {nama_pegawai}")
print(f"tunjangan istri adalah: Rp. {l:,}")
print(f"tunjangan anak adalah: Rp. {k:,}")
print(f"gaji anda adalah: Rp. {hasil:,}")

    
        




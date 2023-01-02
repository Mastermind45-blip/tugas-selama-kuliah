import modul2
data = [

    ['T3122076','DAFA DESKAISYAH','Logika pemrogramman', 90, 80, 90],
    ['H1119218', 'RENDI SIJABAT', 'Sejarah', 90, 80, 75],
    ['S2222998', 'KOSIMI LASOKO', 'Sosiologi', 90, 80, 75]

]
print('='*40)
nomor = 0
for urutan in data:
    nomor +=1
    nim = urutan[0]
    nama = urutan[1]
    kehadiran = urutan[3]
    tugas = urutan[4]
    uts = urutan[5]
    matkul = urutan[2]
    namafak = modul2.fakultas(nim[0:1])
    jurusan = modul2.jurusan(nim[0:3])
    tahun_masuk = '20'+(nim[3:5])
    status = modul2.status(tahun_masuk)
    rata = modul2.rata_rata(kehadiran, tugas, uts)
    uas = modul2.UAS(rata)

    print(f"nomor            :  {nomor}")
    print(f"nim anda adalah  :  {nim}")
    print(f"atas nama        :  {nama}")
    print(f"Fakultas         :  {namafak}")
    print(f"Program Studi    :  {jurusan}")
    print(f"Tahun Masuk      :  {tahun_masuk}")
    print(f"Mata Kuliah      :  {matkul}")
    print(f"Status Mahasiswa :  {status}")
    print(f"Nilai Kehadiran  :  {kehadiran}")
    print(f"Nilai Tugas      :  {tugas}")
    print(f"Nilai UTS        :  {uts}")
    print(f"Nilai Rata-rata  :  {rata:.0f}")
    print(f"Status UAS       :  {uas}")
    print('='*40)



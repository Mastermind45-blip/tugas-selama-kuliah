def fakultas(kode):
    daftar_fakultas = {
        'T':'Teknik/Ilmu Komputer',
        'H':'Hukum',
        'E':'Ekonomi',
        'P':'Pertanian',
        'S':'FISIP'
    }
    
    if kode not in daftar_fakultas.keys():
        fak = 'fakultas tidak di ketahui'
    else:
        fak = daftar_fakultas[kode]
    return fak

def jurusan(kode):
    Daftar_jurusan = {
        'H11':'Ilmu Hukum',
        'E21':'Manajemen',
        'E11':'Akuntansi',
        'T31':'Teknik Informatika',
        'K11':'Sistem Informasi',
        'T41':'Desain Komunkasi Visual',
        'P21':'Agroteknologi',
        'P22':'Agribisnis',
        'P23':'Teknologi Hasil Petanian',
        'S21':'Ilmi Pertanian',
        'S22':'Ilmu Komunikasi',
        'T11':'Teknik Industri',
        'T21':'Teknik Elektro'

    }
    if kode not in Daftar_jurusan.keys():
        jurusan = 'jurusan tidak di ketahui'
    else:
        jurusan = Daftar_jurusan[kode]
    return jurusan

def status(oke):
    if int(oke) < 2022:
        status = 'Program Ulang'
    else:
        status = 'Program Baru'
    return status

def rata_rata(kehadiran, tugas, UTS):
    tambah = (kehadiran + tugas + UTS) / 3
    return tambah

def UAS(nilai):
    if nilai > 85:
        keterangan = 'BEBAS UAS'
    elif nilai > 60:
        keterangan = 'IKUT UAS'
    elif nilai < 60:
        keterangan = 'TIDAK MEMENUHI'
    return keterangan

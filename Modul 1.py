data = [
    {'ID': 1, 'Nama': 'John', 'Usia': 25, 'Kota': 'Jakarta', 'Kontak': '081122334455'},
    {'ID': 2, 'Nama': 'Diana', 'Usia': 30, 'Kota': 'Surabaya', 'Kontak': '082233445566'},
    {'ID': 3, 'Nama': 'Bob', 'Usia': 22, 'Kota': 'Bandung', 'Kontak': '083344556677'}
]

admin = [
    {'Nama' : 'Herdian', 'Password' : '111'},
    {'Nama' : 'Arveliko', 'Password' : '222'}
]

#==============================================================================================================================
from tabulate import tabulate
import regex as re
from os import system, name

def func_clear():
    if name == 'nt':
        _ = system('cls')

#==============================================================================================================================
# READ DATA
def func_read_data1():
    print(tabulate(data, headers= "keys", tablefmt="pretty"))

def func_read_data2():
    func_clear()
    print(tabulate(data, headers= "keys", tablefmt="pretty"))
    filter = input('''
Apakah Anda ingin melakukan filter terhadap isi dari tabel?
y = Ya
n = Tidak
Jawaban Anda: ''')
    if filter == 'y':
        func_main_filter()
    elif not (filter == 'n' or filter =='y'):
        print('Tolong masukkan dengan benar!')
        return func_read_data2()

def func_main_filter():
    main_filter = input("Anda ingin filter berdasarkan apa?")
    if main_filter == 'nama' or main_filter == 'Nama':
        func_filter_nama()
    elif main_filter == 'usia' or main_filter == 'Usia':
        func_filter_usia()
    elif main_filter == 'kota' or  main_filter == 'Kota':
        func_filter_kota()
    elif main_filter  == 'kontak' or main_filter == 'Kontak':
        func_filter_kontak()
    else:
        print('Mohon tuliskan kolom apa yang ingin Anda update datanya!')
        return func_main_filter()
    
def func_filter_nama():
    func_clear()
    print(tabulate(data, headers= "keys", tablefmt="pretty"))
    inputan_nama = input("Masukkan nama yang ingin difilter: ")
    filter_nama = []
    for a in data:
        if inputan_nama == a["Nama"]:
            filter_nama.append(a)
    print(tabulate(filter_nama, headers= "keys", tablefmt="pretty"))
    return filter_nama    

def func_filter_usia():
    func_clear()
    print(tabulate(data, headers= "keys", tablefmt="pretty"))
    inputan_usia = int(input("Masukkan usia yang ingin difilter: "))
    filter_usia = []
    for b in data:
        if inputan_usia == b["Usia"]:
            filter_usia.append(b)
    print(tabulate(filter_usia, headers= "keys", tablefmt="pretty"))
    return filter_usia

def func_filter_kota():
    func_clear()
    print(tabulate(data, headers= "keys", tablefmt="pretty"))
    inputan_kota = input("Masukkan kota yang ingin difilter: ")
    filter_kota = []
    for c in data:
        if inputan_kota == c["Kota"]:
            filter_kota.append(c)
    print(tabulate(filter_kota, headers= "keys", tablefmt="pretty"))
    return filter_kota

def func_filter_kontak():
    func_clear()
    print(tabulate(data, headers= "keys", tablefmt="pretty"))
    inputan_kontak = input("Masukkan kontak yang ingin difilter: ")
    filter_kontak = []
    for d in data:
        if inputan_kontak == d["Kontak"]:
            filter_kontak.append(d)
    print(tabulate(filter_kontak, headers= "keys", tablefmt="pretty"))
    return filter_kontak

#==============================================================================================================================
# CREATE DATA
def func_create_data():
    nama = func_nama_baru()
    usia = func_usia_baru()
    kota = func_kota_baru()
    kontak = func_kontak_baru()
    id = func_id_baru()
    data.append({"ID": id, "Nama": nama, "Usia": usia, "Kota": kota, 'Kontak':kontak})
    func_read_data1()

def func_nama_baru():
    namaBaru = input("Masukkan nama Anda: ")
    if namaBaru.isalpha():
        return namaBaru.capitalize()
    else:
        print('Mohon masukkan huruf saja')
        return func_nama_baru()

def func_usia_baru():
    try:
        usiaBaru = int(input("Masukkan umur Anda: "))
        if usiaBaru >= 100:
            print("Umur maksimal 100 tahun")
            return func_usia_baru()
        else:
            return usiaBaru
    except:
        print('Yang Anda masukkan bukan Angka!')
        return func_usia_baru()

def func_kota_baru():
    kotaBaru = input("Masukkan kota Anda: ")
    if kotaBaru.isalpha():
        return kotaBaru.capitalize()
    else:
        print('Mohon masukkan huruf saja')
        return func_kota_baru()

def func_kontak_baru():
    kontakBaru = str(input("Masukkan kontak Anda: "))
    if kontakBaru.isnumeric():
        if 11 <= len(kontakBaru) <= 13:
            return kontakBaru
        else:
            print('Nomor harus terdiri dari 11 sampai 13 digit')
            return func_kontak_baru()
    else:
        print('Mohon masukkan angka saja')
        return func_kontak_baru()

def func_id_baru():
    idBaru = len(data)+1
    return idBaru

#==============================================================================================================================
# UPDATE DATA

def func_update_data():
    func_clear()
    func_read_data1()
    update_Data = input('Kolom apa yang ingin Anda Update? ')
    if update_Data == 'nama' or update_Data == 'Nama':
        hasil_pencarian_nama = func_update_pencarian()
        func_update_nama(hasil_pencarian_nama)
    elif update_Data == 'usia' or update_Data == 'Usia':
        hasil_pencarian_usia = func_update_pencarian()
        func_update_usia(hasil_pencarian_usia)
    elif update_Data == 'kota' or update_Data == 'Kota':
        hasil_pencarian_kota = func_update_pencarian()
        func_update_kota(hasil_pencarian_kota)
    elif update_Data == 'kontak' or update_Data == 'Kontak':
        hasil_pencarian_kontak = func_update_pencarian()
        func_update_kontak(hasil_pencarian_kontak)
    else:
        print('Mohon tuliskan kolom apa yang ingin Anda update datanya!')
        return func_update_data()

def func_update_pencarian():
    update_Pencarian = int(input("Tuliskan ID yang ingin Anda update datanya: "))
    hasil_pencarian_update = 0
    for item in data:
        if update_Pencarian == item['ID']:
            return hasil_pencarian_update
        hasil_pencarian_update += 1
    print("Data tidak ditemukan")
    return func_update_pencarian()

def func_update_nama(hasil_pencarian_nama):
    update_Nama = func_nama_baru()
    data[hasil_pencarian_nama]["Nama"] = update_Nama
    func_read_data1()

def func_update_usia(hasil_pencarian_usia):
    update_Usia = func_usia_baru()
    data[hasil_pencarian_usia]["Usia"] = update_Usia
    func_read_data1()

def func_update_kota(hasil_pencarian_kota):
    update_Kota = func_kota_baru()
    data[hasil_pencarian_kota]["Kota"] = update_Kota
    func_read_data1()

def func_update_kontak(hasil_pencarian_kontak):
    update_Kontak = func_kontak_baru()
    data[hasil_pencarian_kontak]["Kota"] = update_Kontak
    func_read_data1()

#==============================================================================================================================
# DELETE DATA

def func_delete_data():
    hasil_pencarian_delete = func_delete_data1()
    func_delete_data2(hasil_pencarian_delete)

def func_delete_data1():
    func_clear()
    func_read_data1()
    delete_Data = int(input("Masukkan data keberapa yang ini di hapus: "))
    hasil_pencarian_delete = 0
    for item in data:
        if delete_Data == item['ID']:
            return hasil_pencarian_delete
        hasil_pencarian_delete += 1
    print("Data tidak ditemukan")
    return func_delete_data1()

def func_delete_data2(hasil_pencarian_delete):
    data.pop(hasil_pencarian_delete)
    func_read_data1()

def func_main_data1():
    func_clear()
    while True:
        print('''
        SELAMAT DATANG!

        Apa yang ingin Anda lakukan?
        1. Lihat data
        2. Membuat data
        3. Update data
        4. Delete data
        5. Keluar
        ''')

        input_main = input('Mau pilih angka berapa?')
        if input_main == '1':
            func_read_data2()
        elif input_main == '2':
            func_create_data()
        elif input_main == '3':
            func_update_data()
        elif input_main == '4':
            func_delete_data()
        elif input_main == '5':
            break
        else:
            print("Anda salah!")

def func_main_data2():
    func_clear()
    while True:
        print('''
        SELAMAT DATANG!

        Apa yang ingin Anda lakukan?
        1. Lihat data
        2. Keluar
        ''')

        input_main = input('Mau pilih angka berapa?')
        if input_main == '1':
            func_read_data2()
        elif input_main == '2':
            break
        else:
            print("Anda salah!")

def func_admin():
    indexAdmin = namaadmin()
    passwordadmin(indexAdmin)

def namaadmin():
    namaAdmin = input("Tolong masukkan nama Anda! ")
    indexAdmin = 0
    for x in admin:
        if namaAdmin == x["Nama"]:
            return indexAdmin
    print("Data tidak ditemukan!")
    return namaadmin()

def passwordadmin(indexAdmin):
    while True:
        passwordAdmin = input("Tolong masukkan password yang sesuai!")
        if admin[indexAdmin]["Password"] == passwordAdmin:
            return func_main_data1()
        print('Password Anda salah!')
        return passwordadmin(indexAdmin)

def dashboard():
    while True:
        print('''Selamat datang! 
Jika Anda User tolong ketik angka 1. 
Jika Anda pengunjung ketik angka 2. 
Jika ingin keluar ketik angka 3.
''')
        Dashboard = input('Masukkan angka berapa yang ingin Anda pilih! ')
        if Dashboard == '1':
            func_admin()
        elif Dashboard == '2':
            func_main_data2()
        elif Dashboard == '3':
            break
        else:
            print("Tolong masukkan angka yang benar!")

dashboard()
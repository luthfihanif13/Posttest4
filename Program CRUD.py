#List penjualan ikan Luthfish Market

def login():
    print('login Luthfish Market')
    username = input('Username : ')
    passw = input('Password : ')
    if username == 'Luthfi' and passw == '210':
        print('Alhamdulillah Antum(Admin) telah login')
    elif username == 'Ahmad' and passw == '082':
        print('Alhamdulillah Antum(User) telah login')
    else:
        print('Silahkan memasukkan password/Username dengan benar')
        
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print('            Selamat datang di           ')
    print('             Luthfish market            ')
    print('             selamat belanja            ')
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')


ikan = {
    'Ikan Arwana'  : 1000000,
    'Ikan Pepper'  : 250000,
    'Ikan Nuptune' : 50000,
    'Ikan Clarion' : 75000,
    'Ikan Badut'   : 1000
}

#Fungsi
def list_menu():
    ikan
    for key, value in ikan.items():
        print(key, ': Rp', value)

def tambah():
    input_baru = input('masukan nama ikan: ')
    in_baru = int(input('Masukan harga ikan: '))
    ikan[input_baru] = in_baru

def update():
    input_baru = input('Update nama ikan: ')
    in_baru = int(input('Update harga ikan: '))
    ikan[input_baru] = in_baru

def delete():
    del ikan [input('apa yang mau dihapus: ')]

#program CRUD
def main_menu():
    while True:
        print('menu')
        print('1. List menu\n2. Tambah\n3. Update\n4. Hapus\n5. exit')
        pilih = input('Masukan pilihan : ')
        if pilih == '1':
            list_menu()
            print('\nTekan [Enter] untuk kembali')
            input()
        elif pilih == '2':
            tambah()
            print('\nTekan [Enter] untuk kembali')
            input()
        elif pilih == '3':
            update()
            print('\nTekan [Enter] untuk kembali')
            input()
        elif pilih == '4':
            delete()
            print('\nTekan [Enter] untuk kembali')
            input()
        elif pilih == '5':
            print('Antum telah keluar')
            break

def kasir():
    ikan
    for key, value in ikan.items ():
        print (key,":", value)
    pilih = ikan [input("masukkan ikan yang anda ingin beli :")]
    jumlah= int(input("Masukan jumlah ikan yang ingin dibeli: "))
    total=pilih * jumlah 
    haripembelian =input('hari pembelian: ')
    if haripembelian == 'senin':
        diskon=int(total*(10/100))
        total = total - diskon
        print('-Diskon 10 %-')
        print("Total Harga = ", "Rp.",total)
        Bayar=int(input("Jumlah Nominal Uang = Rp. ", ))
        Kembalian= (Bayar-total)
    elif haripembelian == 'kamis':
        diskon=int(total*(25/100))
        total = total - diskon
        print('-Diskon 25 %-')
        print("Total Harga = ", "Rp.",total)
        Bayar=int(input("Jumlah Nominal Uang = Rp. ", ))
        Kembalian= (Bayar-total)
    else:
        print('Maaf,anda tidak mendapatkan diskon')
        print("Total Harga = ", "Rp.",total)
        Bayar=int(input("Jumlah Nominal Uang = Rp. ", ))
        Kembalian= (Bayar-total)

    print("Uang Kembalian = ", "Rp.",Kembalian)
    pilihan=input("Apakah anda ingin order kembali y/t= ")
    if pilihan=="t":
      print('Terima Kasih Telah Berbelanja di Luthfish Market')
      print("Silahkan datang kembali")

while True : 
    login()
    print('Menu')
    print('1. data penjualan')
    print('2. kasir')
    print('3. exit')
    x = input('masukkan pilihan :')
    if x == "1" :
        main_menu ()
    elif x == "2" :
        kasir()
    elif x == '3':
      print('Antum telah keluar')
      print('selamat beristirahat')
      break
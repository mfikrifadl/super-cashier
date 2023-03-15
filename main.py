import time

list_transaction = {}
total_purchases = 0
check = False

def menu():
    """Fungsi untuk menampilkan daftar tugas.
    """

    print("-"*60)
    print("SELAMAT DATANG DI CASHIER ANDI")
    print("-"*60)
    print("1. Tambah Item Baru")
    print("2. Update Nama Item")
    print("3. Update Jumlah Item")
    print("4. Update Harga Item")
    print("5. Hapus Item")
    print("6. Reset List")
    print("7. Check Order")
    print("8. Hitung total belanja")
    print("9. Exit\n")

    choice = int(input('Masukkan Nomor Menu : '))
    global check

    try:
        if choice != 8 and choice != 7 :
            check = False

        if choice == 1:
            add_item()
        elif choice == 2:
            update_item_name()
        elif choice == 3:
            update_item_qty()
        elif choice == 4:
            update_item_price()
        elif choice == 5:
            delete_item()
        elif choice == 6:
            reset_transaction()
        elif choice == 7:
            check_order()
        elif choice == 8:
            total_price()
        elif choice == 9:
            print("-"*60)
            print("Terima kasih telah mengunjungi Cashier Andi.")
            print("-"*60)
            pass
        else:
            print("Input Anda Salah.\n")
            menu()
    except Exception as e:
        print(str(e))
        menu()

def getTransactionId(name_customer) :
    ts = time.time()
    return name_customer + str(ts)

def add_item() :
    item_name = input('Masukkan Nama Barang : ')
    item_name = item_name.lower()
    if check_name(item_name) :
        print("Nama item sudah digunakan")
    else :
        item_qty = int(input('Masukkan Jumlah Barang : '))
        item_price = int(input('Masukkan Harga Barang : '))
        list_transaction[item_name] = {'qty' : item_qty, 'price' : item_price}
        print("Barang berhasil ditambahkan!")
    menu()

def update_item_name() :
    item_name = input('Masukkan Nama Barang : ')
    item_name = item_name.lower()
    if check_name(item_name) :
        item_name_rev = input('Masukkan Nama Barang Update : ')
        list_transaction[item_name_rev] = list_transaction.pop(item_name)
        print("Barang berhasil diupdate!")
    else :
        print("Nama item tidak ada")
    menu()

def update_item_qty() :
    item_name = input('Masukkan Nama Barang : ')
    item_name = item_name.lower()
    if check_name(item_name) :
        item_qty_rev = int(input('Masukkan Jumlah Barang : '))
        list_transaction[item_name]['qty'] = item_qty_rev
        print("Barang berhasil diupdate!")
    else :
        print("Nama item tidak ada")
    menu()

def update_item_price() :
    item_name = input('Masukkan Nama Barang : ')
    item_name = item_name.lower()
    if check_name(item_name) :
        item_price_rev = int(input('Masukkan Harga Barang : '))
        list_transaction[item_name]['price'] = item_price_rev
        print("Barang berhasil diupdate!")
    else :
        print("Nama item tidak ada")
    menu()

def delete_item() :
    item_name = input('Masukkan Nama Barang : ')
    item_name = item_name.lower()
    if check_name(item_name) :
        del list_transaction[item_name]
        print("Barang berhasil dihapus!")
    else :
        print("Nama item tidak ada")
    menu()

def reset_transaction() :
    list_transaction.clear()
    print("Data berhasil direset!")
    menu()

def check_order() :
    if len(list_transaction) > 0 :
        global check
        global total_purchases

        print('-'*63)

        print("{:<2} {:<10} {:<2} {:<6} {:<10}".format('| No', ' | Nama Item', ' | Jumlah Item', ' | Harga/Item', ' | Total harga |'))
        print("{:<2} {:<10} {:<2} {:<6} {:<10}".format('|' + '-'*4, '|' + '-'*11, '|' + '-'*13, '|' + '-'*12, '|' + '-'*13 + '|'))
        no = 1
        total_purchases = 0
        check = True
        for x in list_transaction:
            total = (list_transaction[x]['price'] * list_transaction[x]['qty'])
            total_purchases += total
            print("{:1} {:^3} {:1} {:^10} {:1} {:^12} {:1} {:^11} {:1} {:^11} {:1}".format('|', str(no), '|', x, '|', str(list_transaction[x]['qty']), '|', str(list_transaction[x]['price']), '|', str(total), '|'))
            if x == '' or str(list_transaction[x]['qty']) == '' or str(list_transaction[x]['price']) == '' :
                check = False
            no += 1

        print('-'*63)

        if check :
            print("Pesanan sudah sesuai")
        else :
            print("Terdapat kesalahan input data")

    else :
        print("Harap masukkan item terlebih dahulu!")

    menu()

def total_price() :
    global check
    global total_purchases

    if check :
        discount = 0
        final_total_purchases = 0
        if total_purchases > 500000 :
            discount = 10
        elif total_purchases > 300000 :
            discount = 8
        elif total_purchases > 200000 :
            discount = 5
        
        final_total_purchases = total_purchases - (total_purchases * discount / 100)

        if(discount > 0) :
            print(f"Total belanjaan ID Pesanan {transaction_id} mendapatkan discount {discount}% menjadi Rp {final_total_purchases}")
        else :
            print(f"Total belanjaan ID Pesanan {transaction_id} adalah Rp {final_total_purchases}")
    else :
        print("Harap check order terlebih dahulu!")
    
    menu()

def check_name(name) :
    if name in list_transaction :
        return True
    else :
        return False

name_customer = input('Masukkan Nama Anda : ')
transaction_id = getTransactionId(name_customer)
menu()
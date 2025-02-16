## Toko Sabun

from tabulate import tabulate

list_produk = [{"sku": "FW001", "item_name": "Gentle Facial Cleanser", "brand": "GlowSkin", "category": "Face Wash", "price": 75000, "stock": 50}, {"sku": "FW002", "item_name": "Hydrating Face Wash", "brand": "DermaCare", "category": "Face Wash", "price": 95000, "stock": 40}, {"sku": "FW003", "item_name": "Tea Tree Acne Cleanser", "brand": "PureBeauty", "category": "Face Wash", "price": 89000, "stock": 35}, {"sku": "FW004", "item_name": "Brightening Foam Cleanser", "brand": "GlowSkin", "category": "Face Wash", "price": 99000, "stock": 30}, {"sku": "FW005", "item_name": "Vitamin C Face Wash", "brand": "DermaCare", "category": "Face Wash", "price": 105000, "stock": 25}, {"sku": "BW001", "item_name": "Aloe Vera Body Wash", "brand": "NatureGlow", "category": "Body Wash", "price": 120000, "stock": 35}, {"sku": "BW002", "item_name": "Coconut Milk Shower Gel", "brand": "Tropical Bliss", "category": "Body Wash", "price": 105000, "stock": 45}, {"sku": "BW003", "item_name": "Moisturizing Honey Body Wash", "brand": "GlowSkin", "category": "Body Wash", "price": 110000, "stock": 50}, {"sku": "BW004", "item_name": "Lavender Relaxing Body Wash", "brand": "PureBeauty", "category": "Body Wash", "price": 98000, "stock": 40}, {"sku": "BW005", "item_name": "Charcoal Detox Body Wash", "brand": "DermaCare", "category": "Body Wash", "price": 115000, "stock": 38}, {"sku": "HC001", "item_name": "Argan Oil Shampoo", "brand": "SilkySmooth", "category": "Hair Care", "price": 130000, "stock": 30}, {"sku": "HC002", "item_name": "Keratin Repair Conditioner", "brand": "HairRevive", "category": "Hair Care", "price": 140000, "stock": 25}, {"sku": "HC003", "item_name": "Tea Tree Anti-Dandruff Shampoo", "brand": "SilkySmooth", "category": "Hair Care", "price": 125000, "stock": 20}, {"sku": "HC004", "item_name": "Aloe & Coconut Hair Mask", "brand": "GlowSkin", "category": "Hair Care", "price": 135000, "stock": 22}, {"sku": "HC005", "item_name": "Biotin Strengthening Conditioner", "brand": "DermaCare", "category": "Hair Care", "price": 145000, "stock": 18}, {"sku": "FM001", "item_name": "Charcoal Detox Face Mask", "brand": "GlowSkin", "category": "Face Mask", "price": 85000, "stock": 50}, {"sku": "FM002", "item_name": "Hydrating Sheet Mask", "brand": "DermaCare", "category": "Face Mask", "price": 45000, "stock": 60}, {"sku": "FM003", "item_name": "Collagen Firming Face Mask", "brand": "PureBeauty", "category": "Face Mask", "price": 78000, "stock": 48}, {"sku": "FM004", "item_name": "Green Tea Calming Face Mask", "brand": "NatureGlow", "category": "Face Mask", "price": 67000, "stock": 55}, {"sku": "FM005", "item_name": "Vitamin E Nourishing Mask", "brand": "Tropical Bliss", "category": "Face Mask", "price": 72000, "stock": 52}]


def jeda():
    while True:
        jeda = str(input('tekan enter untuk melanjutkan'))
        return

def menampilkan_list_produk():
    # Ubah list produk ke format list of lists untuk tabulate
    # Library tabulate memang mengharuskan data harus berbentuk list dalam list
    data = []
    index = 0
    for produk in list_produk:
        data.append([
            index,  # Index produk
            produk["sku"],  # SKU produk
            produk["item_name"],  # Nama
            produk["brand"],  # Brand
            produk["category"],  # Kategori
            produk["price"],  # Harga
            produk["stock"], #Stock
        ])
        index += 1  # Increment index setiap kali loop
    # Cetak tabel
    print("Daftar produk\n")
    print(tabulate(data, headers=["SKU", "Nama", "Brand", "Kategori", "Harga", "Stock"], tablefmt="grid"))
    print(f"Saat ini terdapat {len(list_produk)} produk yang tersimpan di gudang")
    return

def filter_sku():
    while True :
        keyword = str(input('Masukkan keyword untuk filter berdasarkan SKU: '))
        if keyword == '':
            print('Harap mengisi kata kunci')
        elif keyword.isalnum() == False:
            print('SKU tidak bisa menggunakan spesial karakter')
        elif len(keyword) >= 5:
            print('Filter SKU tidak bisa lebih dari 5 karakter')
        elif keyword != '':
            break
    print(f'Hasil pencarian berdasarkan SKU dengan kata kunci: {keyword.upper()}\n===========================================================================================================================')
    data = []
    count = 0
    index = 0
    for produk in list_produk:
        if keyword.upper() in produk['sku'].upper():
            count += 1
            data.append([
                index,  # Index produk
                produk["sku"],  # SKU produk
                produk["item_name"],  # Nama
                produk["brand"],  # Brand
                produk["category"],  # Kategori
                produk["price"],  # Harga
                produk["stock"], #Stock
        ])
        index += 1
    if count == 0:
        print("Maaf kami tidak dapat menemukan hasil berdasarkan kata kunci yang digunakan")
        return
    else:
        print(tabulate(data, headers=["SKU", "Nama", "Brand", "Kategori", "Harga", "Stock"], tablefmt="grid"))
        print(f' ======================================= Filter Result ====================================== \n Terdapat {count} produk berdasarkan filter yang digunakan')
        return

def filter_brand():
    keyword = str(input('Masukkan keyword untuk filter berdasarkan brand: '))
    print(f'Hasil pencarian berdasarkan Brand dengan kata kunci: {keyword.lower()}\n===========================================================================================================================')
    data = []
    count = 0
    index = 0
    for produk in list_produk:
        if keyword.lower() in produk['brand'].lower():
            count += 1
            data.append([
                index,  # Index produk
                produk["sku"],  # SKU produk
                produk["item_name"],  # Nama
                produk["brand"],  # Brand
                produk["category"],  # Kategori
                produk["price"],  # Harga
                produk["stock"], #Stock
        ])
        index += 1
    if count == 0:
        print("Maaf kami tidak dapat menemukan hasil berdasarkan kata kunci yang digunakan")
        return
    else:
        print(tabulate(data, headers=["SKU", "Nama", "Brand", "Kategori", "Harga", "Stock"], tablefmt="grid"))
        print(f' ======================================= Filter Result ====================================== \n Terdapat {count} produk berdasarkan filter yang digunakan')
        return

def filter_nama():
    keyword = str(input('Masukkan keyword untuk filter berdasarkan nama: '))
    print(f'Hasil pencarian berdasarkan Nama Produk dengan kata kunci: {keyword.lower()}\n===========================================================================================================================')
    data = []
    count = 0
    index = 0
    for produk in list_produk:
        if keyword.lower() in produk['item_name'].lower():
            count += 1
            data.append([
                index,  # Index produk
                produk["sku"],  # SKU produk
                produk["item_name"],  # Nama
                produk["brand"],  # Brand
                produk["category"],  # Kategori
                produk["price"],  # Harga
                produk["stock"], #Stock
        ])
        index += 1
    if count == 0:
        print("Maaf kami tidak dapat menemukan hasil berdasarkan kata kunci yang digunakan")
        return
    else:
        print(tabulate(data, headers=["SKU", "Nama", "Brand", "Kategori", "Harga", "Stock"], tablefmt="grid"))
        print(f' ======================================= Filter Result ====================================== \n Terdapat {count} produk berdasarkan filter yang digunakan')
        return

def filter_kategori():
    keyword = str(input('Masukkan keyword untuk filter berdasarkan kategori: '))
    print(f'Hasil pencarian berdasarkan Nama Produk dengan kata kunci: {keyword.lower()}\n===========================================================================================================================')
    data = []
    count = 0
    index = 0
    for produk in list_produk:
        if keyword.lower() in produk['category'].lower():
            count += 1
            data.append([
                index,  # Index produk
                produk["sku"],  # SKU produk
                produk["item_name"],  # Nama
                produk["brand"],  # Brand
                produk["category"],  # Kategori
                produk["price"],  # Harga
                produk["stock"], #Stock
        ])
        index += 1
    if count == 0:
        print("Maaf kami tidak dapat menemukan hasil berdasarkan kata kunci yang digunakan")
        return
    else:
        print(tabulate(data, headers=["SKU", "Nama", "Brand", "Kategori", "Harga", "Stock"], tablefmt="grid"))
        print(f' ======================================= Filter Result ====================================== \n Terdapat {count} produk berdasarkan filter yang digunakan')
        return

def filter_harga():
    while True:
        try:
            while True:
                harga_bawah = int(input("Masukkan harga terendah: "))
                if harga_bawah >= 0:
                    break
                else:
                    print('Harga tidak boleh bersifat negatif')
            break
        except Exception as e:
            print('Harga hanya boleh berupa angka')

    while True:
        try:
            while True:
                harga_atas = int(input("Masukkan harga tertinggi: "))
                if harga_atas > harga_bawah:
                    break
                elif harga_atas == harga_bawah:
                    print('Harga tidak boleh sama dengan harga terendah')
                else :
                    print('Harga tidak boleh lebih rendah dari harga terendah')
            break
        except Exception as e:
            print('Harga hanya boleh berupa angka')

    print(f'Hasil pencarian berdasarkan harga {harga_bawah} - {harga_atas}\n===========================================================================================================================')
    data = []
    count = 0
    index = 0
    for produk in list_produk:
        if harga_bawah <= produk['price'] and harga_atas >= produk['price']:
            count += 1
            data.append([
                index,  # Index produk
                produk["sku"],  # SKU produk
                produk["item_name"],  # Nama
                produk["brand"],  # Brand
                produk["category"],  # Kategori
                produk["price"],  # Harga
                produk["stock"], #Stock
        ])
        index += 1
    if count == 0:
        print("Maaf kami tidak dapat menemukan hasil berdasarkan range harga yang dicari")
    else:
        while True:
            try:
                print('Urutkan berdasarkan :\n1. Harga Tertinggi\n2. Harga Terendah')
                choose_option = int(input("Masukkan pilihan: "))
                if choose_option > 2 or choose_option < 0 :
                    print('Pilihan tidak tersedia')
                elif choose_option == 1 :
                    sorted_data = sorted(data, key=lambda x: x[5], reverse=True)
                    print(tabulate(sorted_data, headers=["SKU", "Nama", "Brand", "Kategori", "Harga", "Stock"], tablefmt="grid"))
                    break
                elif choose_option == 2 :
                    sorted_data = sorted(data, key=lambda x: x[5], reverse=False)
                    print(tabulate(sorted_data, headers=["SKU", "Nama", "Brand", "Kategori", "Harga", "Stock"], tablefmt="grid"))
                    break
            except Exception as e:
                print('Pilihan hanya bisa berupa angka')  
    print(f' ======================================= Filter Result ====================================== \n Terdapat {count} produk berdasarkan filter yang digunakan')
    return

def filter_stock():
    while True:
        try:
            while True:
                stock_bawah = int(input("Masukkan stock terendah: "))
                if stock_bawah >= 0:
                    break
                else:
                    print('stock tidak boleh bersifat negatif')
            break
        except Exception as e:
            print('stock hanya boleh berupa angka')

    while True:
        try:
            while True:
                stock_atas = int(input("Masukkan stock tertinggi: "))
                if stock_atas > stock_bawah:
                    break
                elif stock_atas == stock_bawah:
                    print('stock tidak boleh sama dengan stock terendah')
                else :
                    print('stock tidak boleh lebih rendah dari stock terendah')
            break
        except Exception as e:
            print('stock hanya boleh berupa angka')

    print(f'Hasil pencarian berdasarkan stock {stock_bawah} - {stock_atas}\n===========================================================================================================================')
    data = []
    count = 0
    index = 0
    for produk in list_produk:
        if stock_bawah <= produk['stock'] and stock_atas >= produk['stock']:
            count += 1
            data.append([
                index,  # Index produk
                produk["sku"],  # SKU produk
                produk["item_name"],  # Nama
                produk["brand"],  # Brand
                produk["category"],  # Kategori
                produk["price"],  # stock
                produk["stock"], #Stock
        ])
        index += 1
    if count == 0:
        print("Maaf kami tidak dapat menemukan hasil berdasarkan range stock yang dicari")
    else:
        while True:
            try:
                print('Urutkan berdasarkan :\n1. Stock Tertinggi\n2. Stock Terendah')
                choose_option = int(input("Masukkan pilihan: "))
                if choose_option > 2 or choose_option < 0 :
                    print('Pilihan tidak tersedia')
                elif choose_option == 1 :
                    sorted_data = sorted(data, key=lambda x: x[6], reverse=True)
                    print(tabulate(sorted_data, headers=["SKU", "Nama", "Brand", "Kategori", "Harga", "Stock"], tablefmt="grid"))
                    break
                elif choose_option == 2 :
                    sorted_data = sorted(data, key=lambda x: x[6], reverse=False)
                    print(tabulate(sorted_data, headers=["SKU", "Nama", "Brand", "Kategori", "Harga", "Stock"], tablefmt="grid"))
                    break
            except Exception as e:
                print('Pilihan hanya bisa berupa angka')  
    print(f' ======================================= Filter Result ====================================== \n Terdapat {count} produk berdasarkan filter yang digunakan')
    return

def read_menu():
    while True:
        try:
            print('====================\nMenu Tampilkan Produk :\n====================\nTampilkan data produk berdasarkan :\n1. Tampilkan seluruh produk yang tersedia\n2. Tampilkan produk berdasarkan filter\n3. Kembali ke Menu Utama')
            choose_option = str(input('Masukkan pilihan yang diinginkan: '))
            if int(choose_option) < 1 or int(choose_option) > 3:
                print('''=============== ERROR ===============
Masukkan pilihan berdasarkan pilihan yang ada
=============== ERROR ===============''')       
            elif int(choose_option) == 1:
                if len(list_produk) == 0:
                    print('Saat ini gudang sedang tidak menyimpan produk apapun') 
                    jeda()
                else :
                    menampilkan_list_produk()
                    jeda()
            elif int(choose_option) == 2:
                filter_menu()
            elif int(choose_option) == 3:
                return
        except Exception as e:
            print('''=============== ERROR ===============
Pilihan hanya bisa berupa angka
=============== ERROR ===============''')


#list_produk = []

def filter_menu():
    while True:
        try:
            if len(list_produk) == 0:
                print('Saat ini gudang sedang tidak menyimpan produk apapun') 
                jeda()
                return
            else:
                print('====================\nMenu filter produk :\n====================\n1. Filter SKU\n2. Filter Nama\n3. Filter Brand\n4. Filter Kategori\n5. Filter Harga\n6. Filter Stock\n7. Kembali ke Menu Tampilkan produk')
                choose_option = int(input('Pilih filter berdasarkan: '))
                if choose_option < 1 or choose_option > 7:
                    print('''=============== ERROR ===============
Masukkan pilihan berdasarkan pilihan yang ada
=============== ERROR ===============''')
                elif choose_option == 1:
                    filter_sku()
                    jeda()
                elif choose_option == 2:
                    filter_nama()
                    jeda()
                elif choose_option == 3:
                    filter_brand()
                    jeda()
                elif choose_option == 4:
                    filter_kategori()
                    jeda()
                elif choose_option == 5:
                    filter_harga()
                    jeda()
                elif choose_option == 6:
                    filter_stock()
                    jeda()
                elif choose_option == 7:
                    return
        except Exception as e:
            print('''=============== ERROR ===============
Pilihan hanya dapat berupa angka
=============== ERROR ===============''')
                
def create_menu():
        while True:
            print('====================\nMenu Tambahkan Produk :\n====================')
            print('1. Tambah Produk\n2. Kembali ke Menu Utama')
            try:
                choose_option = int(input("Masukkan pilihan: "))
                if choose_option < 1 or choose_option > 2:
                    print('''=============== ERROR ===============
Masukkan sesuai pilihan yang ada
=============== ERROR ===============''')
                elif choose_option == 1 :
                    create_product()
                    jeda()
                elif choose_option == 2 :
                    return
            except Exception as e:
                print('''=============== ERROR ===============
Pilihan hanya dapat berupa angka
=============== ERROR ===============''')

def create_product():
    print('====================\nMenu Tambahkan Produk :\n====================')
    while True:
        sku = str(input("Masukkan SKU produk: "))
        sku = sku.replace(' ','')
        if len(sku) != 5:
            print('SKU harus memiliki 5 karakter')
        else:
            cek_SKU = lambda x: any(i['sku'] == x for i in list_produk)
            if cek_SKU(sku.upper()) == True:
                print('=============== ERROR ===============\nSKU sudah digunakan\n=============== ERROR ===============')
            else :
                while True:
                    nama = str(input("Masukkan nama produk: "))
                    cek_nama = nama.replace(' ','')
                    if cek_nama == '':
                        print('Nama tidak boleh dikosongkan')
                    else:
                        break
                while True:
                    brand = str(input("Masukkan brand produk: "))
                    cek_brand = brand.replace(' ','')
                    if cek_brand == '':
                        print('Brand tidak boleh dikosongkan')
                    else:
                        break
                while True:
                    kategori = str(input("Masukkan kategori produk: "))
                    cek_kategori = kategori.replace(' ','')
                    if cek_kategori == '':
                        print('Kategori tidak boleh dikosongkan')
                    else:
                        break
                while True:
                    try:
                        harga = int(input("Masukkan harga produk: "))
                        break
                    except Exception as e:
                        print('''=============== ERROR ===============\nTidak dapat memasukkan selain angka\n=============== ERROR ===============''')
                while True:
                    try:
                        stock = int(input("Masukkan stock produk: "))
                        break
                    except Exception as e:
                        print('''=============== ERROR ===============\nStock hanya dapat berupa angka\n=============== ERROR ===============''')

                new_product = {
                    'sku': sku.upper(),
                    'item_name': nama,
                    'brand': brand,
                    'category': kategori,
                    'price': harga,
                    'stock': stock,
                }
                confirmation_result = confirmation_option(f'Apakah anda ingin menambah produk {nama} dengan SKU {sku}?')
                if confirmation_result == True:
                    list_produk.append(new_product)     
                    print(f'Berhasil menambahkan produk {nama} dengan SKU {sku}')
                    return
                else:
                    break 

def delete_product():
    while True:
        sku_dihapus = str(input("Masukkan SKU produk yang ingin dihapus: "))
        if len(sku_dihapus) != 5:
            print('SKU harus memiliki 5 karakter') 
        else:
            break
    cek_produk = False
    indexing = 0
    for i in list_produk:
        if i['sku'] == sku_dihapus.upper():
            cek_produk = True
            confirmation_result = confirmation_option(f'Apakah anda ingin menghapus produk {i['sku']} {i['item_name']}?')
            if confirmation_result == True:
                del list_produk[indexing]
                print(f'Produk {i['sku']} {i['item_name']} berhasil dihapus')
                indexing += 1
        else:
            indexing += 1
    if  cek_produk == False:
        print("Produk tidak ditemukan")
        max_rekomendasi = 0
        isi_rekomendasi = ''
        indexing = 0
        sku_dihapus = sku_dihapus[1:4].upper()
        for i in list_produk:
            if  max_rekomendasi == 3:
                break
            elif sku_dihapus.upper() in list_produk[indexing]['sku']:
                isi_rekomendasi = isi_rekomendasi + list_produk[indexing]['sku'] + " - " +list_produk[indexing]['item_name'] + " | "
                indexing += 1
                max_rekomendasi += 1
            else:
                indexing += 1
        if isi_rekomendasi != '':
            print('Beberapa rekomendasi Produk yang mungkin anda cari')
            print(isi_rekomendasi)

def delete_menu():
    while True:
        print('====================\nMenu Hapus Produk\n====================')
        print('1. Hapus Produk\n2. Kembali ke Menu Utama')
        try:
            choose_option = int(input("Masukkan pilihan: "))
            if choose_option < 1 or choose_option > 2:
                print('''=============== ERROR ===============
Masukkan sesuai pilihan yang ada
=============== ERROR ===============''')
            elif choose_option == 1 :
                delete_product()
                jeda()
            elif choose_option == 2 :
                return
        except Exception as e:
            print('''=============== ERROR ===============
Pilihan hanya dapat berupa angka
=============== ERROR ===============''')
            
def update_menu():
    while True:
        print('====================\nMenu Update Produk\n====================')
        print('1. Update Produk\n2. Kembali ke Menu Utama')
        try:
            choose_option = int(input("Masukkan pilihan: "))
            if choose_option < 1 or choose_option > 2:
                print('''=============== ERROR ===============
Masukkan sesuai pilihan yang ada
=============== ERROR ===============''')
            elif choose_option == 1 :
                update_product()
                jeda()
            elif choose_option == 2 :
                return
        except Exception as e:
            print('''=============== ERROR ===============
Pilihan hanya dapat berupa angka
=============== ERROR ===============''')
                  
def confirmation_option(message):
    print(message)
    output = False
    while True:
        choose_option = str(input('Masukkan pilihan (Y/N): '))
        if choose_option.lower() == 'y':
            output = True
            return output
        elif choose_option.lower() == 'n':
            output = False
            return output
        else :
            print('Masukkan sesuai pilihan')

def update_product():
    while True:
        sku_diupdate = str(input("Masukkan SKU produk yang ingin diupdate: "))
        if len(sku_diupdate) != 5:
            print('SKU harus memiliki 5 karakter') 
        else:
            break
    cek_produk = False
    indexing = 0
    for i in list_produk:
        if i['sku'] == sku_diupdate.upper():
            cek_produk = True
            confirmation_result = confirmation_option(f'Apakah anda ingin mengupdate produk {i['sku']} {i['item_name']}?')
            if confirmation_result == True:
                while True:
                    nama = str(input("Masukkan nama produk: "))
                    cek_nama = nama.replace(' ','')
                    if cek_nama == '':
                        print('Nama tidak boleh dikosongkan')
                    else:
                        break
                while True:
                    brand = str(input("Masukkan brand produk: "))
                    cek_brand = brand.replace(' ','')
                    if cek_brand == '':
                        print('Brand tidak boleh dikosongkan')
                    else:
                        break
                while True:
                    kategori = str(input("Masukkan kategori produk: "))
                    cek_kategori = kategori.replace(' ','')
                    if cek_kategori == '':
                        print('Kategori tidak boleh dikosongkan')
                    else:
                        break
                while True:
                    try:
                        harga = int(input("Masukkan harga produk: "))
                        if harga > i['price']:
                            price_difference = abs(harga - i['price'])
                            difference_percentage = round(((harga - i['price']) / i['price']) *100 )
                        elif harga < i['price']:
                            price_difference = abs(i['price'] - harga)
                            difference_percentage = round(((i['price'] - harga) / harga *100 ))
                        if harga < 0:
                            print('Harga tidak bisa bersifat negatif')
                        elif harga == 0:
                            print('Harga tidak bisa 0')
                        elif difference_percentage >= 35:
                            konfirmasi_harga = confirmation_option(f'Terdapat perbedaan harga sebesar {price_difference} ({difference_percentage}%)\n Apakah ingin melanjutkan perubahan harga (Y/N)?')
                            if  konfirmasi_harga == True:
                                break
                        else:
                            break
                    except Exception as e:
                        print('''=============== ERROR ===============\nTidak dapat memasukkan selain angka\n=============== ERROR ===============''')
                while True:
                    try:
                        stock = int(input("Masukkan stock produk: "))
                        if stock < 0:
                            print('Stock tidak bisa bersifat negatif')
                        else:
                            break
                    except Exception as e:
                        print('''=============== ERROR ===============\nStock hanya dapat berupa angka\n=============== ERROR ===============''')
                list_produk[indexing].update({f'item_name':nama, f'brand': brand, f'category': kategori, f'price': harga, f'stock': stock})
                print(f'Produk {i['sku']} {i['item_name']} berhasil diudpate')
                indexing += 1
        else:
            indexing += 1
    if  cek_produk == False:
        print("Produk tidak ditemukan")
        max_rekomendasi = 0
        isi_rekomendasi = ''
        indexing = 0
        sku_diupdate = sku_diupdate[1:4].upper()
        for i in list_produk:
            if  max_rekomendasi == 3:   
                break
            elif sku_diupdate.upper() in list_produk[indexing]['sku']:
                isi_rekomendasi = isi_rekomendasi + list_produk[indexing]['sku'] + " - " +list_produk[indexing]['item_name'] + " | "
                indexing += 1
                max_rekomendasi += 1
            else:
                indexing += 1
        if isi_rekomendasi != '':
            print('Beberapa rekomendasi Produk yang mungkin anda cari')
            print(isi_rekomendasi)

def main_menu():
    while True:
        print("===========================================================================================================================\nSelamat datang dalam aplikasi Gudang Skin Care Purwaderma\n===========================================================================================================================")
        print("1. Cek inventory gudang")
        print("2. Menambah barang")
        print("3. Menghapus barang")
        print("4. Mengupdate barang")
        print("5. Keluar")
        pilihan_menu_utama = str(input("Masukkan angka sesuai pilihan yang diinginkan: "))
        if pilihan_menu_utama == "1":
            read_menu()
        elif pilihan_menu_utama == "2":
            create_menu()
        elif pilihan_menu_utama == "3":
            delete_menu()
        elif pilihan_menu_utama == "4":
            update_menu()
        elif pilihan_menu_utama == "5":
            print('Menutup aplikasi')
            break
        elif pilihan_menu_utama.isdigit() == False :
             print("============= ERROR =============\nFormat hanya bisa berisi angka\n============= ERROR =============")
        else :
             print("============= ERROR =============\nMasukkan hanya angka sesuai pilihan yang ada\n============= ERROR =============")

main_menu()
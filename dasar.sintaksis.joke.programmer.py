"""
semua sintaks dasar bahasa pemrograman terdiri dari:
1. Sekuensial: langkah berurutan
2. Percabangan: langkah melllompat jika kondisi terpenuhi
3. Perulangan: mengulang langkah yang sama berkali kali selama sampai kondisi terpenuhi
"""

#Sekuensial
print('Ibu berkata, "Pergi ke toko"')
print('Budi menjawab, "Baik, apa yanh harus saya lakukan di toko?"')
print('Ibu menjawab, "Beli satu botol susu, dan jika ada telur beli 6"')
print('Maka Budi berangkat ke toko')
print('Dan mulai berbelanja')
print('di toko, "Apa ada susu Bu?"')
print('Penjaga Toko,"Oh ada, mau beli berapa kaleng?"')
print('Budi menjawab: "1 kaleng bu"')
print('Budi bertanya lagi: "apa ada telur juga?"')
print('Telur ada, mau berapa?')
print('beli 6 butir telur bu, baik ini uangnya')
print('baik, ini kembaliannya, terima kasih ya')
print('Budi pun pulang kembali ke rumahnya dan menyerahkan barang belanjaan ke ibunya')

# Percabangan
jumlah_botol_susu = 173
jumlah_telor = 1587
print(f'Jumlah botol susu {jumlah_botol_susu} botol')
print(f'Jumlah telor {jumlah_telor} butir')

if jumlah_botol_susu >0:
    print('Budi mengecek harganya, dan ternyata uangnya cukup')
    if jumlah_telor == 0:
        print('Budi membeli 1 botol susu')
    else:
        print('Budi membeli 6 botol susu')

else:
    print('Budi tidak jadi membeli 1 botol susu')

print('Budi pulang ke rumah')
print('Menyampaikan hasilnya kepada Ibu')
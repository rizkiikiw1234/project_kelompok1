import matplotlib.pyplot as plt
from collections import defaultdict, Counter

def buat_grafik_produk_terlaris(data_produk, data_transaksi):
    jumlah_per_produk = Counter()
    for trx in data_transaksi:
        idp = trx['id_produk']
        jumlah_per_produk[idp] += trx['jumlah']

    produk = [data_produk[idp]['nama'] for idp in jumlah_per_produk.keys()]
    jumlah = list(jumlah_per_produk.values())

    plt.figure(figsize=(8,5))
    plt.bar(produk, jumlah, color='skyblue')
    plt.title('Produk Terlaris')
    plt.xlabel('Produk')
    plt.ylabel('Jumlah Terjual')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('img/grafik_produk_terlaris.png')
    plt.close()

def buat_grafik_kategori(data_produk, data_transaksi):
    transaksi_kategori = defaultdict(int)
    for trx in data_transaksi:
        kategori = data_produk[trx['id_produk']]['kategori']
        transaksi_kategori[kategori] += 1

    labels = list(transaksi_kategori.keys())
    sizes = list(transaksi_kategori.values())

    plt.figure(figsize=(6,6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Distribusi Penjualan per Kategori')
    plt.savefig('img/grafik_kategori.png')
    plt.close()

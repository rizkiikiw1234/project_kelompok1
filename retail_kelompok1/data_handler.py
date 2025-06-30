import csv
from collections import defaultdict, Counter

def load_data(file_path):
    data_produk = {}
    data_transaksi = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                id_produk = row['IDProduk']
                data_produk[id_produk] = {
                    'nama': row['Nama'],
                    'kategori': row['Kategori'],
                    'harga': int(row['Harga'])
                }
                data_transaksi.append({
                    'id_produk': id_produk,
                    'jumlah': int(row['Jumlah']),
                    'tanggal': row['Tanggal']
                })
    except FileNotFoundError:
        raise FileNotFoundError("File tidak ditemukan!")
    except Exception as e:
        raise Exception(f"Gagal memuat data: {e}")
    return data_produk, data_transaksi

def analisis_data(data_produk, data_transaksi):
    pendapatan = 0
    jumlah_per_produk = Counter()
    transaksi_per_kategori = defaultdict(int)

    for trx in data_transaksi:
        idp = trx['id_produk']
        jumlah = trx['jumlah']
        harga = data_produk[idp]['harga']
        kategori = data_produk[idp]['kategori']

        pendapatan += harga * jumlah
        jumlah_per_produk[idp] += jumlah
        transaksi_per_kategori[kategori] += 1

    id_terlaris = jumlah_per_produk.most_common(1)[0][0]
    nama_terlaris = data_produk[id_terlaris]['nama']

    return pendapatan, nama_terlaris, dict(transaksi_per_kategori)

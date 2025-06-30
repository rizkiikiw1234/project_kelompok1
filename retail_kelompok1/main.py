from data_handler import load_data, analisis_data
from visualization import buat_grafik_produk_terlaris, buat_grafik_kategori

if __name__ == "__main__":
    try:
        data_produk, data_transaksi = load_data("data/penjualan.csv")
        pendapatan, terlaris, transaksi_kategori = analisis_data(data_produk, data_transaksi)

        print("==============================")
        print(" APLIKASI ANALISIS PENJUALAN ")
        print("==============================")
        print(f"Total Pendapatan       : Rp {pendapatan:,}")
        print(f"Produk Terlaris        : {terlaris}")
        print("Transaksi per Kategori :")
        for kategori, jumlah in transaksi_kategori.items():
            print(f" - {kategori:<25}: {jumlah} transaksi")

        buat_grafik_produk_terlaris(data_produk, data_transaksi)
        buat_grafik_kategori(data_produk, data_transaksi)

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")



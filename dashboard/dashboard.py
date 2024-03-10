import streamlit as st
from streamlit.components.v1 import html as st_html
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Load Data
df_customer = pd.read_csv("data/customers_dataset.csv")
df_order_items = pd.read_csv("dashboard/order_items_clean.csv")
df_orders = pd.read_csv("dashboard/orders_clean.csv")
df_payment = pd.read_csv("data/order_payments_dataset.csv")

# # Mengelompokkan berdasarkan wilayah penjual dan menghitung jumlah penjual unik
# unique_sellers_by_state = df_order_items.groupby(by="seller_state")["seller_id"].nunique().sort_values(ascending=False)

# Exploratory Data Analysis
category_orders = df_order_items.groupby(by="product_category_name_english")["product_id"].count().reset_index()
category_orders = category_orders.rename(columns={"product_category_name_english": "category", "product_id": "orders"})

# Streamlit Dashboard
st.title("E-Commerce Public Dataset Overview Dashboard")
st.sidebar.header("Navigation")
# Buat peta opsi dengan ikon atau deskripsi
options = {
    "Home": "🏠 Home",
    "Pertanyaan 1": "📊 1. Best Selling Categories",
    "Pertanyaan 2": "📦 2. Cities with Most and Fewest Customers ",
    "Pertanyaan 3": "💰 3. Most Payment Type Used",
    "Pertanyaan 4": "📈 4. Sales Increase Analysis",
}

# Tampilkan sidebar dengan opsi yang telah diperbarui
selected_page = st.sidebar.radio("Go to", list(options.keys()), format_func=lambda page: options[page])


if selected_page == "Home":
    st.header("Selamat datang di E-Commerce Data Analysis Dashboard")
    st.subheader("E-Commerce Public Dataset")
    st.image("https://storage.googleapis.com/kaggle-datasets-images/55151/105464/d59245a7014a35a35cc7f7b721de4dae/dataset-cover.png?t=2018-09-21-16-21-21", caption="E-Commerce Image", use_column_width=True)
    # Tambahkan teks selamat datang dan deskripsi dataset di home page
    st.markdown(
        "Selamat datang! Ini adalah dataset publik e-commerce Brasil dari pesanan yang dibuat di Olist Store. Dataset ini memiliki informasi dari 100 ribu pesanan dari tahun 2016 hingga 2018 yang dibuat di beberapa pasar di Brasil. Fitur-fiturnya memungkinkan untuk melihat pesanan dari berbagai dimensi: mulai dari status pesanan, harga, pembayaran, dan kinerja pengiriman hingga lokasi pelanggan, atribut produk, dan akhirnya ulasan yang ditulis oleh pelanggan. Kami juga merilis set data geolokasi yang menghubungkan kode pos Brasil dengan koordinat lintang/lintang."
"        Ini adalah data komersial yang nyata, telah dianonimkan, dan referensi ke perusahaan dan mitra dalam teks ulasan telah diganti dengan nama-nama rumah besar Game of Thrones."
        "Translated with DeepL.com (free version)"
    )
    
    st.markdown(
        "Ada beberapa pertanyaan bisnis yang akan di selesaikan dengan visualisasi data, yaitu :\n"
        "1. Kota mana yang memiliki jumlah customer paling banyak dan paling sedikit? 📊 \n "
        "2. Berapa durasi rata-rata pengiriman paket terlama, dan dari kota mana ke kota mana paket tersebut dikirimkan? 📦\n"
        "3. Jenis Pembayaran tipe apa yang paling sering digunakan? 💰\n"
        "4. Pada bulan manakah terjadi peningkatan penjualan yang paling signifikan, dan apa faktor yang mungkin mempengaruhinya? 📈\n"
        "\nBuka Side Bar untuk melihat jawaban dari pertanyaan diatas."
    )

elif selected_page == "Pertanyaan 1":
    st.header("Pertanyaan 1: Kategori yang paling laris dan tidak laris")

    # Membuat subplot untuk menampilkan dua grafik bar
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(18, 6))

    # Warna untuk grafik bar
    colors = ["#4C72B0", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

    # Grafik bar untuk kategori terlaris
    sns.barplot(x="orders", y="category", data=category_orders.sort_values(by="orders", ascending=False).head(5), palette=colors, ax=ax[0])
    ax[0].set_ylabel(None)
    ax[0].set_xlabel("Number of Orders")  # Menambah label sumbu x
    ax[0].set_title("Top Categories", loc="center", fontsize=15)
    ax[0].tick_params(axis='y', labelsize=12)

    # Grafik bar untuk kategori sedikit diminati
    sns.barplot(x="orders", y="category", data=category_orders.sort_values(by="orders", ascending=True).head(5), palette=colors, ax=ax[1])
    ax[1].set_ylabel(None)
    ax[1].set_xlabel("Number of Orders")  # Menambah label sumbu x
    ax[1].invert_xaxis()
    ax[1].yaxis.set_label_position("right")
    ax[1].yaxis.tick_right()
    ax[1].set_title("Least Popular Categories", loc="center", fontsize=15)
    ax[1].tick_params(axis='y', labelsize=12)

    # Menampilkan judul utama
    st.pyplot(fig)  # Menggunakan st.pyplot untuk menampilkan plot pada dashboard Streamlit
    
    # Menambahkan conclusion
    st.subheader("\nConclusion: Kategori Barang yang Paling Diminati dan Paling Kurang Diminati")
    st.write("Berdasarkan analisis, kategori yang paling diminati oleh konsumen adalah bed_bath_table, menunjukkan minat tinggi dalam produk-produk untuk keperluan kamar tidur dan kamar mandi. Sebaliknya, kategori security dan service menjadi kategori paling rendah yang dapat mencerminkan kemungkinan keterbatasan atau kurangnya permintaan untuk barang-barang dalam kategori tersebut.")

elif selected_page == "Pertanyaan 2":
    # Visualisasi Distribusi Kota Customer
    st.header("Pertanyaan 2: Kota yang paling banyak dan kurang Customer")

    st.subheader("Kota dengan Customer Terbanyak:")
    top_customer_city = df_customer['customer_city'].value_counts().head(10)
    
    # Setel gaya seaborn untuk tampilan yang lebih menarik
    sns.set(style="whitegrid")

    # Buat gambar dan sumbu menggunakan matplotlib
    fig_top_customer = plt.figure(figsize=(10, 6))

    # Buat bar plot untuk top 10 sebaran pelanggan berdasarkan kota
    sns.barplot(x=top_customer_city.values, y=top_customer_city.index, palette='plasma')
    plt.title('Top 10 Sebaran Pelanggan Berdasarkan Kota', fontsize=12)
    plt.xlabel('Jumlah Pelanggan', fontsize=10)
    plt.ylabel('Kota', fontsize=10)

    # Tampilkan plot pertama pada dashboard Streamlit
    st.pyplot(fig_top_customer)

    st.subheader("Kota dengan Customer Paling Sedikit:")
    tail_customer_city = df_customer['customer_city'].value_counts().tail(10)

    # Setel ukuran gambar untuk visualisasi tail
    fig_tail_customer = plt.figure(figsize=(10, 6))

    # Buat bar plot untuk tail 10 sebaran pelanggan berdasarkan kota
    sns.barplot(x=tail_customer_city.values, y=tail_customer_city.index, palette='plasma')
    plt.title('Tail 10 Sebaran Pelanggan Berdasarkan Kota', fontsize=12)
    plt.xlabel('Jumlah Pelanggan', fontsize=10)
    plt.ylabel('Kota', fontsize=10)

    # Rotasi label pada sumbu y untuk meningkatkan kejelasan
    plt.xticks(rotation=45)

    # Tampilkan plot kedua pada dashboard Streamlit
    st.pyplot(fig_tail_customer)

    # Menambahkan conclusion
    st.subheader("Conclusion: Kota yang memiliki jumlah customer paling banyak dan paling sedikit")
    st.write("Sao Paulo menjadi kota dengan jumlah pelanggan paling tinggi, mencapai hampir 16.000 orang. Sebaliknya, lebih dari 5 kota hanya memiliki 1 pelanggan. Diperlukan upaya untuk meningkatkan jumlah pelanggan di kota-kota tersebut agar tidak terjadi penurunan di masa mendatang. Selain itu, perlu dilakukan penyelidikan lebih lanjut untuk memahami penyebab rendahnya jumlah pelanggan dari beberapa kota.")


# Menambahkan blok kode untuk pertanyaan 3 pada halaman yang dipilih
elif selected_page == "Pertanyaan 3":
    st.header("Pertanyaan 3: Analisis Pembayaran yang Paling Sering Digunakan")

    # Mengelompokkan berdasarkan jenis pembayaran dan menghitung jumlah pesanan unik
    unique_orders_by_payment = df_payment.groupby(by="payment_type")["order_id"].nunique().sort_values(ascending=False)

    # Menampilkan distribusi jumlah pesanan unik berdasarkan jenis pembayaran di Streamlit
    st.subheader("Distribusi jenis pembayaran berdasarkan hasil penjualannya")
    fig, ax = plt.subplots(figsize=(8, 5))

    # Pilih warna dari palet warna seaborn
    colors = sns.color_palette('viridis', len(unique_orders_by_payment))

    # Membuat bar chart dengan warna yang ditentukan
    unique_orders_by_payment.plot(kind='bar', color=colors, ax=ax)

    # Menambahkan judul dan label sumbu
    ax.set_title('Distribusi Jumlah Pesanan Unik Berdasarkan Jenis Pembayaran', fontsize=10)
    ax.set_xlabel('Jenis Pembayaran', fontsize=8)
    ax.set_ylabel('Jumlah Pesanan Unik', fontsize=8)

    # Menambahkan label pada setiap batang dengan nilai yang sesuai
    for i, value in enumerate(unique_orders_by_payment):
        ax.text(i, value + 5, f'{value}', ha='center', va='bottom', fontsize=10, color='black')

    # Menambahkan rotasi pada label sumbu x
    ax.set_xticklabels(unique_orders_by_payment.index, rotation=35, ha='right')

    # Menghilangkan kotak sekeliling plot
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    # Menampilkan plot menggunakan Streamlit
    st.pyplot(fig)

    st.subheader("Conclusion: Pembayaran yang paling sering digunakan saat transaksi adalah credit_card")
    st.write("Credit card dipakai hampir 80.000 transaksi dalam rentang waktu 2016-2018. Sebaliknya, penggunaan debit_card sudah mulai jarang dipakai oleh khalayak umum.")

    
elif selected_page == "Pertanyaan 4":
    st.header("Bulan terjadi peningkatan penjualan yang paling signifikan dan faktor yang mungkin mempengaruhinya")

    # Mengelompokkan data berdasarkan bulan dan tahun serta menghitung jumlah order_id yang unik
    monthly_sales = df_orders.groupby(by=["month", "year"])["order_id"].nunique().reset_index()

    # Mengonversi kolom "month" ke format tanggal menggunakan pd.to_datetime
    monthly_sales["month"] = pd.to_datetime(monthly_sales["month"], format='%m-%Y')

    # Setel ukuran gambar
    plt.figure(figsize=(12, 6))

    # Buat line plot menggunakan seaborn dengan nuansa 'dark' dan marker 'o'
    ax = sns.lineplot(x='month', y='order_id', data=monthly_sales, estimator=None, linewidth=3, color='darkblue', marker='o')

    # Setel posisi x-ticks agar sesuai dengan nilai bulan
    ax.set(xticks=monthly_sales.month.values)

    # Atur judul dan label sumbu
    plt.title("Sales Growth Trend", loc="center", fontsize=14)
    plt.ylabel("Total Orders")
    plt.xlabel(None)

    # Matikan grid pada sumbu y
    ax.grid(False)

    # Rotasi label bulan agar lebih mudah dibaca
    for tick in ax.get_xticklabels():
        tick.set_rotation(45)

    # Menampilkan plot
    st.pyplot(plt)

    # Menambahkan conclusion
    st.subheader("Conclusion: Bulan dengan Peningkatan Penjualan Tertinggi")
    st.write("Analisis menunjukkan bahwa bulan November 2017 menjadi bulan dengan penjualan tertinggi. Tentunya tanggal akhir November 2017 mungkin menunjukkan adanya acara promosi atau penawaran khusus yang memicu peningkatan signifikan dalam aktivitas pembelian.")


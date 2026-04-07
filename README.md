# logistics-quickwin-app

Glosarium Istilah Logistik untuk Aplikasi Quick-Win Analytics
A
Aging Hours

Jumlah jam sejak shipment dibuat (order_time) sampai waktu sekarang atau sampai shipment selesai.
Dipakai untuk melihat paket yang terlalu lama belum selesai.

Aging Bucket

Kelompok umur shipment berdasarkan durasi, misalnya:

0–24 jam
24–48 jam
48–72 jam

72 jam

Dipakai untuk memantau penumpukan shipment.

Arrived Hub Time

Waktu saat shipment tiba di hub transit / gateway.

Arrived Origin Station Time

Waktu saat shipment tiba di station/cabang asal setelah pickup.

AWB / AWB Number

Air Waybill Number atau nomor resi / nomor pengiriman unik untuk tiap shipment.
Di aplikasi kamu disimpan sebagai awb_no.

B
Bottleneck

Titik hambatan dalam alur logistik yang menyebabkan keterlambatan, penumpukan, atau penurunan performa.
Contohnya:

hub terlalu lama memproses shipment
station tertentu sering telat pickup
linehaul miss cut-off
Business Segment / Shipper Segment

Kategori pengirim, misalnya:

Enterprise
SME
Marketplace

Dipakai untuk analisis performa per jenis customer/pengirim.

C
Cache

Mekanisme penyimpanan sementara hasil query agar app lebih cepat dan tidak selalu query ulang ke database.

Chargeable Weight

Berat yang dipakai untuk perhitungan biaya pengiriman.
Biasanya nilai terbesar antara:

berat aktual (weight_kg)
berat volumetrik (volumetric_weight_kg)
Control Tower

Tampilan dashboard eksekutif untuk memonitor operasional logistik end-to-end dari level manajemen.

Courier

Petugas yang menangani pickup atau delivery shipment.

Courier Assigned Time

Waktu saat shipment/pickup task sudah di-assign ke kurir.

Current Status

Status terkini shipment, misalnya:

Delivered
In Transit
At Hub
Out For Delivery
Failed Pickup
Return To Sender
D
Declared Value

Nilai barang yang dideklarasikan oleh pengirim.
Sering digunakan untuk referensi risiko, asuransi, atau prioritas penanganan.

Delay

Keterlambatan dibanding SLA atau target operasional.

Delay Root Cause

Penyebab utama keterlambatan.
Di aplikasi kamu bisa dibucket seperti:

First Mile Delay
Hub Bottleneck
Remote Area
Last Mile Delay
Delivery Exception
Delivered Time

Waktu shipment benar-benar diterima oleh customer.

Delivery Attempts

Jumlah percobaan pengantaran ke penerima.

Delivery Exception

Masalah saat proses delivery, misalnya:

customer tidak ada
alamat salah
customer minta reschedule
Destination Hub

Hub/gateway tujuan sebelum shipment masuk proses final delivery.

Destination Region

Wilayah tujuan shipment.

Destination Station

Station/cabang tujuan yang menangani last mile.

Direct Connection

Koneksi database langsung ke PostgreSQL tanpa pooler. Biasanya lebih cocok untuk migration atau admin task.

Dwell Time

Durasi shipment “diam” atau tertahan di suatu titik proses.
Di app kamu ada:

dwell_origin_hours
dwell_hub_hours
Dwell Hub Hours

Lama shipment tertahan di hub.

Dwell Origin Hours

Lama shipment tertahan di station asal sebelum lanjut ke tahap berikutnya.

E
Engine (SQLAlchemy Engine)

Objek koneksi database di Python yang dipakai untuk berkomunikasi dengan Neon/PostgreSQL.

Estimated Cost

Estimasi biaya operasional shipment.
Dipakai untuk melihat exposure cost, exception cost, atau cost-to-serve.

Exception

Kondisi tidak normal yang mengganggu proses shipment.
Contoh:

damaged
lost
invalid address
capacity delay
weather delay
Exception Flag

Penanda apakah shipment mengalami exception atau tidak.

Exception Monitoring

Modul dashboard yang fokus memantau shipment bermasalah.

Exception Type

Jenis exception yang dialami shipment.

Executive KPI

Indikator utama untuk manajemen, misalnya:

total shipments
OTD %
pickup on-time %
exceptions
aging >72h
F
Failed Delivery

Pengiriman gagal diselesaikan ke penerima.

Failed Delivery Flag

Penanda apakah shipment mengalami delivery failure.

Failed Delivery Reason

Alasan delivery gagal, misalnya:

customer not home
invalid address
customer reschedule
remote area delay
cash issue
Failed Pickup

Pickup dari seller/pengirim gagal dilakukan.

Failed Pickup Flag

Penanda apakah pickup gagal.

Failed Pickup Reason

Penyebab pickup gagal, misalnya:

shipper not ready
address not found
capacity full
schedule miss
shipper closed
First Mile

Tahap awal logistik, dari shipment dibuat sampai paket masuk ke jaringan origin station/hub.

First Mile SLA

Pengukuran SLA untuk proses awal, terutama pickup dan first scan.

First Scan

Scan pertama paket setelah pickup atau saat masuk station awal.

First Scan Timeliness

Kecepatan first scan setelah pickup.
Biasanya dihitung dalam menit.

First Scan Timeliness Min

Durasi menit dari pickup sampai first scan.

G
GitHub

Tempat menyimpan source code dan file project.
Dalam konteks app kamu, file dummy CSV bisa disimpan di repo GitHub lalu dibaca oleh Streamlit.

Glossary

Daftar istilah beserta definisinya untuk memudahkan pemahaman user atau client.

H
Hub

Titik transit/logistics center tempat shipment dikonsolidasikan, diproses, lalu diteruskan ke node berikutnya.

Hub Bottleneck

Kondisi saat hub menjadi titik kemacetan proses, biasanya terlihat dari dwell time tinggi atau backlog.

I
In Transit

Shipment sedang dalam perjalanan antar node logistik dan belum sampai ke tahap final delivery.

Index (Database Index)

Struktur database untuk mempercepat query pada kolom tertentu.

Invalid Address

Alamat tidak lengkap, salah, atau tidak dapat diproses oleh operasi.

L
Lane Type

Jenis rute shipment:

Intra-Region = dalam wilayah yang sama
Inter-Region = antar wilayah
Last Mile

Tahap akhir pengiriman dari station/hub tujuan ke customer.

Last Scan Location

Lokasi scan terakhir shipment.

Late Reason Bucket

Kategori penyebab keterlambatan yang disederhanakan untuk analisis.

Linehaul

Transport utama antar station/hub/gateway, biasanya truk antar kota atau perpindahan antar node besar.

Load / Seed Data

Proses memasukkan data awal ke database.
Di app kamu, page Seed Database dipakai untuk upload dummy CSV ke Neon.

M
Marketplace

Segmen pengirim yang berasal dari ekosistem e-commerce/platform online.

Missed Cut-Off

Kondisi saat shipment tidak berhasil masuk keberangkatan sesuai batas waktu operasional.

N
Neon

Layanan PostgreSQL berbasis cloud yang kamu gunakan sebagai database utama aplikasi.

NullPool

Konfigurasi SQLAlchemy untuk mematikan pooling di sisi aplikasi, berguna jika database sudah memakai pooler sendiri.

O
On-Time Delivery (OTD)

Pengiriman yang selesai sesuai atau sebelum promised_delivery_time.

On-Time Delivery Flag

Penanda apakah shipment delivered on time atau tidak.

OperationalError

Jenis error SQLAlchemy/psycopg2 yang menunjukkan masalah koneksi atau operasi database.

Order Time

Waktu shipment dibuat di sistem.

Origin Hub

Hub/gateway asal tempat shipment diproses sebelum lanjut ke node berikutnya.

Origin Region

Wilayah asal shipment.

Origin Station

Station/cabang asal yang menerima shipment pertama kali setelah pickup.

Out For Delivery (OFD)

Status saat shipment sudah dibawa kurir untuk diantar ke customer.

Out For Delivery Time

Waktu shipment mulai masuk proses last mile aktif.

P
Pandas

Library Python yang dipakai untuk membaca CSV, mengolah data, dan mengirim data ke database.

Payment Type

Jenis pembayaran shipment, misalnya:

Prepaid
COD
Pooled Connection

Koneksi ke database yang melalui connection pooler.
Cocok untuk app web seperti Streamlit.

PostgreSQL

Database relasional yang digunakan di Neon.

Promised Delivery Time

Waktu target maksimum shipment harus selesai delivered.

Promised SLA Hours

Target SLA dalam satuan jam.

Pickup

Proses pengambilan paket dari pengirim/seller.

Pickup Actual Time

Waktu pickup benar-benar terjadi.

Pickup On-Time Flag

Penanda apakah pickup selesai dalam batas SLA atau tidak.

Pickup Requested Time

Waktu saat request pickup dibuat.

Pickup SLA Hours

Batas jam maksimal untuk pickup sejak request dibuat.

Pool Pre Ping

Fitur SQLAlchemy untuk mengecek apakah koneksi masih hidup sebelum dipakai.

Pool Recycle

Pengaturan SQLAlchemy untuk mendaur ulang koneksi setelah beberapa waktu agar tidak memakai koneksi stale.

Q
Query

Perintah SQL untuk mengambil data dari database.

Quick Win Solution

Solusi analytics yang cepat dibuat, mudah dipahami, dan langsung menunjukkan value bisnis.

R
Region

Wilayah geografis operasional, misalnya:

Jabodetabek
West Java
Central Java
East Java
Outer Java
Replace (if_exists='replace')

Mode upload data yang akan menghapus tabel lama lalu membuat ulang isi tabel dengan data baru.

Repo

Repository GitHub tempat source code dan file data disimpan.

Return To Sender (RTS)

Shipment dikembalikan ke pengirim karena gagal diselesaikan ke customer.

RTS Flag

Penanda apakah shipment mengalami return to sender.

RTS Reason

Alasan shipment dikembalikan ke pengirim.

Run Query

Fungsi helper untuk mengeksekusi query SQL dari page dashboard.

S
Schema

Struktur logis dalam database tempat tabel disimpan, misalnya public.

Seed Database Page

Halaman Streamlit internal yang dipakai untuk mengisi data dummy ke Neon.

Service Type

Jenis layanan pengiriman, misalnya:

Same Day
Next Day
Regular
Shipment

Satu unit transaksi pengiriman.

Shipment Aging

Analisis umur shipment yang belum selesai.

Shipment Event Log

Tabel log peristiwa shipment secara berurutan, seperti:

Shipment Created
Pickup Requested
Picked Up
Arrived Hub
Delivered
Shipment ID

ID unik internal shipment.

Shipment Master

Tabel utama satu baris per shipment yang dipakai untuk dashboard.

Shipment Revenue

Pendapatan shipment.

Shipper

Pihak pengirim barang.

Shipper ID

ID unik pengirim.

Shipper Name

Nama pengirim.

Shipper Segment

Kategori pengirim:

Enterprise
SME
Marketplace
SLA

Service Level Agreement — target atau standar waktu layanan.

SQLAlchemy

Library Python untuk koneksi dan operasi database.

Station

Cabang atau node operasional logistik yang menangani pickup, intake, sort, atau delivery.

Status Category

Kategori besar status shipment, misalnya:

Open
Closed
Exception
RTS
Streamlit

Framework Python untuk membuat aplikasi dashboard interaktif.

Streamlit Cloud

Layanan hosting Streamlit yang kamu pakai untuk deploy app.

T
Tab / Page

Halaman-halaman modul di Streamlit, misalnya:

Executive Control Tower
First Mile SLA
Shipment Aging
Exception Monitoring
to_sql

Fungsi pandas untuk upload DataFrame ke database.

Tracking Event

Peristiwa yang tercatat sepanjang lifecycle shipment.

V
Vehicle Type

Jenis kendaraan operasional, misalnya:

Bike
Van
Truck
Volumetric Weight

Berat berdasarkan dimensi paket, bukan berat aktual.
Dipakai untuk billing jika lebih besar dari berat aktual.

W
Weight KG

Berat aktual paket dalam kilogram.

Warehouse / Facility

Fasilitas operasional untuk penyimpanan, transit, atau proses shipment.
Dalam app kamu lebih banyak direpresentasikan sebagai station atau hub.

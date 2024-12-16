import mysql.connector

# Fungsi untuk menentukan kategori tekanan darah
def kategori_tekanan_darah(sistolik, diastolik):
    if sistolik < 120 and diastolik < 80:
        return "Normal", "Kategori ini menunjukkan tekanan darah yang sehat. Tekanan darah sistolik (angka atas) kurang dari 120 mmHg dan tekanan darah diastolik (angka bawah) kurang dari 80 mmHg. Ini adalah kondisi normal di mana jantung memompa darah dengan tekanan yang ideal, sehingga risiko penyakit jantung atau stroke sangat rendah."
    elif 120 <= sistolik <= 129 and diastolik < 80:
        return "Prehipertensi / Elevasi", "Kategori ini menunjukkan tekanan darah yang sedikit lebih tinggi dari normal, tetapi belum mencapai level hipertensi. Tekanan sistolik berada di antara 120 hingga 129 mmHg, sementara tekanan diastolik tetap di bawah 80 mmHg. Meskipun tidak dikategorikan sebagai hipertensi, tekanan darah dalam kisaran ini dapat berisiko berkembang menjadi hipertensi jika tidak diperhatikan atau jika gaya hidup tidak sehat terus berlanjut."
    elif 130 <= sistolik <= 139 or 80 <= diastolik <= 89:
        return "Hipertensi Tingkat 1", "Kategori ini mengindikasikan tekanan darah yang lebih tinggi dari normal, tetapi masih dalam batas yang dapat dikelola dengan perubahan gaya hidup dan, dalam beberapa kasus, obat-obatan. Tekanan sistolik antara 130 hingga 139 mmHg atau tekanan diastolik antara 80 hingga 89 mmHg. Pada kondisi ini, risiko masalah jantung, stroke, dan gangguan ginjal meningkat, dan perubahan gaya hidup serta pengobatan dapat membantu mengelola kondisi ini."
    elif sistolik >= 140 or diastolik >= 90:
        return "Hipertensi Tingkat 2", "Kategori ini menunjukkan hipertensi yang lebih parah, dengan tekanan darah sistolik 140 mmHg atau lebih, atau tekanan darah diastolik 90 mmHg atau lebih. Hipertensi tingkat 2 memerlukan perhatian medis segera, karena kondisi ini meningkatkan risiko terkena penyakit jantung dan stroke. Sering kali, pengobatan medis dan perubahan gaya hidup diperlukan untuk mengontrol tekanan darah."
    elif sistolik > 180 or diastolik > 120:
        return "Krisis Hipertensi", "Kategori ini adalah kondisi darurat medis yang membutuhkan perhatian segera. Tekanan darah sangat tinggi, yaitu lebih dari 180 mmHg untuk sistolik atau lebih dari 120 mmHg untuk diastolik. Krisis hipertensi adalah kondisi yang sangat berbahaya karena dapat menyebabkan kerusakan pada organ vital seperti otak, jantung, ginjal, atau mata. Seseorang dengan kondisi ini memerlukan perawatan medis segera untuk menghindari komplikasi serius, termasuk stroke atau gagal jantung."
    else:
        return "Data tidak valid", "Data yang dimasukkan tidak valid. Harap masukkan nilai yang benar."

# Fungsi untuk menyimpan hasil ke database
def simpan_ke_database(sistolik, diastolik, kategori, deskripsi):
    try:
        # Membuka koneksi ke database MySQL
        conn = mysql.connector.connect(
            host="localhost",       # Alamat server MySQL
            user="root",            # Username MySQL
            password="",    # Password MySQL
            database="tekanan_darah"  # Nama database yang digunakan
        )
        cursor = conn.cursor()

        # Query untuk menyimpan data
        query = "INSERT INTO hasil_tekanan_darah (sistolik, diastolik, kategori, deskripsi) VALUES (%s, %s, %s, %s)"
        values = (sistolik, diastolik, kategori, deskripsi)

        cursor.execute(query, values)
        conn.commit()  # Menyimpan perubahan

        print("Data berhasil disimpan ke database.")
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

# Fungsi utama untuk kalkulasi dan input
def main():
    print("Kalkulator Kategori Tekanan Darah")

    try:
        sistolik = int(input("Masukkan tekanan sistolik (mmHg): "))
        diastolik = int(input("Masukkan tekanan diastolik (mmHg): "))
    except ValueError:
        print("Harap masukkan nilai numerik yang valid.")
        return

    kategori, deskripsi = kategori_tekanan_darah(sistolik, diastolik)

    # Tampilkan hasil kategori dan deskripsi
    print(f"Kategori tekanan darah Anda: {kategori}")
    print(f"Deskripsi: {deskripsi}")

    # Simpan hasil ke database
    simpan_ke_database(sistolik, diastolik, kategori, deskripsi)

if __name__ == "__main__":
    main()
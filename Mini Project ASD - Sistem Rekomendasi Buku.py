import random, os, time
os.system("cls")
class Buku:
    def __init__(self, id, judul, penulis, tahun, genre, rating, terjual):
        self.id = id
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun
        self.genre = genre
        self.rating = rating
        self.terjual = terjual

    # Method untuk menampilkan informasi buku
    def display_info(self):
        print(f"ID: {self.id}")
        print(f"Judul buku: {self.judul}")
        print(f"Penulis: {self.penulis}")
        print(f"Tahun: {self.tahun}")
        print(f"Genre: {self.genre}")
        print(f"Rating: {self.rating}")
        print(f"Terjual: {self.terjual} Copy")

# Membuat instance dari kelas Book
Daftar_Buku = [
    Buku(1, "The Shining", "Stephen King", 1977, "Horror", 4.5, random.randint(100, 1000)),
    Buku(2, "Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 1997, "Fantasy", 4.8, random.randint(100, 1000)),
    Buku(3, "Good Omens", "Terry Pratchett & Neil Gaiman", 1990, "Comedy", 4.3, random.randint(100, 1000)),
    Buku(4, "It", "Stephen King", 1986, "Horror", 4.7, random.randint(100, 1000)),
    Buku(5, "The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy", 4.6, random.randint(100, 1000)),
    Buku(6, "Bridget Jones's Diary", "Helen Fielding", 1996, "Comedy", 4.0, random.randint(100, 1000)),
    Buku(7, "Dracula", "Bram Stoker", 1897, "Horror", 4.4, random.randint(100, 1000)),
    Buku(8, "A Game of Thrones", "George R.R. Martin", 1996, "Fantasy", 4.9, random.randint(100, 1000)),
    Buku(9, "The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979, "Comedy", 4.2, random.randint(100, 1000)),
    Buku(10, "Frankenstein", "Mary Shelley", 1818, "Horror", 4.6, random.randint(100, 1000))
]


# Fungsi untuk menampilkan menu admin
def menu_admin():
    print("\n\033[1;36m╭──────────────────────────────────────────────────────────────────────╮\033[0m")
    print("\033[1;36m│\033[0;94m                              Menu Admin                              \033[1;36m│\033[0m")
    print("\033[1;36m├──────────────────────────────────────────────────────────────────────┤\033[0m")
    print("\033[92m│ 1. 📚 Tambah Buku                                                    │\033[0m")
    print("\033[92m│ 2. 📝 Edit Buku                                                      │\033[0m")
    print("\033[92m│ 3. ❌ Hapus Buku                                                     │\033[0m")
    print("\033[92m│ 4. 📖 Lihat Daftar Buku                                              │\033[0m")
    print("\033[92m│ 5. 🏠 Kembali ke Menu Utama                                          │\033[0m")
    print("\033[1;36m╰──────────────────────────────────────────────────────────────────────╯\033[0m")

    pilihan = input("\033[3;32mMasukkan pilihan Anda: \033[0m")

    if pilihan == "1":
        tambah_buku()
    elif pilihan == "2":
        edit_buku()
    elif pilihan == "3":
        hapus_buku()
    elif pilihan == "4":
        lihat_daftar_buku()
    elif pilihan == "5":
        print("\033[92mKembali ke Menu Utama...\033[0m")
        time.sleep(2)
        main()
    else:
        print("\033[91mPilihan tidak valid. Silakan coba lagi.\033[0m")


def tambah_buku():
    print("\033[0;31m Tambah Buku \033[0;31m")
    # Mendapatkan input dari pengguna untuk informasi buku baru
    id = int(input("ID: "))
    judul = input("Judul: ")
    penulis = input("Penulis: ")
    tahun = int(input("Tahun: "))
    genre = input("Genre: ")
    rating = float(input("Rating: "))
    terjual = int(input("Terjual: "))
    
    # Membuat objek Buku baru dan menambahkannya ke daftar buku
    Daftar_Buku.append(Buku(id, judul, penulis, tahun, genre, rating, terjual))
    time.sleep(1)
    print("\033[0;32m Buku berhasil ditambahkan! \033[0m")
    menu_admin()

# Fungsi untuk mengedit informasi buku
def edit_buku():
    print("Edit Buku")
    id_buku = int(input("\033[92mMasukkan ID buku yang ingin di edit: \033[0m"))
    # Mencari buku berdasarkan ID
    for buku in Daftar_Buku:
        if buku.id == id_buku:
            # Mendapatkan input baru dari pengguna
            judul_baru = input("Judul baru: ")
            penulis_baru = input("Penulis baru: ")
            tahun_baru = int(input("Tahun baru: "))
            genre_baru = input("Genre baru: ")
            rating_baru = float(input("Rating baru: "))
            terjual_baru = int(input("Terjual baru: "))
            
            # Mengupdate informasi buku
            buku.judul = judul_baru
            buku.penulis = penulis_baru
            buku.tahun = tahun_baru
            buku.genre = genre_baru
            buku.rating = rating_baru
            buku.terjual = terjual_baru
            print("\033[0;32m Informasi buku berhasil diupdate!\033[0m")
            time.sleep(1)
            menu_admin()
    print("\033[0;31m Buku dengan ID tersebut tidak ditemukan. \033[0m")

# Fungsi untuk menghapus buku dari daftar
def hapus_buku():
    print("Hapus Buku")
    id_buku = int(input("\033[92m Masukkan ID buku yang ingin dihapus: \033[0m"))
    # Mencari buku berdasarkan ID
    for buku in Daftar_Buku:
        if buku.id == id_buku:
            # Menghapus buku dari daftar
            Daftar_Buku.remove(buku)
            time.sleep(1)
            print("\033[92m Buku berhasil dihapus! \033[0m")
            menu_admin()
    print("\033[0;31m Buku dengan ID tersebut tidak ditemukan. \033[0m")

# Menampilkan semua buku
def lihat_daftar_buku():
    print("Daftar Buku:")
    for buku in Daftar_Buku:
        buku.display_info()
        print()
    
    while True:
        jawaban = (input("Apakah anda ingin kembali(y/n) :"))
        if jawaban == "y" :
            menu_admin()
        else:
            print("Terima kasih, sampai jumpa lagi.")
            raise SystemExit

def daftar_buku():
    print("Daftar Buku:")
    for buku in Daftar_Buku:
        buku.display_info()
        print()
    
    while True:
        jawaban = (input("Apakah anda ingin kembali(y/n) :"))
        if jawaban == "y" :
            menu_pengguna()
        else:
            print("Terima kasih, sampai jumpa lagi.")
            raise SystemExit

def menu_pengguna():
    print("\n\033[1;36m╭──────────────────────────────────────────────────────────────────────╮\033[0m")
    print("\033[1;36m│\033[0;94m                        📚=== Menu Pengguna ===📚                     \033[1;36m│\033[0m")
    print("\033[1;36m├──────────────────────────────────────────────────────────────────────┤\033[0m")
    print("\033[92m│ 1. 📚 Tampilkan Semua Buku                                           │\033[0m")
    print("\033[92m│ 2. 📖 Rekomendasi Buku                                               │\033[0m")
    print("\033[92m│ 3. 🏠 Kembali ke Menu Utama                                          │\033[0m")
    print("\033[1;36m╰──────────────────────────────────────────────────────────────────────╯\033[0m")

    pilihan = input("\033[3;93m Masukkan pilihan Anda: \033[0m")



    if pilihan == "1":
        daftar_buku()
    elif pilihan == "2":
        rekomendasi_buku()
    elif pilihan == "3":
        print("\033[92mKembali ke Menu Utama...\033[0m")
        time.sleep(2)
        pass
    else:
        print("\033[0;31mPilihan tidak valid❌.\033[0m")
def rekomendasi_buku():
    print("\033[1mRekomendasi Buku:\033[0m")
    print("\033[92m╔════════════════════════════╗\033[0m")
    print("\033[92m║ \033[0;36m1. 📚 Buku Terlaris        \033[92m║\033[0m")
    print("\033[92m║ \033[0;36m2. 📖 Berdasarkan Genre    \033[92m║\033[0m")
    print("\033[92m║ \033[0;36m3. ⭐ Berdasarkan Rating   \033[92m║\033[0m")
    print("\033[92m╚════════════════════════════╝\033[0m")
    pilihan = input("\033[3;96mMasukkan pilihan Anda: \033[0m")

    if pilihan == "1":
        buku_terlaris = sorted(Daftar_Buku, key=lambda x: x.terjual, reverse=True)
        print("Buku Terlaris:")
        for buku in buku_terlaris[:3]:
            buku.display_info()
            print()
        menu_pengguna()
    elif pilihan == "2":
        genre = input("Masukkan genre buku: ")
        buku_genre = [buku for buku in Daftar_Buku if buku.genre.lower() == genre.lower()]
        if buku_genre:
            print(f"Buku dengan genre {genre}:")
            for buku in buku_genre:
                buku.display_info()
                print()
                
            menu_pengguna()
        else:
            print(f"\033[0;31m Tidak ada buku dengan genre {genre}.\033[0m ")
            menu_pengguna()
    elif pilihan == "3":
        rating_threshold = float(input("Masukkan threshold rating: "))
        buku_rating = [buku for buku in Daftar_Buku if buku.rating >= rating_threshold]
        if buku_rating:
            print(f"Buku dengan rating di atas {rating_threshold}:")
            for buku in buku_rating:
                buku.display_info()
                print()
            menu_pengguna()
        else:
            print(f"\033[0;31m Tidak ada buku dengan rating di atas {rating_threshold}.\033[0m")
            menu_pengguna()
    else:
        print("\033[0;31mPilihan tidak valid❌.\033[0m")
        menu_pengguna()

# Implementasi menu utama
def main():
    while True:
        print("╔════════════════════════════════════════════╗")
        print("║           \033[0;34mSelamat Datang di Aplikasi\033[0m       ║")
        print("║               \033[3;34m     BookyFinds     \033[0m         ║")
        print("╠════════════════════════════════════════════╣")
        print("║               \033[0;36m 1. Menu Admin\033[0m               ║")
        print("║               \033[0;36m 2. Menu Pengguna\033[0m            ║")
        print("║               \033[0;36m 3. Keluar\033[0m                   ║")
        print("╚════════════════════════════════════════════╝")
        pilihan = input("\033[0;37mMasukkan pilihan Anda:\033[0m ")

        if pilihan == "1":
            menu_admin()
        elif pilihan == "2":
            menu_pengguna()
        elif pilihan == "3":
            print("╔════════════════════════════════════════════╗")
            print("      \033[3;33mTerima kasih! Sampai jumpa lagi.\033[0m")
            print("╚════════════════════════════════════════════╝")
            break
        else:
            print("\033[0;31mPilihan tidak valid❌.\033[0m")

if __name__ == "__main__":
    main()

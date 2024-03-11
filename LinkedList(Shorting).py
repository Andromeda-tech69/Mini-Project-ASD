import random, os, time
os.system("cls")

# Membuat kelas untuk node buku
class ListNode:
    def __init__(self, buku):
        self.buku = buku
        self.next = None

# Membuat kelas untuk linked list buku
class LinkedList:
    def __init__(self):
        self.head = None

    def merge_sort(self, key=lambda x: x.lower(), reverse=False):
        if not self.head or not self.head.next:
            return self

        def merge(left, right):
            result = LinkedList()
            while left and right:
                if (key(left.buku) < key(right.buku)) != reverse:
                    result.tambah_di_akhir(left.buku)
                    left = left.next
                else:
                    result.tambah_di_akhir(right.buku)
                    right = right.next
            while left:
                result.tambah_di_akhir(left.buku)
                left = left.next
            while right:
                result.tambah_di_akhir(right.buku)
                right = right.next
            return result.head

        def split(head):
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            middle = slow.next
            slow.next = None
            return head, middle

        def sort(head):
            if not head or not head.next:
                return head
            left, right = split(head)
            left_sorted = sort(left)
            right_sorted = sort(right)
            return merge(left_sorted, right_sorted)

        self.head = sort(self.head)

    def print_list(self):
        current = self.head
        while current:
            print(current.buku, end=" ")
            current = current.next
        print()



    # Method untuk menambahkan buku di awal linked list
    def tambah_di_awal(self, buku):
        new_node = ListNode(buku)
        new_node.next = self.head
        self.head = new_node

    # Method untuk menambahkan buku di akhir linked list
    def tambah_di_akhir(self, buku):
        new_node = ListNode(buku)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    # Method untuk menambahkan buku di tengah linked list  
    def tambah_di_tengah(self, buku, posisi):
        if posisi <= 0:
            print("Posisi harus lebih besar dari 0.")
            return
        new_node = ListNode(buku)
        if not self.head:
            self.head = new_node
            return
        if posisi == 1:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        count = 1
        while current and count < posisi:
            if count == posisi - 1:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
            count += 1
        print("Posisi melebihi panjang linked list.")

    
    # Method untuk menghapus buku di awal linked list
    def hapus_di_awal(self):
        if not self.head:
            print("Linked list kosong. Tidak ada yang bisa dihapus.")
            return
        self.head = self.head.next

    # Method untuk menghapus buku di akhir linked list
    def hapus_di_akhir(self):
        if not self.head:
            print("Linked list kosong. Tidak ada yang bisa dihapus.")
            return
        if not self.head.next:
            self.head = None
            return
        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next
        current_node.next = None

    # Method untuk menghapus buku di tengah linked list
    def hapus_di_tengah(self, posisi):
        if posisi <= 0:
            print("Posisi tidak valid.")
            return
        if posisi == 1:
            self.hapus_di_awal()
            return
        current_node = self.head
        for _ in range(posisi - 2):
            if current_node is None:
                print("Posisi tidak valid.")
                return
            current_node = current_node.next
        if not current_node or not current_node.next:
            print("Posisi tidak valid.")
            return
        current_node.next = current_node.next.next
        new_node.next = current_node.next
        current_node.next = new_node

    # Method untuk menampilkan semua buku dalam linked list
    def tampilkan_semua(self):
        current_node = self.head
        while current_node:
            current_node.buku.display_info()
            current_node = current_node.next
            print("/////////////////////////////")

# Membuat kelas Buku
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

# Membuat daftar buku menggunakan linked list
daftar_buku = LinkedList()

# Menambahkan buku ke linked list
daftar_buku.tambah_di_akhir(Buku(1, "The Shining", "Stephen King", 1977, "Horror", 4.5, random.randint(100, 1000)))
daftar_buku.tambah_di_akhir(Buku(2, "Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 1997, "Fantasy", 4.8, random.randint(100, 1000)))
daftar_buku.tambah_di_akhir(Buku(3, "Good Omens", "Terry Pratchett & Neil Gaiman", 1990, "Comedy", 4.3, random.randint(100, 1000)))
daftar_buku.tambah_di_akhir(Buku(4, "It", "Stephen King", 1986, "Horror", 4.7, random.randint(100, 1000)))
daftar_buku.tambah_di_akhir(Buku(5, "The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy", 4.6, random.randint(100, 1000)))
daftar_buku.tambah_di_akhir(Buku(6, "Bridget Jones's Diary", "Helen Fielding", 1996, "Comedy", 4.0, random.randint(100, 1000)))
daftar_buku.tambah_di_akhir(Buku(7, "Dracula", "Bram Stoker", 1897, "Horror", 4.4, random.randint(100, 1000)))
daftar_buku.tambah_di_akhir(Buku(8, "A Game of Thrones", "George R.R. Martin", 1996, "Fantasy", 4.9, random.randint(100, 1000)))
daftar_buku.tambah_di_akhir(Buku(9, "The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979, "Comedy", 4.2, random.randint(100, 1000)))
daftar_buku.tambah_di_akhir(Buku(10, "Frankenstein", "Mary Shelley", 1818, "Horror", 4.6, random.randint(100, 1000)))
daftar_buku.tambah_di_akhir(Buku(11, "Pet Sematary", "Stephen King", 1983, "Horror", 4.2, random.randint(100, 1000)))
daftar_buku.tambah_di_akhir(Buku(12, "The Exorcist", "William Peter Blatty", 1971, "Horror", 4.6, random.randint(100, 1000)))
daftar_buku.tambah_di_akhir(Buku(13, "Carrie", "Stephen King", 1974, "Horror", 4.1, random.randint(100, 1000)))
daftar_buku.tambah_di_akhir(Buku(14, "The Importance of Being Earnest", "Oscar Wilde", 1895, "Comedy", 4.5, random.randint(100, 1000)))
daftar_buku.tambah_di_akhir(Buku(15, "Catch-22", "Joseph Heller", 1961, "Comedy", 4.3, random.randint(100, 1000)))
daftar_buku.tambah_di_akhir(Buku(16, "Three Men in a Boat", "Jerome K. Jerome", 1889, "Comedy", 4.0, random.randint(100, 1000)))
daftar_buku.tambah_di_akhir(Buku(17, "The Name of the Wind", "Patrick Rothfuss", 2007, "Fantasy", 4.8, random.randint(100, 1000)))
daftar_buku.tambah_di_akhir(Buku(18, "The Lies of Locke Lamora", "Scott Lynch", 2006, "Fantasy", 4.4, random.randint(100, 1000)))
daftar_buku.tambah_di_akhir(Buku(19, "Mistborn: The Final Empire", "Brandon Sanderson", 2006, "Fantasy", 4.7, random.randint(100, 1000)))

def tambah_buku(daftar_buku):
    print("\n\033[1;36mTambah Buku\033[0m")
    print("\033[92m1. Tambah di Awal")
    print("2. Tambah di Akhir")
    print("3. Tambah di Tengah\033[0m")

    pilihan = input("\033[3;32mPilih lokasi penambahan buku: \033[0m")

    if pilihan == "1":
        # Meminta input informasi buku baru
        id = int(input("Masukkan ID buku: "))
        judul = input("Masukkan judul buku: ")
        penulis = input("Masukkan nama penulis: ")
        tahun = int(input("Masukkan tahun terbit: "))
        genre = input("Masukkan genre buku: ")
        rating = float(input("Masukkan rating buku: "))
        terjual = int(input("Masukkan jumlah buku terjual: "))

        # Membuat objek Buku baru
        buku_baru = Buku(id, judul, penulis, tahun, genre, rating, terjual)

        # Menambahkan buku baru di awal linked list
        daftar_buku.tambah_di_awal(buku_baru)
        print("Buku berhasil ditambahkan di awal.")

    elif pilihan == "2":
        # Meminta input informasi buku baru
        id = int(input("Masukkan ID buku: "))
        judul = input("Masukkan judul buku: ")
        penulis = input("Masukkan nama penulis: ")
        tahun = int(input("Masukkan tahun terbit: "))
        genre = input("Masukkan genre buku: ")
        rating = float(input("Masukkan rating buku: "))
        terjual = int(input("Masukkan jumlah buku terjual: "))

        # Membuat objek Buku baru
        buku_baru = Buku(id, judul, penulis, tahun, genre, rating, terjual)

        # Menambahkan buku baru di akhir linked list
        daftar_buku.tambah_di_akhir(buku_baru)
        print("Buku berhasil ditambahkan di akhir.")

    elif pilihan == "3":
        # Meminta input informasi buku baru
        id = int(input("Masukkan ID buku: "))
        judul = input("Masukkan judul buku: ")
        penulis = input("Masukkan nama penulis: ")
        tahun = int(input("Masukkan tahun terbit: "))
        genre = input("Masukkan genre buku: ")
        rating = float(input("Masukkan rating buku: "))
        terjual = int(input("Masukkan jumlah buku terjual: "))

        # Membuat objek Buku baru
        buku_baru = Buku(id, judul, penulis, tahun, genre, rating, terjual)

        # Meminta input posisi untuk menambahkan buku
        posisi = int(input("Masukkan posisi penambahan buku: "))

        # Mencari node pada posisi yang diminta
        current_node = daftar_buku.head
        for _ in range(posisi - 2):
            if current_node is None:
                print("Posisi tidak valid.")
                return
            current_node = current_node.next

        # Menambahkan buku baru di antara dua node
        daftar_buku.tambah_di_tengah(buku_baru, posisi)
        print("Buku berhasil ditambahkan di tengah.")

    else:
        print("Pilihan tidak valid.")

def edit_buku(daftar_buku):
    # Meminta input ID buku yang akan diedit
    id_buku = int(input("Masukkan ID buku yang akan diedit: "))

    # Mencari buku dengan ID yang sesuai
    current_node = daftar_buku.head
    while current_node:
        if current_node.buku.id == id_buku:
            # Meminta input informasi baru untuk buku
            judul = input("Masukkan judul buku baru: ")
            penulis = input("Masukkan nama penulis baru: ")
            tahun = int(input("Masukkan tahun terbit baru: "))
            genre = input("Masukkan genre buku baru: ")
            rating = float(input("Masukkan rating buku baru:"))
            terjual = int(input("Masukkan jumlah buku terjual baru: "))

            # Mengupdate informasi buku
            current_node.buku.judul = judul
            current_node.buku.penulis = penulis
            current_node.buku.tahun = tahun
            current_node.buku.genre = genre
            current_node.buku.rating = rating
            current_node.buku.terjual = terjual

            print("Buku berhasil diubah.")
            return
        current_node = current_node.next
    print("Buku dengan ID tersebut tidak ditemukan.")

def hapus_buku(daftar_buku):
    print("\n\033[1;36mHapus Buku\033[0m")
    print("\033[92m1. Hapus di Awal")
    print("2. Hapus di Akhir")
    print("3. Hapus di Tengah\033[0m")

    pilihan = input("\033[3;32mPilih lokasi penghapusan buku: \033[0m")

    if pilihan == "1":
        # Hapus buku di awal linked list
        daftar_buku.hapus_di_awal()
        print("Buku berhasil dihapus di awal.")

    elif pilihan == "2":
        # Hapus buku di akhir linked list
        daftar_buku.hapus_di_akhir()
        print("Buku berhasil dihapus di akhir.")

    elif pilihan == "3":
        # Meminta input ID buku yang akan dihapus
        id_buku = int(input("Masukkan ID buku yang akan dihapus: "))

        # Mencari buku dengan ID yang sesuai
        current_node = daftar_buku.head
        prev_node = None
        while current_node:
            if current_node.buku.id == id_buku:
                if prev_node:
                    # Hapus buku di tengah atau akhir linked list
                    prev_node.next = current_node.next
                else:
                    # Hapus buku di awal linked list
                    daftar_buku.head = current_node.next
                print("Buku berhasil dihapus di tengah.")
                return
            prev_node = current_node
            current_node = current_node.next
        print("Buku dengan ID tersebut tidak ditemukan.")

    else:
        print("Pilihan tidak valid.")

def lihat_daftar_buku(daftar_buku):
    print("\nDaftar Buku:")
    daftar_buku.tampilkan_semua()

def submenu_lihat_daftar_buku(daftar_buku):
    while True:
        print("\n\033[1;36m╭──────────────────────────────────────────────────────────────────────╮\033[0m")
        print("\033[1;36m│\033[0;94m                         Lihat Daftar Buku                            \033[1;36m│\033[0m")
        print("\033[1;36m├──────────────────────────────────────────────────────────────────────┤\033[0m")
        print("\033[92m│ 1. 📝 Urutkan berdasarkan Judul (A-Z)                                │\033[0m")
        print("\033[92m│ 2. 📝 Urutkan berdasarkan Judul (Z-A)                                │\033[0m")
        print("\033[92m│ 3. 🆔 Urutkan berdasarkan ID (1-19)                                  │\033[0m")
        print("\033[92m│ 4. 🆔 Urutkan berdasarkan ID (19-1)                                  │\033[0m")
        print("\033[92m│ 5. 🏠 Kembali ke Menu Admin                                          │\033[0m")
        print("\033[1;36m╰──────────────────────────────────────────────────────────────────────╯\033[0m")

        pilihan_sub = input("\033[3;32mMasukkan pilihan Anda: \033[0m")

        if pilihan_sub == '1':
            daftar_buku.merge_sort(key=lambda x: x.judul.lower())
            daftar_buku.tampilkan_semua()
        elif pilihan_sub == '2':
            daftar_buku.merge_sort(key=lambda x: x.judul.lower(), reverse=True)
            daftar_buku.tampilkan_semua()
        elif pilihan_sub == '3':
            daftar_buku.merge_sort(key=lambda x: x.id)
            daftar_buku.tampilkan_semua()
        elif pilihan_sub == '4':
            daftar_buku.merge_sort(key=lambda x: x.id, reverse=True)
            daftar_buku.tampilkan_semua()
        elif pilihan_sub == '5':
            break

# Fungsi utama menu admin
def menu_admin(daftar_buku):
    while True:
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
            tambah_buku(daftar_buku)
        elif pilihan == "2":
            edit_buku(daftar_buku)
        elif pilihan == "3":
            hapus_buku(daftar_buku)
        elif pilihan == "4":
            submenu_lihat_daftar_buku(daftar_buku)
        elif pilihan == "5":
            print("Kembali ke Menu Utama.")
            break
        else:
            print("Pilihan tidak valid.")

def tampilkan_buku_berdasarkan_genre(daftar_buku):
    print("\n\033[1;36mTampilkan Buku Berdasarkan Genre\033[0m")
    genre_dicari = input("Masukkan genre buku yang ingin ditampilkan: ")

    # Inisialisasi variabel untuk menghitung halaman
    halaman = 1
    buku_per_halaman = 3
    current_node = daftar_buku.head

    # Mengumpulkan buku dengan genre yang sesuai
    buku_genre = []
    while current_node:
        if current_node.buku.genre.lower() == genre_dicari.lower():
            buku_genre.append(current_node.buku)
        current_node = current_node.next

    # Menampilkan buku berdasarkan genre dengan sistem halaman
    if buku_genre:
        buku_ditampilkan = 0
        total_buku = len(buku_genre)

        while buku_ditampilkan < total_buku:
            print(f"\n\033[1;33mHalaman {halaman}\033[0m")
            for i in range(buku_per_halaman):
                if buku_ditampilkan < total_buku:
                    buku_genre[buku_ditampilkan].display_info()
                    buku_ditampilkan += 1
            print("\n")

            if buku_ditampilkan < total_buku:
                lanjut = input("Lanjut ke halaman selanjutnya (tekan Enter) atau ketik '1' untuk kembali ke halaman sebelumnya: ")
                if lanjut == "1":
                    if halaman > 2:
                        halaman -= 2
                        buku_ditampilkan -= buku_per_halaman * 2
                    else:
                        print("Anda sudah berada di halaman pertama.")
                else:
                    halaman += 1
            else:
                print("Anda telah mencapai halaman terakhir.")
                break
    else:
        print("Tidak ada buku dengan genre tersebut.")


def rekomendasi_buku(daftar_buku):
    print("\n\033[1;36mRekomendasi Buku\033[0m")
    print("\033[92m1. Berdasarkan Rating")
    print("2. Berdasarkan Jumlah Terjual\033[0m")

    pilihan = input("\033[3;93m Pilih kriteria rekomendasi: \033[0m")

    # Menginisialisasi list untuk menyimpan semua buku
    semua_buku = []

    # Menambahkan semua buku ke dalam list
    current_node = daftar_buku.head
    while current_node:
        semua_buku.append(current_node.buku)
        current_node = current_node.next

    if pilihan == "1":
        # Mengurutkan buku berdasarkan rating
        rekomendasi = sorted(semua_buku, key=lambda x: x.rating, reverse=True)
        kriteria = "Rating"
    elif pilihan == "2":
        # Mengurutkan buku berdasarkan jumlah terjual
        rekomendasi = sorted(semua_buku, key=lambda x: x.terjual, reverse=True)
        kriteria = "Jumlah Terjual"
    else:
        print("Pilihan tidak valid.")
        return

    # Menampilkan rekomendasi buku
    print(f"\nTop 3 Rekomendasi Buku Berdasarkan {kriteria}:")
    for i in range(min(3, len(rekomendasi))):
        rekomendasi[i].display_info()

def menu_pengguna(daftar_buku):
    while True:
        print("\n\033[1;36m╭──────────────────────────────────────────────────────────────────────╮\033[0m")
        print("\033[1;36m│\033[0;94m                        📚=== Menu Pengguna ===📚                     \033[1;36m│\033[0m")
        print("\033[1;36m├──────────────────────────────────────────────────────────────────────┤\033[0m")
        print("\033[92m│ 1. 📚 Tampilkan Buku Berdasarkan Genre                               │\033[0m")
        print("\033[92m│ 2. 📖 Rekomendasi Buku Berdasarkan Rating dan Terjual                │\033[0m")
        print("\033[92m│ 3. 🏠 Kembali ke Menu Utama                                          │\033[0m")
        print("\033[1;36m╰──────────────────────────────────────────────────────────────────────╯\033[0m")

        pilihan = input("\033[3;93m Masukkan pilihan Anda: \033[0m")

        if pilihan == "1":
            tampilkan_buku_berdasarkan_genre(daftar_buku)
        elif pilihan == "2":
            rekomendasi_buku(daftar_buku)
        elif pilihan == "3":
            print("Kembali ke Menu Utama.")
            break
        else:
            print("Pilihan tidak valid.")

# Fungsi utama untuk menjalankan program
def main():
    while True:
        print("\n\033[1;36m╭──────────────────────────────────────────────────────────────────────╮\033[0m")
        print("\033[1;36m│\033[0;94m                             Menu Utama                               \033[1;36m│\033[0m")
        print("\033[1;36m├──────────────────────────────────────────────────────────────────────┤\033[0m")
        print("\033[92m│ 1. Menu Admin                                                        │\033[0m")
        print("\033[92m│ 2. Menu Pengguna                                                     │\033[0m")
        print("\033[92m│ 3. Keluar                                                            │\033[0m")
        print("\033[1;36m╰──────────────────────────────────────────────────────────────────────╯\033[0m")

        pilihan = input("\033[3;93m Pilih menu: \033[0m")
        if pilihan == "1":
            menu_admin(daftar_buku)
        elif pilihan == "2":
            menu_pengguna(daftar_buku)
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid.")

# Memanggil fungsi main
if __name__ == "__main__":
    main()



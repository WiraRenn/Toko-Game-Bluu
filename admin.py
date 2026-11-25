# ==========================================
# MODUL FITUR ADMIN
# ==========================================

from data import games, users, koleksi, wishlist
import data
from validasi import input_teks, input_angka, konfirmasi, clear_terminal


def tampilkan_game():
    """Prosedur untuk menampilkan seluruh katalog game."""
    print("\n========== DAFTAR GAME ==========")

    if len(games) == 0:
        print("Tidak ada game dalam katalog.")
    else:
        for game in games:
            print("--------------------------------")
            print("ID     :", game["id"])
            print("Nama   :", game["nama"])
            print("Genre  :", game["genre"])
            print("Stok   :", game["stok"])


def cari_game(id_game):
    """Fungsi dengan parameter untuk mencari game berdasarkan ID."""
    for game in games:
        if game["id"] == id_game:
            return game
    return None


def tambah_game():
    """Menambahkan game baru ke katalog."""
    clear_terminal()
    print("\n========== TAMBAH GAME ==========")

    try:
        nama = input_teks("Nama game: ")
        genre = input_teks("Genre game: ")
        stok = input_angka("Stok game: ", 0)

        game_baru = {
            "id": data.id_berikutnya,
            "nama": nama,
            "genre": genre,
            "stok": stok
        }

        games.append(game_baru)
        data.id_berikutnya += 1

        print("Game berhasil ditambahkan.")

    except ValueError as error:
        print("Data tidak valid:", error)


def edit_game():
    """Mengubah nama, genre, atau stok game."""
    clear_terminal()
    print("\n========== EDIT GAME ==========")
    tampilkan_game()

    if len(games) == 0:
        return

    try:
        id_game = input_angka("Masukkan ID game: ", 1)
        game = cari_game(id_game)

        if game is None:
            raise ValueError("ID game tidak ditemukan.")

        print("\nData game:")
        print("1. Nama")
        print("2. Genre")
        print("3. Stok")

        pilihan = input_angka("Pilih data yang diubah: ", 1)

        if pilihan == 1:
            game["nama"] = input_teks("Nama baru: ")
        elif pilihan == 2:
            game["genre"] = input_teks("Genre baru: ")
        elif pilihan == 3:
            game["stok"] = input_angka("Stok baru: ", 0)
        else:
            raise ValueError("Pilihan perubahan tidak tersedia.")

        print("Data game berhasil diperbarui.")

    except ValueError as error:
        print("Kesalahan:", error)


def hapus_game():
    """Menghapus game dari katalog setelah mendapat konfirmasi."""
    clear_terminal()
    print("\n========== HAPUS GAME ==========")
    tampilkan_game()

    if len(games) == 0:
        return

    try:
        id_game = input_angka("Masukkan ID game yang dihapus: ", 1)
        game = cari_game(id_game)

        if game is None:
            raise ValueError("ID game tidak ditemukan.")

        print("\nNama game :", game["nama"])
        print("Genre     :", game["genre"])
        print("Stok      :", game["stok"])

        if konfirmasi("Yakin ingin menghapus game ini?"):
            # Simpan data game terlebih dahulu agar koleksi user tetap dapat
            # menampilkan game yang sudah pernah dibeli.
            data.game_terhapus[id_game] = game.copy()

            # Hapus game hanya dari katalog, bukan dari koleksi user.
            games.remove(game)

            # Game yang dihapus dari katalog tidak lagi ditampilkan di Wishlist.
            for username in wishlist:
                wishlist[username].discard(id_game)

            print("Game berhasil dihapus dari katalog.")
            print("Jika game sudah dibeli user, game tetap ada di koleksi user.")
        else:
            print("Penghapusan dibatalkan.")

    except ValueError as error:
        print("Kesalahan:", error)


def menu_admin():
    """Prosedur menu Admin."""
    clear_terminal()
    while True:
        print("\n========== MENU ADMIN ==========")
        print("1. Tambah Game")
        print("2. Lihat Daftar Game")
        print("3. Edit Game")
        print("4. Hapus Game")
        print("5. Logout")

        pilihan = input_angka("Pilih menu: ")

        if pilihan == 1:
            tambah_game()
        elif pilihan == 2:
            tampilkan_game()
        elif pilihan == 3:
            edit_game()
        elif pilihan == 4:
            hapus_game()
        elif pilihan == 5:
            print("Admin berhasil logout.")
            break
        else:
            print("Pilihan tidak valid.")
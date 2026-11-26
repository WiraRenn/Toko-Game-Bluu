# ==========================================
# MODUL FITUR ADMIN
# ==========================================

from data import games, users, koleksi, wishlist
import data
from validasi import input_teks, input_angka, konfirmasi, clear_terminal, pilih_opsi, HIJAU, MERAH, KUNING, CYAN, TEBAL
from prettytable import PrettyTable


def tampilkan_game():
    """Prosedur untuk menampilkan seluruh katalog game dalam tabel."""
    clear_terminal()
    print(CYAN + TEBAL + "\\n========== DAFTAR GAME ==========")

    if len(games) == 0:
        print(KUNING + "Tidak ada game dalam katalog.")
    else:
        tabel = PrettyTable()
        tabel.field_names = ["ID", "Nama Game", "Genre", "Stok"]
        tabel.align["Nama Game"] = "l"
        tabel.align["Genre"] = "l"

        for game in games:
            tabel.add_row([
                game["id"],
                game["nama"],
                game["genre"],
                game["stok"]
            ])

        print(HIJAU + str(tabel))


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
        stok = input_angka("Stok game (maksimal 300): ", 0, 300)

        game_baru = {
            "id": data.id_berikutnya,
            "nama": nama,
            "genre": genre,
            "stok": stok
        }

        games.append(game_baru)
        data.id_berikutnya += 1

        print(HIJAU + "Game berhasil ditambahkan.")

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
        id_game = pilih_opsi("Pilih game yang ingin diedit:", [
            {"name": f'{game["id"]} - {game["nama"]}', "value": game["id"]}
            for game in games
        ])
        game = cari_game(id_game)

        if game is None:
            raise ValueError("ID game tidak ditemukan.")

        pilihan = pilih_opsi("Pilih data yang ingin diubah:", ["Nama", "Genre", "Stok"])

        if pilihan == "Nama":
            game["nama"] = input_teks("Nama baru: ")
        elif pilihan == "Genre":
            game["genre"] = input_teks("Genre baru: ")
        elif pilihan == "Stok":
            game["stok"] = input_angka("Stok baru: ", 0)

        print(HIJAU + "Data game berhasil diperbarui.")

    except ValueError as error:
        print(MERAH + "Kesalahan:", error)


def hapus_game():
    """Menghapus game dari katalog setelah mendapat konfirmasi."""
    clear_terminal()
    print("\n========== HAPUS GAME ==========")
    tampilkan_game()

    if len(games) == 0:
        return

    try:
        id_game = pilih_opsi("Pilih game yang ingin dihapus:", [
            {"name": f'{game["id"]} - {game["nama"]}', "value": game["id"]}
            for game in games
        ])
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

            print(HIJAU + "Game berhasil dihapus dari katalog.")
            print(CYAN + "Jika game sudah dibeli user, game tetap ada di koleksi user.")
        else:
            print("Penghapusan dibatalkan.")

    except ValueError as error:
        print(MERAH + "Kesalahan:", error)


def menu_admin():
    """Prosedur menu Admin."""
    clear_terminal()
    while True:
        print(CYAN + TEBAL + "\n========== MENU ADMIN ==========")
        pilihan = pilih_opsi("Pilih menu Admin:", [
            "Tambah Game", "Lihat Daftar Game", "Edit Game", "Hapus Game", "Logout"
        ])

        if pilihan == "Tambah Game":
            tambah_game()
        elif pilihan == "Lihat Daftar Game":
            tampilkan_game()
        elif pilihan == "Edit Game":
            edit_game()
        elif pilihan == "Hapus Game":
            hapus_game()
        elif pilihan == "Logout":
            print("Admin berhasil logout.")
            break
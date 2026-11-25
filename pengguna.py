# ==========================================
# MODUL FITUR USER
# ==========================================

from data import games, users, koleksi, wishlist, game_terhapus
from admin import cari_game
from validasi import input_teks, input_angka, konfirmasi, clear_terminal


def lihat_katalog():
    """Menampilkan katalog dan detail game yang dipilih."""
    clear_terminal()
    print("\n========== KATALOG GAME ==========")

    if len(games) == 0:
        print("Belum ada game tersedia.")
        return

    for game in games:
        print("--------------------------------")
        print("ID     :", game["id"])
        print("Nama   :", game["nama"])
        print("Genre  :", game["genre"])
        print("Stok   :", game["stok"])

    try:
        id_game = input_angka("\nMasukkan ID game untuk melihat detail (0 untuk kembali): ", 0)

        if id_game == 0:
            return

        game = cari_game(id_game)

        if game is None:
            raise ValueError("Game tidak ditemukan.")

        print("\n========== DETAIL GAME ==========")
        print("Nama  :", game["nama"])
        print("Genre :", game["genre"])
        print("Stok  :", game["stok"])

    except ValueError as error:
        print("Kesalahan:", error)


def lihat_koleksi(username):
    """Menampilkan seluruh game yang dimiliki user."""
    clear_terminal()
    print("\n========== KOLEKSI GAME ==========")

    if len(koleksi[username]) == 0:
        print("Koleksi masih kosong.")
    else:
        for id_game in koleksi[username]:
            # Cari game di katalog terlebih dahulu.
            game = cari_game(id_game)

            # Jika tidak ada di katalog, cari di data game yang dihapus.
            if game is None:
                game = game_terhapus.get(id_game)

            if game is not None:
                print("ID:", game["id"], "|", game["nama"], "|", game["genre"])


def beli_game(username):
    """Memproses pembelian game dan mengurangi stok katalog."""
    clear_terminal()
    print("\n========== PEMBELIAN GAME ==========")

    if len(games) == 0:
        print("Belum ada game yang tersedia.")
        return

    for game in games:
        print("--------------------------------")
        print("ID:", game["id"])
        print("Nama:", game["nama"])
        print("Genre:", game["genre"])
        print("Stok:", game["stok"])

    try:
        id_game = input_angka("\nMasukkan ID game yang ingin dibeli: ", 1)
        game = cari_game(id_game)

        if game is None:
            raise ValueError("Game tidak ditemukan.")

        if game["stok"] <= 0:
            raise ValueError("Stok game habis.")

        if id_game in koleksi[username]:
            raise ValueError("Game sudah dimiliki dan ada di koleksi.")

        print("\nGame:", game["nama"])
        print("Stok tersedia:", game["stok"])

        if konfirmasi("Konfirmasi pembelian?"):
            game["stok"] -= 1
            koleksi[username].append(id_game)

            print("Pembelian berhasil.")
            print("Stok game sekarang:", game["stok"])
        else:
            print("Pembelian dibatalkan.")

    except ValueError as error:
        print("Kesalahan:", error)


def edit_profil(username):
    """Mengubah nama, username, atau password akun User."""
    clear_terminal()
    print("\n========== EDIT PROFIL ==========")

    akun = users[username]
    print("Nama     :", akun["nama"])
    print("Username :", akun["username"])
    print("Password : (disembunyikan)")

    print("\nPilih data yang ingin diubah:")
    print("1. Nama")
    print("2. Username")
    print("3. Password")

    try:
        pilihan = input_angka("Pilihan: ", 1)

        if pilihan == 1:
            akun["nama"] = input_teks("Nama baru: ")

        elif pilihan == 2:
            username_baru = input_teks("Username baru: ")

            if username_baru in users:
                raise ValueError("Username sudah digunakan.")

            # Memindahkan data akun ke key username yang baru.
            users[username_baru] = akun
            users[username_baru]["username"] = username_baru
            del users[username]

            koleksi[username_baru] = koleksi[username]
            del koleksi[username]

            wishlist[username_baru] = wishlist[username]
            del wishlist[username]

            username = username_baru

        elif pilihan == 3:
            akun["password"] = input_teks("Password baru: ")

        else:
            raise ValueError("Pilihan tidak tersedia.")

        print("Profil berhasil diperbarui.")

    except ValueError as error:
        print("Kesalahan:", error)

    return username


def menu_user(username):
    """Prosedur menu utama User."""
    clear_terminal()
    while True:
        print("\n========== MENU USER ==========")
        print("1. Lihat Katalog Game")
        print("2. Beli Game")
        print("3. Lihat Koleksi Game")
        print("4. Edit Profil")
        print("5. Wishlist")
        print("6. Logout")

        pilihan = input_angka("Pilih menu: ")

        if pilihan == 1:
            lihat_katalog()
        elif pilihan == 2:
            beli_game(username)
        elif pilihan == 3:
            lihat_koleksi(username)
        elif pilihan == 4:
            username = edit_profil(username)
        elif pilihan == 5:
            menu_wishlist(username)
        elif pilihan == 6:
            print("User berhasil logout.")
            break
        else:
            print("Pilihan tidak valid.")


def menu_wishlist(username):
    """Prosedur menu Wishlist."""
    clear_terminal()
    while True:
        print("\n========== MENU WISHLIST ==========")
        print("1. Lihat Wishlist")
        print("2. Tambah Wishlist")
        print("3. Hapus Wishlist")
        print("4. Kembali")

        pilihan = input_angka("Pilih menu: ")

        if pilihan == 1:
            lihat_wishlist(username)
        elif pilihan == 2:
            tambah_wishlist(username)
        elif pilihan == 3:
            hapus_wishlist(username)
        elif pilihan == 4:
            break
        else:
            print("Pilihan tidak valid.")


def lihat_wishlist(username):
    """Menampilkan seluruh game yang ada di wishlist."""
    clear_terminal()
    print("\n========== DAFTAR WISHLIST ==========")

    if len(wishlist[username]) == 0:
        print("Wishlist masih kosong.")
    else:
        for id_game in wishlist[username]:
            game = cari_game(id_game)
            if game is not None:
                print("ID:", game["id"], "|", game["nama"], "|", game["genre"])


def tambah_wishlist(username):
    """Menambahkan game yang tersedia ke wishlist."""
    clear_terminal()
    print("\n========== TAMBAH WISHLIST ==========")

    if len(games) == 0:
        print("Belum ada game dalam katalog.")
        return

    for game in games:
        print("ID:", game["id"], "|", game["nama"])

    try:
        id_game = input_angka("Masukkan ID game: ", 1)
        game = cari_game(id_game)

        if game is None:
            raise ValueError("Game tidak ditemukan.")

        if id_game in wishlist[username]:
            raise ValueError("Game sudah terdaftar di Wishlist.")

        wishlist[username].add(id_game)
        print("Game berhasil ditambahkan ke Wishlist.")

    except ValueError as error:
        print("Kesalahan:", error)


def hapus_wishlist(username):
    """Menghapus game dari wishlist."""
    clear_terminal()
    print("\n========== HAPUS WISHLIST ==========")

    if len(wishlist[username]) == 0:
        print("Wishlist masih kosong.")
        return

    lihat_wishlist(username)

    try:
        id_game = input_angka("Masukkan ID game yang dihapus: ", 1)

        if id_game not in wishlist[username]:
            raise ValueError("ID game tidak ditemukan di Wishlist.")

        wishlist[username].remove(id_game)
        print("Game berhasil dihapus dari Wishlist.")

    except ValueError as error:
        print("Kesalahan:", error)
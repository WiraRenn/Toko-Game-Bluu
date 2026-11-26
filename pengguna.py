# ==========================================
# MODUL FITUR USER
# ==========================================

from data import games, users, koleksi, wishlist, game_terhapus
from admin import cari_game
from validasi import input_teks, input_angka, konfirmasi, clear_terminal, pilih_opsi, HIJAU, MERAH, KUNING, CYAN, TEBAL
from prettytable import PrettyTable


def lihat_katalog():
    """Menampilkan katalog dan detail game yang dipilih."""
    clear_terminal()
    print(CYAN + TEBAL + "\n========== KATALOG GAME ==========")

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
        pilihan_game = pilih_opsi("Pilih game untuk melihat detail:", [
            {"name": f'{game["id"]} - {game["nama"]}', "value": game["id"]}
            for game in games
        ] + [{"name": "Kembali", "value": 0}])

        if pilihan_game == 0:
            return

        game = cari_game(pilihan_game)

        if game is None:
            raise ValueError("Game tidak ditemukan.")

        print("\n========== DETAIL GAME ==========")
        print("Nama  :", game["nama"])
        print("Genre :", game["genre"])
        print("Stok  :", game["stok"])

    except ValueError as error:
        print(MERAH + "Kesalahan:", error)


def lihat_koleksi(username):
    """Menampilkan seluruh game yang dimiliki user."""
    clear_terminal()
    print(CYAN + TEBAL + "\n========== KOLEKSI GAME ==========")

    if len(koleksi[username]) == 0:
        print(KUNING + "Koleksi masih kosong.")
    else:
        tabel = PrettyTable()
        tabel.field_names = ["ID", "Nama Game", "Genre", "Status"]
        tabel.align["Nama Game"] = "l"
        tabel.align["Genre"] = "l"

        for id_game in koleksi[username]:
            # Cari game di katalog, lalu di arsip jika sudah dihapus admin.
            game = cari_game(id_game)
            status = "Tersedia di katalog"

            if game is None:
                game = game_terhapus.get(id_game)
                status = "Dihapus dari katalog"

            if game is not None:
                tabel.add_row([game["id"], game["nama"], game["genre"], status])

        print(HIJAU + str(tabel))


def beli_game(username):
    """Memproses pembelian game dan mengurangi stok katalog."""
    clear_terminal()
    print(CYAN + TEBAL + "\n========== PEMBELIAN GAME ==========")

    if len(games) == 0:
        print("Belum ada game yang tersedia.")
        return

    tabel = PrettyTable()
    tabel.field_names = ["ID", "Nama Game", "Genre", "Stok"]
    tabel.align["Nama Game"] = "l"
    tabel.align["Genre"] = "l"

    for game in games:
        tabel.add_row([game["id"], game["nama"], game["genre"], game["stok"]])

    print(HIJAU + str(tabel))

    try:
        id_game = pilih_opsi("Pilih game yang ingin dibeli:", [
            {"name": f'{game["id"]} - {game["nama"]} (Stok: {game["stok"]})', "value": game["id"]}
            for game in games
        ])
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

            print(HIJAU + "Pembelian berhasil.")
            print("Stok game sekarang:", game["stok"])
        else:
            print("Pembelian dibatalkan.")

    except ValueError as error:
        print(MERAH + "Kesalahan:", error)


def edit_profil(username):
    """Mengubah nama, username, atau password akun User."""
    clear_terminal()
    print("\n========== EDIT PROFIL ==========")

    akun = users[username]
    print("Nama     :", akun["nama"])
    print("Username :", akun["username"])
    print("Password : (disembunyikan)")

    try:
        pilihan = pilih_opsi("Pilih data yang ingin diubah:", ["Nama", "Username", "Password"])

        if pilihan == "Nama":
            akun["nama"] = input_teks("Nama baru: ")

        elif pilihan == "Username":
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

        elif pilihan == "Password":
            akun["password"] = input_teks("Password baru: ")

        print("Profil berhasil diperbarui.")

    except ValueError as error:
        print(MERAH + "Kesalahan:", error)

    return username


def menu_user(username):
    """Prosedur menu utama User."""
    clear_terminal()
    while True:
        print("\n========== MENU USER ==========")
        pilihan = pilih_opsi("Pilih menu User:", [
            "Lihat Katalog Game", "Beli Game", "Lihat Koleksi Game",
            "Edit Profil", "Wishlist", "Logout"
        ])

        if pilihan == "Lihat Katalog Game":
            lihat_katalog()
        elif pilihan == "Beli Game":
            beli_game(username)
        elif pilihan == "Lihat Koleksi Game":
            lihat_koleksi(username)
        elif pilihan == "Edit Profil":
            username = edit_profil(username)
        elif pilihan == "Wishlist":
            menu_wishlist(username)
        elif pilihan == "Logout":
            print("User berhasil logout.")
            break


def menu_wishlist(username):
    """Prosedur menu Wishlist."""
    clear_terminal()
    while True:
        print("\n========== MENU WISHLIST ==========")
        pilihan = pilih_opsi("Pilih menu Wishlist:", [
            "Lihat Wishlist", "Tambah Wishlist", "Hapus Wishlist", "Kembali"
        ])

        if pilihan == "Lihat Wishlist":
            lihat_wishlist(username)
        elif pilihan == "Tambah Wishlist":
            tambah_wishlist(username)
        elif pilihan == "Hapus Wishlist":
            hapus_wishlist(username)
        elif pilihan == "Kembali":
            break


def lihat_wishlist(username):
    """Menampilkan seluruh game yang ada di wishlist."""
    clear_terminal()
    print("\n========== DAFTAR WISHLIST ==========")

    if len(wishlist[username]) == 0:
        print(KUNING + "Wishlist masih kosong.")
    else:
        tabel = PrettyTable()
        tabel.field_names = ["ID", "Nama Game", "Genre"]
        tabel.align["Nama Game"] = "l"
        tabel.align["Genre"] = "l"

        for id_game in wishlist[username]:
            game = cari_game(id_game)
            if game is not None:
                tabel.add_row([game["id"], game["nama"], game["genre"]])

        print(HIJAU + str(tabel))


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
        id_game = pilih_opsi("Pilih game untuk ditambahkan ke Wishlist:", [
            {"name": f'{game["id"]} - {game["nama"]}', "value": game["id"]}
            for game in games
        ])
        game = cari_game(id_game)

        if game is None:
            raise ValueError("Game tidak ditemukan.")

        if id_game in wishlist[username]:
            raise ValueError("Game sudah terdaftar di Wishlist.")

        wishlist[username].add(id_game)
        print("Game berhasil ditambahkan ke Wishlist.")

    except ValueError as error:
        print(MERAH + "Kesalahan:", error)


def hapus_wishlist(username):
    """Menghapus game dari wishlist."""
    clear_terminal()
    print("\n========== HAPUS WISHLIST ==========")

    if len(wishlist[username]) == 0:
        print(KUNING + "Wishlist masih kosong.")
        return

    lihat_wishlist(username)

    try:
        pilihan_game = []
        for id_item in wishlist[username]:
            game = cari_game(id_item)
            if game is not None:
                pilihan_game.append({"name": f'{game["id"]} - {game["nama"]}', "value": id_item})
        id_game = pilih_opsi("Pilih game yang dihapus dari Wishlist:", pilihan_game)

        if id_game not in wishlist[username]:
            raise ValueError("ID game tidak ditemukan di Wishlist.")

        wishlist[username].remove(id_game)
        print("Game berhasil dihapus dari Wishlist.")

    except ValueError as error:
        print(MERAH + "Kesalahan:", error)
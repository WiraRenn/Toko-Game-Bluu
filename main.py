from autentikasi import login, register
from admin import menu_admin
from pengguna import menu_user
from data import games, users
from validasi import clear_terminal, pilih_opsi, tampilkan_header, CYAN, TEBAL

def menu_utama():
    # Prosedur untuk menampilkan menu awal program.
    clear_terminal()
    while True:
        tampilkan_header("SISTEM TOKO GAME", "Temukan dan kelola koleksi game favoritmu")
        print(CYAN + f"  Katalog: {len(games)} game tersedia   |   Akun terdaftar: {len(users)}")
        print()
        pilihan = pilih_opsi("Apa yang ingin kamu lakukan?", ["Login", "Register", "Keluar"])

        if pilihan == "Login":
            akun = login()

            if akun is not None:
                if akun["hak_akses"] == "Admin":
                    menu_admin()
                else:
                    menu_user(akun["username"])

        elif pilihan == "Register":
            register()

        elif pilihan == "Keluar":
            print("Terima kasih telah menggunakan Sistem Toko Game.")
            break

if __name__ == "__main__":
    try:
        menu_utama()
    except KeyboardInterrupt:
        print("\nProgram dihentikan oleh pengguna.")
        print("Terima kasih telah menggunakan Sistem Toko Game.")
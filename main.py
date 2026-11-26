# ==========================================
# PROGRAM UTAMA SISTEM TOKO GAME
# Jalankan file ini untuk memulai program.
# ==========================================

from autentikasi import login, register
from admin import menu_admin
from pengguna import menu_user
from validasi import clear_terminal, pilih_opsi


def menu_utama():
    """Prosedur untuk menampilkan menu awal program."""
    clear_terminal()
    while True:
        print("\n================================")
        print("       SISTEM TOKO GAME")
        print("================================")

        pilihan = pilih_opsi("Pilih menu:", ["Login", "Register", "Keluar"])

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
        print("\n\nProgram dihentikan oleh pengguna (Ctrl+C).")
        print("Terima kasih telah menggunakan Sistem Toko Game.")
from data import users, koleksi, wishlist
from validasi import input_teks, clear_terminal, tampilkan_header, CYAN, TEBAL

def register():
    # Mendaftarkan akun baru dengan hak akses User.
    clear_terminal()
    tampilkan_header("REGISTRASI AKUN", "Buat akun pengguna baru")

    while True:
        username = input_teks("Buat username: ")

        try:
            if username in users:
                raise ValueError("Username sudah digunakan.")

            password = input_teks("Buat password: ")
            nama = input_teks("Masukkan nama: ")

            users[username] = {
                "username": username,
                "password": password,
                "hak_akses": "User",
                "nama": nama
            }

            koleksi[username] = []
            wishlist[username] = set()

            print("Registrasi berhasil!")
            print("Silakan login menggunakan akun yang dibuat.")
            break

        except ValueError as error:
            print("Kesalahan:", error)

def login():
    # Memeriksa username dan password, maksimal 3 percobaan password.
    clear_terminal()
    tampilkan_header("LOGIN", "Masuk ke Sistem Toko Game")

    username = input_teks("Username: ")

    if username not in users:
        print("Username tidak ditemukan.")
        return None

    batas = 0

    while batas < 3:
        password = input_teks("Password: ")

        if users[username]["password"] == password:
            print("Login berhasil. Selamat datang,", users[username]["nama"])
            return users[username]

        batas += 1
        sisa = 3 - batas
        print("Password salah.")
        if sisa > 0:
            print("Sisa percobaan:", sisa)

    print("Kesempatan login habis. Silakan coba kembali.")
    return None
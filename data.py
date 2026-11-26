# ==========================================
# DATA PROGRAM SISTEM TOKO GAME
# ==========================================

# Data akun disimpan dalam dictionary.
# Akun Admin awal:
# Username : admin
# Password : admin123

users = {
    "admin": {
        "username": "admin",
        "password": "admin123",
        "hak_akses": "Admin",
        "nama": "Administrator"
    }
}

# Katalog game disimpan dalam list yang berisi dictionary.
# Data game hanya menggunakan ID, nama, genre, dan stok.
games = [
    {
        "id": 1,
        "nama": "Minecraft",
        "genre": "Sandbox",
        "stok": 10
    },
    {
        "id": 2,
        "nama": "Grand Theft Auto V",
        "genre": "Action Adventure",
        "stok": 8
    },
    {
        "id": 3,
        "nama": "Stardew Valley",
        "genre": "Simulation RPG",
        "stok": 15
    },
    {
        "id": 4,
        "nama": "Elden Ring",
        "genre": "Action RPG",
        "stok": 5
    },
    {
        "id": 5,
        "nama": "The Sims 4",
        "genre": "Simulation",
        "stok": 12
    }
]


# Data game yang dihapus dari katalog tetapi masih dimiliki user.
# Data ini digunakan agar game yang sudah dibeli tetap muncul di koleksi.
game_terhapus = {}

# Koleksi setiap user disimpan dalam dictionary.
# Isi koleksi berupa list ID game.
koleksi = {
    "admin": []
}

# Wishlist setiap user disimpan dalam dictionary.
# Isi wishlist berupa set ID game agar tidak ada data duplikat.
wishlist = {
    "admin": set()
}

# ID game berikutnya.
id_berikutnya = 6
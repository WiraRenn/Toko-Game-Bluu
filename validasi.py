import os
from colorama import init, Fore, Style
from InquirerPy import inquirer

init(autoreset=True)

HIJAU = Fore.GREEN
MERAH = Fore.RED
KUNING = Fore.YELLOW
CYAN = Fore.CYAN
BIRU = Fore.BLUE
TEBAL = Style.BRIGHT
RESET = Style.RESET_ALL

def clear_terminal():
    # Membersihkan terminal sesuai sistem operasi yang digunakan.
    os.system("cls" if os.name == "nt" else "clear")

def tampilkan_header(judul, keterangan=None):
    # Menampilkan header terminal dengan desain yang konsisten.
    lebar = 54
    print(CYAN + TEBAL + "╔" + "═" * lebar + "╗")
    print(CYAN + TEBAL + "║" + judul.center(lebar) + "║")
    if keterangan:
        print(CYAN + "║" + keterangan.center(lebar) + "║")
    print(CYAN + TEBAL + "╚" + "═" * lebar + "╝")

def input_teks(pesan):
    # Meminta input teks yang tidak boleh kosong.
    while True:
        try:
            nilai = input(pesan).strip()

            if nilai == "":
                raise ValueError("Input tidak boleh kosong.")

            return nilai

        except ValueError as error:
            print("Kesalahan:", error)

def input_angka(pesan, minimum=None, maksimum=None):
    # Meminta input angka bulat dan memeriksa batas minimum serta maksimum.
    while True:
        try:
            angka = int(input(pesan))

            if minimum is not None and angka < minimum:
                raise ValueError("Angka minimal adalah " + str(minimum) + ".")

            if maksimum is not None and angka > maksimum:
                raise ValueError("Angka maksimal adalah " + str(maksimum) + ".")

            return angka

        except ValueError as error:
            print("Input tidak valid:", error)
            if minimum is not None and maksimum is not None:
                print(f"Masukkan angka antara {minimum} sampai {maksimum}.")
            elif minimum is not None:
                print("Nilai minimal:", minimum)
            elif maksimum is not None:
                print("Nilai maksimal:", maksimum)

def konfirmasi(pesan):
    # Meminta konfirmasi Ya atau Tidak menggunakan try-except-finally.
    while True:
        try:
            jawaban = input(pesan + " (ya/tidak) : ").lower().strip()

            if jawaban == "ya":
                return True
            elif jawaban == "tidak":
                return False
            else:
                raise ValueError("Masukkan hanya ya atau tidak.")

        except ValueError as error:
            print("Kesalahan:", error)

        finally:
            print("Pemeriksaan konfirmasi selesai.")

def pilih_opsi(pesan, pilihan):
    # Menampilkan pilihan interaktif menggunakan InquirerPy.
    return inquirer.select(
        message=pesan,
        choices=pilihan,
        instruction="(Gunakan tombol panah dan Enter)"
    ).execute()
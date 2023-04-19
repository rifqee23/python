import random

pilihan = ["Batu", "Gunting", "Kertas", "Kadal", "Spock"]
com = random.choice(pilihan)


class batuguntingkertas:

    def __init__(self, user, computer):
        self.user = user
        self.computer = computer

    def opsi(self):
        if self.user == "Batu":
            print("Anda Memilih Batu")
        elif self.user == "Gunting":
            print("Anda Memilih Gunting")
        elif self.user == "Kertas":
            print("Anda Memilih Kertas")
        elif self.user == "Kadal":
            print("Anda Memilih Kadal")
        else:
            print("Anda Memilih Spock")

        if self.computer == "Batu":
            print("cpu Menggunakan Batu")
        elif self.computer == "Gunting":
            print("cpu Menggunakan Gunting")
        elif self.computer == "Kertas":
            print("cpu Menggunakan Kertas")
        elif self.computer == "Kadal":
            print("cpu Menggunakan Kadal")
        else:
            print("cpu Menggunakan Spock")

    def permainan(self):
        if self.user == "Batu" and self.computer == "Gunting":
            print("Anda Menang! Woohoo! ")
        elif self.user == "Gunting" and self.computer == "Kertas":
            print("Anda Menang! Woohoo! ")
        elif self.user == "Kertas" and self.computer == "Batu":
            print("Anda Menang! Woohoo! ")
        elif self.user == "Kadal" and self.computer == "Spock":
            print("Anda Menang! Woohoo! ")
        elif self.user == "Spock" and self.computer == "Gunting":
            print("Anda Menang! Woohoo! ")
        elif self.user == "Gunting" and self.computer == "Kadal":
            print("Anda Menang! Woohoo! ")
        elif self.user == "Kadal" and self.computer == "Kertas":
            print("Anda Menang! Woohoo! ")
        elif self.user == "Kertas" and self.computer == "Spock":
            print("Anda Menang! Woohoo! ")
        elif self.user == "Spock" and self.computer == "Batu":
            print("Anda Menang! Woohoo! ")
        elif self.user == "Batu" and self.computer == "Kadal":
            print("Anda Menang! Woohoo! ")
        elif self.user == self.computer:
            print("Ini Draw")
        else:
            print("Anda Kalah! huuuu")


def mainkan():
    print("---------------------------------------------")
    print("Game Suit Batu, Gunting, Kertas, Kadal, Spock")
    print("---------------------------------------------")

    print("Masukkan Pilihan yang ingin anda mainkan:")
    print("1. Batu")
    print("2. Gunting")
    print("3. Kertas")
    print("4. Kadal")
    print("5. Spock")

    user = int(input("Masukkan pilihan(1,2,3,4,5): "))

    if user not in ['1', '2', '3', '4', '5']:
        print("invalid")

import tkinter as tk
from tkinter import messagebox
from random import randint

class OknoDodawaniaPracownika:
    def __init__(self, root):
        self.generowane_haslo = ""
        self.root = root
        root.title("Dodaj pracownika Dominik Zuziak")
        root.configure(bg="LightSteelBlue")

        # Dane pracownika 
        ramka_dane = tk.LabelFrame(root, text="Dane pracownika", bg="LightSteelBlue")
        ramka_dane.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        tk.Label(ramka_dane, text="Imię:", bg="LightSteelBlue").grid(row=0, column=0, sticky="w")
        self.pole_imie = tk.Entry(ramka_dane)
        self.pole_imie.grid(row=0, column=1, pady=2)

        tk.Label(ramka_dane, text="Nazwisko:", bg="LightSteelBlue").grid(row=1, column=0, sticky="w")
        self.pole_nazwisko = tk.Entry(ramka_dane)
        self.pole_nazwisko.grid(row=1, column=1, pady=2)

        tk.Label(ramka_dane, text="Stanowisko:", bg="LightSteelBlue").grid(row=2, column=0, sticky="w")
        self.wybrane_stanowisko = tk.StringVar(value="Kierownik")
        stanowiska = ["Kierownik", "Starszy programista", "Młodszy programista", "Tester"]
        self.menu_stanowisk = tk.OptionMenu(ramka_dane, self.wybrane_stanowisko, *stanowiska)
        self.menu_stanowisk.grid(row=2, column=1, sticky="ew", pady=2)

        # Generowanie hasła
        ramka_haslo = tk.LabelFrame(root, text="Generowanie hasła", bg="LightSteelBlue")
        ramka_haslo.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        tk.Label(ramka_haslo, text="Ile znaków?", bg="LightSteelBlue").grid(row=0, column=0, sticky="w")
        self.pole_liczba_znakow = tk.Entry(ramka_haslo, width=5)
        self.pole_liczba_znakow.grid(row=0, column=1, sticky="w")

        self.czy_male_duze = tk.BooleanVar(value=True)
        self.czy_cyfry = tk.BooleanVar(value=False)
        self.czy_specjalne = tk.BooleanVar(value=False)

        self.cb_male_duze = tk.Checkbutton(
            ramka_haslo, text="Małe i wielkie litery",
            variable=self.czy_male_duze, bg="LightSteelBlue"
        )
        self.cb_male_duze.grid(row=1, columnspan=2, sticky="w")
        self.cb_cyfry = tk.Checkbutton(
            ramka_haslo, text="Cyfry",
            variable=self.czy_cyfry, bg="LightSteelBlue"
        )
        self.cb_cyfry.grid(row=2, columnspan=2, sticky="w")
        self.cb_specjalne = tk.Checkbutton(
            ramka_haslo, text="Znaki specjalne",
            variable=self.czy_specjalne, bg="LightSteelBlue"
        )
        self.cb_specjalne.grid(row=3, columnspan=2, sticky="w")

        self.przycisk_generuj = tk.Button(
            ramka_haslo, text="Generuj hasło", bg="SteelBlue", fg="white",
            width=16, command=self.generuj_haslo
        )
        self.przycisk_generuj.grid(row=4, column=0, columnspan=2, pady=(12, 0))

        # Przycisk Zatwierdź
        self.przycisk_zatwierdz = tk.Button(
            root, text="Zatwierdź", bg="SteelBlue", fg="white",
            width=20, command=self.okno_zatwierdzenia
        )
        self.przycisk_zatwierdz.grid(row=1, column=0, columnspan=2, pady=12)

        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)

    def okno_pokaz_haslo(self):
        messagebox.showinfo("", self.generowane_haslo)

    def okno_za_malo_znakow(self):
        messagebox.showerror(
            "Błąd przy generowaniu hasła",
            "Wprowadzona liczba znaków hasła jest zbyt mała, aby dodać do niej wybrane znaki. Odznacz część dodatkowych grup znaków."
        )

    def okno_zatwierdzenia(self):
        imie = self.pole_imie.get()
        nazwisko = self.pole_nazwisko.get()
        stanowisko = self.wybrane_stanowisko.get()
        messagebox.showinfo(
            "",
            f"Dane pracownika: {imie} {nazwisko} {stanowisko} Hasło: {self.generowane_haslo}"
        )

    def generuj_haslo(self):
        try:
            dlugosc = int(self.pole_liczba_znakow.get())
        except ValueError:
            messagebox.showerror("Błąd", "Wpisz liczbę znaków!")
            return

        czy_male_duze = self.czy_male_duze.get()
        czy_cyfry = self.czy_cyfry.get()
        czy_specjalne = self.czy_specjalne.get()

        malel = "abcdefghijklmnopqrstuvwxyz"
        duzel = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        cyfry = "0123456789"
        znaki_specjalne = "!@#$%^&*()_+-="

        haslo = ""
        for i in range(dlugosc):
            losowy = randint(0, len(malel) - 1)
            haslo += malel[losowy]

        wymagane = 1 if czy_male_duze else 0
        wymagane += 1 if czy_cyfry else 0
        wymagane += 1 if czy_specjalne else 0

        if wymagane > dlugosc:
            self.okno_za_malo_znakow()
            return

        zablokowane_indexy = []

        if czy_male_duze:
            i = -1
            while i == -1 or i in zablokowane_indexy:
                i = randint(0, len(haslo) - 1)
            losowy_duza = randint(0, len(duzel) - 1)
            haslo = haslo[:i] + duzel[losowy_duza] + haslo[i + 1:]
            zablokowane_indexy.append(i)

        if czy_cyfry:
            i = -1
            while i == -1 or i in zablokowane_indexy:
                i = randint(0, len(haslo) - 1)
            losowa_cyfra = randint(0, len(cyfry) - 1)
            haslo = haslo[:i] + cyfry[losowa_cyfra] + haslo[i + 1:]
            zablokowane_indexy.append(i)

        if czy_specjalne:
            i = -1
            while i == -1 or i in zablokowane_indexy:
                i = randint(0, len(haslo) - 1)
            losowy_znak = randint(0, len(znaki_specjalne) - 1)
            haslo = haslo[:i] + znaki_specjalne[losowy_znak] + haslo[i + 1:]
            zablokowane_indexy.append(i)

        self.generowane_haslo = haslo
        self.okno_pokaz_haslo()


if __name__ == '__main__':
    root = tk.Tk()
    app = OknoDodawaniaPracownika(root)
    root.mainloop()

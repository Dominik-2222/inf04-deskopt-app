import tkinter as tk
from tkinter import messagebox
from random import randint

class AddEmployeeWindow:
    def __init__(self, root):
        self.generated_password = ""
        self.root = root
        root.title("Dodaj pracownika Dominik Zuziak")
        root.configure(bg="LightSteelBlue")

        # Dane pracownika 
        dane_frame = tk.LabelFrame(root, text="Dane pracownika", bg="LightSteelBlue")
        dane_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        tk.Label(dane_frame, text="Imię:", bg="LightSteelBlue").grid(row=0, column=0, sticky="w")
        self.name_input = tk.Entry(dane_frame)
        self.name_input.grid(row=0, column=1, pady=2)

        tk.Label(dane_frame, text="Nazwisko:", bg="LightSteelBlue").grid(row=1, column=0, sticky="w")
        self.Nazwisko = tk.Entry(dane_frame)
        self.Nazwisko.grid(row=1, column=1, pady=2)

        tk.Label(dane_frame, text="Stanowisko:", bg="LightSteelBlue").grid(row=2, column=0, sticky="w")
        self.position_combo = tk.StringVar(value="Kierownik")
        stanowiska = ["Kierownik", "Starszy programista", "Młodszy programista", "Tester"]
        self.position_menu = tk.OptionMenu(dane_frame, self.position_combo, *stanowiska)
        self.position_menu.grid(row=2, column=1, sticky="ew", pady=2)

        # Generowanie hasła
        haslo_frame = tk.LabelFrame(root, text="Generowanie hasła", bg="LightSteelBlue")
        haslo_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        tk.Label(haslo_frame, text="Ile znaków?", bg="LightSteelBlue").grid(row=0, column=0, sticky="w")
        self.character_number_input = tk.Entry(haslo_frame, width=5)
        self.character_number_input.grid(row=0, column=1, sticky="w")

        self.lowercase_and_uppercase_var = tk.BooleanVar(value=True)
        self.digits_var = tk.BooleanVar(value=False)
        self.special_var = tk.BooleanVar(value=False)

        self.lowercase_and_uppercase_cb = tk.Checkbutton(
            haslo_frame, text="Małe i wielkie litery",
            variable=self.lowercase_and_uppercase_var, bg="LightSteelBlue"
        )
        self.lowercase_and_uppercase_cb.grid(row=1, columnspan=2, sticky="w")
        self.digits_cb = tk.Checkbutton(
            haslo_frame, text="Cyfry",
            variable=self.digits_var, bg="LightSteelBlue"
        )
        self.digits_cb.grid(row=2, columnspan=2, sticky="w")
        self.special_cb = tk.Checkbutton(
            haslo_frame, text="Znaki specjalne",
            variable=self.special_var, bg="LightSteelBlue"
        )
        self.special_cb.grid(row=3, columnspan=2, sticky="w")

        self.generate_btn = tk.Button(
            haslo_frame, text="Generuj hasło", bg="SteelBlue", fg="white",
            width=16, command=self.generate_password
        )
        self.generate_btn.grid(row=4, column=0, columnspan=2, pady=(12, 0))

        # --- Przycisk Zatwierdź ---
        self.zatwierdz = tk.Button(
            root, text="Zatwierdź", bg="SteelBlue", fg="white",
            width=20, command=self.apply_messagebox
        )
        self.zatwierdz.grid(row=1, column=0, columnspan=2, pady=12)

        # Szerokość okna
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)

    def show_password_messagebox(self):
        messagebox.showinfo("", self.generated_password)

    def not_enough_chars_messagebox(self):
        messagebox.showerror(
            "Błąd przy generowaniu hasła",
            "Wprowadzona liczba znaków hasła jest zbyt mała, aby dodać do niej wybrane znaki. Odznacz część dodatkowych grup znaków."
        )

    def apply_messagebox(self):
        name = self.name_input.get()
        surname = self.Nazwisko.get()
        position = self.position_combo.get()
        messagebox.showinfo(
            "",
            f"Dane pracownika: {name} {surname} {position} Hasło: {self.generated_password}"
        )

    def generate_password(self):
        try:
            password_length = int(self.character_number_input.get())
        except ValueError:
            messagebox.showerror("Błąd", "Wpisz liczbę znaków!")
            return

        include_lowercase_and_uppercase = self.lowercase_and_uppercase_var.get()
        include_digits = self.digits_var.get()
        include_special_characters = self.special_var.get()

        lowercase_character_set = "abcdefghijklmnopqrstuvwxyz"
        uppercase_character_set = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        digits_character_set = "0123456789"
        special_characters_set = "!@#$%^&*()_+-="

        generated_password = ""
        for i in range(password_length):
            random_number = randint(0, len(lowercase_character_set) - 1)
            generated_password += lowercase_character_set[random_number]

        required_number_of_chars = 1 if include_lowercase_and_uppercase else 0
        required_number_of_chars += 1 if include_digits else 0
        required_number_of_chars += 1 if include_special_characters else 0

        if required_number_of_chars > password_length:
            self.not_enough_chars_messagebox()
            return

        blocked_password_character_indexes = []

        if include_lowercase_and_uppercase:
            random_index = -1
            while random_index == -1 or random_index in blocked_password_character_indexes:
                random_index = randint(0, len(generated_password) - 1)
            random_uppercase_char_index = randint(0, len(uppercase_character_set) - 1)
            generated_password = (generated_password[:random_index] +
                                  uppercase_character_set[random_uppercase_char_index] +
                                  generated_password[random_index + 1:])
            blocked_password_character_indexes.append(random_index)

        if include_digits:
            random_index = -1
            while random_index == -1 or random_index in blocked_password_character_indexes:
                random_index = randint(0, len(generated_password) - 1)
            random_digit_index = randint(0, len(digits_character_set) - 1)
            generated_password = (generated_password[:random_index] +
                                  digits_character_set[random_digit_index] +
                                  generated_password[random_index + 1:])
            blocked_password_character_indexes.append(random_index)

        if include_special_characters:
            random_index = -1
            while random_index == -1 or random_index in blocked_password_character_indexes:
                random_index = randint(0, len(generated_password) - 1)
            random_special_char_index = randint(0, len(special_characters_set) - 1)
            generated_password = (generated_password[:random_index] +
                                  special_characters_set[random_special_char_index] +
                                  generated_password[random_index + 1:])
            blocked_password_character_indexes.append(random_index)

        self.generated_password = generated_password
        self.show_password_messagebox()


if __name__ == '__main__':
    root = tk.Tk()
    app = AddEmployeeWindow(root)
    root.mainloop()

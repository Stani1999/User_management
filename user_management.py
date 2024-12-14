import os, json, string, random

USER_DATA = "data/users.json"

def ensure_directory_exists(directory):
    """Tworzy katalog, jeśli jeszcze nie istnieje."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def load_users():
    """Wczytuje dane użytkowników z pliku JSON."""
    users = {"users": []}
    try:
        with open(USER_DATA, "r") as file:
            return json.load(file)
    except (IOError, json.decoder.JSONDecodeError):
        return users

def save_users(users):
    """Sava file with users data"""
    ensure_directory_exists(os.path.dirname(USER_DATA))
    with open(USER_DATA, "w") as file:
        json.dump(users, file, indent=4)

def print_users(users):
    """Print list of users."""
    print("\nLista użytkowników:")
    if not users["users"]:
        print("Brak użytkowników.")
        return

    for u in users["users"]:
        user_id = u.get("user_id", "Nie podano")
        name = u.get("name", "Nie podano")
        pesel = u.get("pesel", "Nie podano")
        nip = u.get("nip", "Nie podano")
        regon = u.get("regon", "Nie podano")
        print(f"ID: {user_id}, Imię i nazwisko: {name}, PESEL: {pesel}, NIP: {nip}, REGON: {regon}")

"""Users operations"""

def add_user(user_data):
    """Dodaje nowego użytkownika do pliku users.json."""
    users = load_users()
    users["users"].append(user_data)
    save_users(users)
    print("\nUżytkownik został dodany.")

def remove_user(user_id):
    """Usuwa użytkownika o podanym ID."""
    users = load_users()
    updated_users = [u for u in users["users"] if u.get("user_id") != user_id]
    if len(updated_users) == len(users["users"]):
        print("\nNie znaleziono użytkownika o podanym ID.")
    else:
        users["users"] = updated_users
        save_users(users)
        print("\nUżytkownik został usunięty.")

def edit_user(user_id, updated_data):
    """Edytuje dane istniejącego użytkownika."""
    users = load_users()
    for user in users["users"]:
        if user.get("user_id") == user_id:
            user.update(updated_data)
            save_users(users)
            print("\nDane użytkownika zostały zaktualizowane.")
            return
    print("\nNie znaleziono użytkownika o podanym ID.")

"""Walidation section"""

def validate_pesel(pesel):
    """Validate pesel number."""
    if len(pesel) != 11 or not pesel.isdigit():
        return False

    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    control_sum = sum(int(pesel[i]) * weights[i] for i in range(10))
    control_digit = (10 - (control_sum % 10)) % 10
    return control_digit == int(pesel[10])

def validate_nip(nip):
    """Waliduje numer NIP."""
    if len(nip) != 10 or not nip.isdigit():
        return False

    weights = [6, 5, 7, 2, 3, 4, 5, 6, 7]
    control_sum = sum(int(nip[i]) * weights[i] for i in range(9))
    control_digit = control_sum % 11
    return control_digit == int(nip[9]) if control_digit < 10 else False

def validate_regon(regon):
    """Waliduje numer REGON."""
    if len(regon) not in [9, 14] or not regon.isdigit():
        return False

    if len(regon) == 9:
        weights = [8, 9, 2, 3, 4, 5, 6, 7]
    else:
        weights = [2, 4, 8, 5, 0, 9, 7, 3, 6, 1, 2, 4, 8]

    control_sum = sum(int(regon[i]) * weights[i] for i in range(len(weights)))
    control_digit = control_sum % 11
    return control_digit == int(regon[len(weights)])

"""Password section"""

def generate_password(length=12):
    """Generuje silne hasło."""
    if length < 8:
        raise ValueError("Hasło musi mieć przynajmniej 8 znaków.")
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def validate_password(password):
    """Waliduje siłę hasła."""
    if len(password) < 8:
        return False, "Hasło jest za krótkie."
    if not any(c.islower() for c in password):
        return False, "Hasło musi zawierać małe litery."
    if not any(c.isupper() for c in password):
        return False, "Hasło musi zawierać wielkie litery."
    if not any(c.isdigit() for c in password):
        return False, "Hasło musi zawierać cyfry."
    if not any(c in string.punctuation for c in password):
        return False, "Hasło musi zawierać znaki specjalne."
    return True, "Hasło jest silne."

def main():
    """Program main interface"""
    users = load_users()
    while True:
        try:
            print("\nAby kontynuować wybierz jedną z poniższych opcji:")
            print("1. Wyświetl listę użytkowników")
            print("2. Dodaj użytkownika")
            print("3. Usuń użytkownika")
            print("4. Modyfikuj użytkownika")
            print("5. Zapisz i wyjdź")
            option = input("Wybór: ")

            if option == "1":
                print_users(users)
            elif option == "2":
                user_id = input("Podaj ID użytkownika: ")
                name = input("Podaj imię i nazwisko: ")
                pesel = input("Podaj PESEL (opcjonalne): ") or None
                nip = input("Podaj NIP (opcjonalne): ") or None
                regon = input("Podaj REGON (opcjonalne): ") or None
                user_data = {
                    "user_id": user_id,
                    "name": name,
                    "pesel": pesel,
                    "nip": nip,
                    "regon": regon
                }
                add_user(user_data)
                users = load_users()
            elif option == "3":
                user_id = input("Podaj ID użytkownika do usunięcia: ")
                remove_user(user_id)
                users = load_users()
            elif option == "4":
                user_id = input("Podaj ID użytkownika do modyfikacji: ")
                print("Podaj nowe dane użytkownika (pozostaw puste, aby zachować bieżące dane):")
                name = input("Nowe imię i nazwisko: ") or None
                pesel = input("Nowy PESEL (opcjonalne): ") or None
                nip = input("Nowy NIP (opcjonalne): ") or None
                regon = input("Nowy REGON (opcjonalne): ") or None
                updated_data = {k: v for k, v in {
                    "name": name,
                    "pesel": pesel,
                    "nip": nip,
                    "regon": regon
                }.items() if v is not None}
                edit_user(user_id, updated_data)
                users = load_users()
            elif option == "5":
                save_users(users)
                print(f"\nZapisano dane użytkowników do pliku {USER_DATA}. Do zobaczenia!")
                break
            else:
                print("Nieprawidłowy wybór. Wybierz liczbę z listy.")
        except ValueError:
            print("Nieprawidłowe dane wejściowe. Wybierz liczbę z listy.")

# Uruchomienie programu
if __name__ == "__main__":
    main()
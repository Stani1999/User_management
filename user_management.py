import json, random, re, os, string

# DIR STRUCTURE 
DATA_DIR = "data"
USER_FILE = "users.json"
USER_DATA = (f"{DATA_DIR}/{USER_FILE}")

def ensure_directory_exists(directory):
    '''
    Create directory file if does'nt exist yet.
    '''
    if not os.path.exists(directory):
        os.makedirs(directory)

# Minimum characters in password declaration :
Min_password_characters = 8

def load_users():
    users = {}
    try:
        with open(USER_DATA, "r") as file:
            return json.load(file)
    except IOError:
        False
    except json.decoder.JSONDecodeError:
        False
    return users 

users = load_users()
       
def print_users(users):
    """
    Wyświetla listę użytkowników.
    """
    print("")  # Odstęp dla lepszej czytelności
    for u in users["users"]:
        user_id = u.get("user_id", "Nie podano")
        name = u.get("name", "Nie podano")
        print(f"Użytkownik o ID {user_id}, to Pan(i): {name}")


def dump_users(users):
    """
    Zapisuje dane użytkowników do pliku JSON.
    """
    with open(USER_DATA) as file:
        return json.dump(users, file, indent = 4)    

def add_user(user_data): #Dodaje nowego użytkownika.
    pass
#    Dodanie nowego użytkownika do pliku json
#    if not validate_numbers(uers_data):


def remove_user(user_id): #Usuwa istniejącego użytkownika.
    pass

def edit_user(user_id, updated_data): #Edytuje dane użytkownika.
    pass

def validate_nip(nip):
    """Waliduje numer NIP."""
    if len(nip) != 10 or not nip.isdigit():
        return False

    weights = [6, 5, 7, 2, 3, 4, 5, 6, 7]
    control_sum = sum(int(nip[i]) * weights[i] for i in range(9))
    control_digit = control_sum % 11

    # Wartość kontrolna musi być liczbą jednocyfrową (0–9)
    return control_digit == int(nip[9]) if control_digit < 10 else False

def validate_pesel(pesel):
    """Waliduje numer PESEL."""
    if len(pesel) != 11 or not pesel.isdigit():
        return False

    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    control_sum = sum(int(pesel[i]) * weights[i] for i in range(10))
    control_digit = (10 - (control_sum % 10)) % 10

    return control_digit == int(pesel[10])

def validate_regon(regon):
    """Waliduje numer REGON."""
    if len(regon) not in [9, 14] or not regon.isdigit():
        return False

    if len(regon) == 14:
        weights = [8, 9, 2, 3, 4, 5, 6, 7]
    else:
        weights = [2, 4, 8, 5, 0, 9, 7, 3, 6, 1, 2, 4, 8]

    control_sum = sum(int(regon[i]) * weights[i] for i in range(len(weights)))
    control_digit = control_sum % 11
    control_digit = 0 if control_digit == 10 else control_digit

    return control_digit == int(regon[len(weights)])

def generate_password():
    """Generuje silne hasło."""
    length = 12 # Długość generowanego hasła
    if length < Min_password_characters :
        raise ValueError(f"Hasło powinno mieć przynajmniej {Min_password_characters} znaków.")

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def validate_password(password):
    """Waliduje siłę hasła."""
    if len(password) < Min_password_characters:
        return False, f"Hasło jest za krótkie (minimum {Min_password_characters} znaków)."

    if not any(char.islower() for char in password):
        return False, "Hasło powinno zawierać przynajmniej jedną małą literę."

    if not any(char.isupper() for char in password):
        return False, "Hasło powinno zawierać przynajmniej jedną wielką literę."

    if not any(char.isdigit() for char in password):
        return False, "Hasło powinno zawierać przynajmniej jedną cyfrę."

    if not any(char in string.punctuation for char in password):
        return False, "Hasło powinno zawierać przynajmniej jeden znak specjalny."

    return True, "Hasło jest wystarczająco silne."

def main():
    ensure_directory_exists(DATA_DIR)
    dump_users(users)
    while True: 
        try:
            option = int(input(
                "\nAby kontynuować wybierz jedną z poniższych opcji:\n"
                "1. Wyświetl listę użytkowników\n"
                "2. Dodaj Użytkownika\n"
                "3. Usuń użytkownika\n"
                "4. Modyfikuj użytkownika\n"
                "5. Zapisz i wyjdź\n"
                "Wybór: "
            ))
            if option == 1:
                print_users(users)
            elif option == 2:
                add_user(user_data)
            elif option == 3:
                print (f"")
                remove_user(user_id)
            elif option == 4:
                edit_user(user_id, updated_data)
            elif option == 5:
                print("\nProgram zakończył działanie. Do zobaczenia!")
                print(f"\nZapisano dane użytkowników do pliku {USER_DATA}.")
                break          
            else:
                print("Nieprawidłowy wybór. Wybierz liczbę z listy")
        except ValueError:
            print("Nieprawidłowe dane wejściowe. Wybierz liczbę z listy.")

# Uruchomienie programu
if __name__ == "__main__":
    main()
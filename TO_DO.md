Tutorial: System Zarządzania Użytkownikami - user_management.py
Struktura plików i branchy
Struktura plików:

user_management.py: Główny plik aplikacji do zarządzania użytkownikami.
data/: Katalog do przechowywania danych użytkowników.
users.json: Plik przechowujący informacje o użytkownikach.
README.md: Dokumentacja projektu.
Branchy w Git:

main: Główna gałąź projektu zawierająca stabilną wersję aplikacji.
feature/user_management: Gałąź do implementacji funkcji zarządzania użytkownikami.
feature/password_validation: Gałąź do implementacji funkcji walidacji hasł.
Nazwy funkcji:

add_user(user_data): Dodaje nowego użytkownika.
remove_user(user_id): Usuwa istniejącego użytkownika.
edit_user(user_id, updated_data): Edytuje dane użytkownika.
validate_nip(nip): Waliduje numer NIP.
validate_pesel(pesel): Waliduje numer PESEL.
validate_regon(regon): Waliduje numer REGON.
generate_password(): Generuje silne hasło.
validate_password(password): Waliduje siłę hasła.
Sprint 1: Podstawowe Funkcjonalności Zarządzania Użytkownikami
Milestone 1: Przygotowanie projektu
Stwórz plik projektu: Utwórz nowy plik o nazwie user_management.py.
Utwórz strukturę katalogów: Utwórz katalog data/ do przechowywania informacji o użytkownikach w pliku users.json.
Importuj biblioteki: Dodaj niezbędne importy, takie jak json, random, re oraz os do pracy z plikami i walidacji.
Milestone 2: Implementacja funkcji dodawania i edycji użytkowników
Funkcja add_user(user_data)

Implementuj funkcję, która dodaje nowego użytkownika do pliku users.json.
Waliduj numer PESEL, NIP oraz REGON przed dodaniem użytkownika.
Funkcje walidacji dodaj jako puste funkcje, kod napiszesz pozniej.
Funkcja edit_user(user_id, updated_data)

Implementuj funkcję do edycji danych istniejącego użytkownika.
Wczytaj dane z pliku users.json, edytuj odpowiedni rekord i zapisz zmodyfikowane dane z powrotem do pliku.
Milestone 3: Praca z plikiem users.json
Funkcja remove_user(user_id)

Implementuj funkcję do usuwania użytkownika na podstawie jego identyfikatora.
Wczytaj dane z pliku users.json, usuń odpowiedni rekord i zapisz zmodyfikowane dane z powrotem do pliku.
Funkcja load_users()

Implementuj funkcję do odczytu istniejących użytkowników z pliku users.json.
Wyświetl wszystkie zapisane informacje o użytkownikach.
Sprint 2: Walidacja i Bezpieczeństwo
Milestone 1: Walidacja danych użytkownika
Funkcja validate_nip(nip)

Numer NIP (Numer Identyfikacji Podatkowej) składa się z 10 cyfr.
Mechanizm tworzenia numeru NIP obejmuje zastosowanie wagi dla każdej cyfry numeru: [6, 5, 7, 2, 3, 4, 5, 6, 7].
W celu walidacji NIP należy przemnożyć każdą z pierwszych dziewięciu cyfr przez odpowiadającą jej wagę, a następnie zsumować wyniki.
Wynik sumowania należy podzielić modulo 11. Jeśli reszta z dzielenia jest równa ostatniej cyfrze numeru NIP, numer jest poprawny.
link do budowy nip https://pl.wikipedia.org/wiki/Numer_identyfikacji_podatkowej
Funkcja validate_pesel(pesel)

Implementuj walidację numeru PESEL.
Sprawdź datę urodzenia i sumę kontrolną.
Budowa pesel - https://www.gov.pl/web/gov/czym-jest-numer-pesel
Funkcja validate_regon(regon)

Implementuj walidację numeru REGON.
Sprawdź poprawność sumy kontrolnej.
Budowa regunu https://pl.wikipedia.org/wiki/REGON
Milestone 2: Generowanie i walidacja hasł
Funkcja generate_password()

Implementuj funkcję generującą silne hasło o minimalnej długości 12 znaków, zawierające duże litery, małe litery, cyfry oraz znaki specjalne.
Funkcja validate_password(password)

Implementuj funkcję walidującą siłę hasła, sprawdzając, czy spełnia minimalne wymagania (długość, złożoność, brak popularnych wzorców).
Sprint 3: Testowanie i Dokumentacja
Milestone 1: Testowanie funkcjonalności
Testowanie dodawania i edycji użytkowników
Przetestuj funkcje add_user(), edit_user(), i remove_user(), aby upewnić się, że działają prawidłowo.
Sprawdź scenariusze, takie jak brak pliku users.json, usuwanie nieistniejącego użytkownika itp.
Milestone 2: Walidacja danych
Testowanie walidacji numerów NIP, PESEL, REGON
Przetestuj funkcje walidujące, aby upewnić się, że rozpoznają błędne i poprawne dane.
Milestone 3: Dokumentacja
Przygotuj dokumentację
Utwórz plik README.md, opisując kroki instalacji oraz używania programu.
Dodaj instrukcje dotyczące dodawania, edycji, usuwania użytkowników oraz wymagania dotyczące walidacji.
Wymień najlepsze praktyki dotyczące zarządzania danymi użytkowników, w tym bezpieczeństwo haseł oraz przechowywanie danych osobowych.
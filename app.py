while True:
    print("Prosty Kalkulator")
    print("Wybierz operację:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")

    wybor = (input("Menu:"))
        
    if wybor == "1":
        liczba_1 = int(input(("Podaj pierwsza liczbe:")))
        liczba_2 = int(input(("Podaj druga liczbe:")))
        wynik = liczba_1+liczba_2
        print(f"Wynik dzialania: {liczba_1} + {liczba_2} = {wynik}")

    if wybor == "2":
        liczba_1 = int(input(("Podaj pierwsza liczbe:")))
        liczba_2 = int(input(("Podaj druga liczbe:")))
        wynik = liczba_1-liczba_2
        print(f"Wynik dzialania: {liczba_1} - {liczba_2} = {wynik}")

    if wybor == "3":
        liczba_1 = int(input(("Podaj pierwsza liczbe:")))
        liczba_2 = int(input(("Podaj druga liczbe:")))
        wynik = liczba_1*liczba_2
        print(f"Wynik dzialania: {liczba_1} * {liczba_2} = {wynik}")
    
    if wybor == "4":
        liczba_1 = int(input(("Podaj pierwsza liczbe:")))
        liczba_2 = int(input(("Podaj druga liczbe:")))
        wynik = liczba_1/liczba_2
        print(f"Wynik dzialania: {liczba_1} / {liczba_2} = {wynik}")
            


    if wybor != "1" and wybor != "2" and wybor != "3" and wybor != "4":
        print("                       ")
        print("!!!!!!!!!!!!!!!!!!!!!!")
        print("Podaj poprawna liczbe")
        print("!!!!!!!!!!!!!!!!!!!!!!")
        print("                       ")
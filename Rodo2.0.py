imie = input("Prosze podaj swoje imie przyjacielu")
nazwisko = input("Prosze podaj swoje nazwisko")
try:
    wiek = int( input("Ile masz lat?"))
except ValueError:
    wiek = 18
    print(wiek)
numerkarty = input("Dawaj swój numer karty kredytowej!!!")
kodCVC = input("I numer CVC!!!")
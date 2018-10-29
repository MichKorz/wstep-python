import sys
import random
import time

 
print("(Jeśli zechcesz zakończyć grę wpisz '5'.)")
time.sleep(0.5)
 
while True:
    print()
 
    wybor = int(input("Wybierasz:\n1.Papier\n2.Kamień\n3.Nożyce\n"))
    wybor_komp = random.randrange(1, 3)
 
    if wybor == 5:
        sys.exit(0)
 
    if wybor == 1 and wybor_komp == 1:
        print("Papier vs Papier")
        print("Remis!")
    elif wybor == 2 and wybor_komp == 2:
        print("Kamień vs Kamień")
        print("Remis!")
    elif wybor == 3 and wybor_komp == 3:
        print("Nożyce vs Nożyce")
        print("Remis!")
 
    if wybor == 1 and wybor_komp == 2:
        print("Papier vs Kamień")
        print("Wygrywasz!")
    elif wybor == 2 and wybor_komp == 3:
        print("Kamień vs Nożyce")
        print("Wygrywasz!")
    elif wybor == 3 and wybor_komp == 1:
        print("Nożyce vs Papier")
        print("Wygrywasz!")
 
    if wybor == 1 and wybor_komp == 3:
        print("Przegrywasz!")
    elif wybor == 2 and wybor_komp == 1:
        print("Kamień vs Papier")
        print("Przegrywasz!")
    elif wybor == 3 and wybor_komp == 2:
        print("Nożyce vs Kamień")
        print("Przegrywasz!")
 
    print()
    input("Wciśnij dowolny przycisk żeby grać dalej")
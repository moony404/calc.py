import colorama
import math
import time
import os
from colorama import Fore
colorama.init(autoreset=True)
#clearConsole()
def clear_console():
    os.system('cls')
i = 1
while (i == 1):
    print(f"{Fore.GREEN}####################")
    print(f"{Fore.GREEN}#{Fore.CYAN}   Calculatrice   {Fore.GREEN}#")
    print(f"{Fore.GREEN}#{Fore.CYAN} 1.Addition       {Fore.GREEN}#")
    print(f"{Fore.GREEN}#{Fore.CYAN} 2.Soustraction   {Fore.GREEN}#")
    print(f"{Fore.GREEN}#{Fore.CYAN} 3.Multiplication {Fore.GREEN}#")
    print(f"{Fore.GREEN}#{Fore.CYAN} 4.Division       {Fore.GREEN}#")
    print(f"{Fore.GREEN}#{Fore.CYAN} 5.Carré          {Fore.GREEN}#")
    print(f"{Fore.GREEN}#{Fore.CYAN} 6.Racine Carré   {Fore.GREEN}#")
    print(f"{Fore.GREEN}####################")
    #programme
    choice = int(input(f"{Fore.YELLOW}Votre choix ?"))
    if choice == 1:
        print(f"{Fore.BLUE}[{Fore.WHITE}calc.py{Fore.BLUE}] {Fore.GREEN}Vous avez choisi Addition.")
        nb1 = int(input(f"{Fore.YELLOW}Premier nombre:"))
        nb2 = int(input(f"{Fore.YELLOW}Deuxieme nombre:"))
        result = (nb1+nb2)
        print(f"{Fore.BLUE}[{Fore.WHITE}calc.py{Fore.BLUE}] {Fore.GREEN}Resultat = ", + result)
    elif choice == 2:
        print(f"{Fore.BLUE}[{Fore.WHITE}calc.py{Fore.BLUE}] {Fore.GREEN}Vous avez choisi Soustraction.")
        nb1 = int(input(f"{Fore.YELLOW}Premier nombre:"))
        nb2 = int(input(f"{Fore.YELLOW}Deuxieme nombre:"))
        result = (nb1-nb2)
        print(f"{Fore.BLUE}[{Fore.WHITE}calc.py{Fore.BLUE}] {Fore.GREEN}Resultat = ", + result)
    elif choice == 3:
        print(f"{Fore.BLUE}[{Fore.WHITE}calc.py{Fore.BLUE}] {Fore.GREEN}Vous avez choisi Multiplication.")
        nb1 = int(input(f"{Fore.YELLOW}Premier nombre:"))
        nb2 = int(input(f"{Fore.YELLOW}Deuxieme nombre:"))
        result = (nb1*nb2)
        print(f"{Fore.BLUE}[{Fore.WHITE}calc.py{Fore.BLUE}] {Fore.GREEN}Resultat = ", + result)
    elif choice == 4:
        print(f"{Fore.BLUE}[{Fore.WHITE}calc.py{Fore.BLUE}] {Fore.GREEN}Vous avez choisi Division.")
        nb1 = int(input(f"{Fore.YELLOW}Premier nombre:"))
        nb2 = int(input(f"{Fore.YELLOW}Deuxieme nombre:"))
        result = (nb1/nb2)
        print(f"{Fore.BLUE}[{Fore.WHITE}calc.py{Fore.BLUE}] {Fore.GREEN}Resultat = ", + result)
    elif choice == 5:
        print(f"{Fore.BLUE}[{Fore.WHITE}calc.py{Fore.BLUE}] {Fore.GREEN}Vous avez choisi Carré.")
        nb = int(input(f"{Fore.YELLOW}Nombre à mettre au carré:"))
        result = (nb*nb)
        print(f"{Fore.BLUE}[{Fore.WHITE}calc.py{Fore.BLUE}] {Fore.GREEN}Resultat = ", + result)
    elif choice == 6:
        print(f"{Fore.BLUE}[{Fore.WHITE}calc.py{Fore.BLUE}] {Fore.GREEN}Vous avez choisi Racine Carré.")
        nb = int(input(f"{Fore.YELLOW}Racine carré de :"))
        result = math.sqrt(nb)
        print(f"{Fore.BLUE}[{Fore.WHITE}calc.py{Fore.BLUE}] {Fore.GREEN}Resultat = ", + result)
    else:
        print(f"{Fore.BLUE}[{Fore.WHITE}calc.py{Fore.BLUE}] {Fore.GREEN}Vous avez envoyé un nombre incorrect !")
        print(f"{Fore.BLUE}[{Fore.WHITE}calc.py{Fore.BLUE}] {Fore.RED}Error 405. Input is false. Error code = {Fore.WHITE}405.")
        time.sleep(5)
        print(f"{Fore.BLUE}[{Fore.WHITE}calc.py{Fore.BLUE}] {Fore.GREEN}The programm will close in 5 seconds..")
        time.sleep(1)
        print(f"{Fore.BLUE}[{Fore.WHITE}calc.py{Fore.BLUE}] {Fore.GREEN}The programm will close in 4 seconds..")
        time.sleep(1)
        print(f"{Fore.BLUE}[{Fore.WHITE}calc.py{Fore.BLUE}] {Fore.GREEN}The programm will close in 3 seconds..")
        time.sleep(1)
        print(f"{Fore.BLUE}[{Fore.WHITE}calc.py{Fore.BLUE}] {Fore.GREEN}The programm will close in 2 seconds..")
        time.sleep(1)
        print(f"{Fore.BLUE}[{Fore.WHITE}calc.py{Fore.BLUE}] {Fore.GREEN}The programm will close in 1 second..")
        time.sleep(1)
        print(f"{Fore.BLUE}[{Fore.WHITE}calc.py{Fore.BLUE}] {Fore.GREEN}The programm will close in 0 second..")
        quit()
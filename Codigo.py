#imports
import math
import random
import colorama
from colorama import Fore, Style

#fichas
f=100

#apostas
"P=PASS LINE BELT"
"F=FIELD"
"A=ANY CRAPS"
"T=TWELVE"

#mudar cor do dialogo
"print(Fore.BLUE+....)"
"print(Fore.YELLOW+ ......)"
"print(Style.RESET_ALL)"

#vitoria= condição de vitória

#Apostar ou Sair
continuar=True
while continuar and f>0:
    #Dados
    numero1=random.randint(1,6)
    numero2=random.randint(1,6)
    soma=soma=numero1+numero2
    #Fase e Fichas
    print("Você está na fase:come out")
    print("Você tem:{0} fichas".format(f))
    pergunta=str(input (Fore.BLUE+"Quer apostar ou sair do jogo?"))
    print(Style.RESET_ALL)
    if pergunta=="sair do jogo":
        continuar=False
    #Escolha do tipo da aposta    
    else:
        print("Você pode apostar no PASS LINE BELT(P); FIELD(F); ANY CRAPS(A); TWELVE(T).")
        tipoP=str(input(Fore.BLUE+"Quer apostar no P (s/n)?"))
        print(Style.RESET_ALL)
        tipoF=str(input(Fore.BLUE+"Quer apostar no F (s/n)?"))
        print(Style.RESET_ALL)
        tipoA=str(input(Fore.BLUE+"Quer apostar no A (s/n)?"))
        print(Style.RESET_ALL)
        tipoT=str(input(Fore.BLUE+"Quer apostar no T (s/n)?"))
        print(Style.RESET_ALL)

        #Aposta T
        if tipoT=="s":
            print("Você apostou no tipo TWELVE:{0} fichas".format(f))
            valorT=int(input(Fore.BLUE+"Quanto você quer apostar?"))
            print(Style.RESET_ALL)
            f=f-valorT
            VitoriaT=12
            if soma==VitoriaT:
                f=f+valorT*31
                print(Fore.YELLOW+"Você ganhou")
                print(Style.RESET_ALL)
            else:
                print(Fore.YELLOW+"Você perdeu") 
                print(Style.RESET_ALL)
        #Aposta A
        if tipoA=="s":
            print("Você apostou no tipo ANY CRAPS:{0} fichas".format(f))
            valorA=int(input(Fore.BLUE+"Quanto você quer apostar?"))
            print(Style.RESET_ALL)
            f=f-valorA
            VitoriaA=2 or 3 or 12
            if soma==VitoriaA:
                f=f+valorA*8
                print(Fore.YELLOW+"Você ganhou")
                print(Style.RESET_ALL)
            else:
                print(Fore.YELLOW+"Você perdeu")
                print(Style.RESET_ALL)

        #Aposta F        
        if tipoF=="s":
            print("Você apostou no tipo FIELD:{0} fichas".format(f))
            valorF=int(input(Fore.BLUE+"Quanto você quer apostar?")) 
            print(Style.RESET_ALL)
            f=f-valorF
            Derrota=5 or 6 or 7 or 8
            Empate=3 or 4 or 9 or 10 or 11
            VitoriaF2=2
            VitoriaF3=12
            if soma==Derrota:
                f=f+0
                print(Fore.YELLOW+ "Você perdeu" )
                print(Style.RESET_ALL)
            elif soma==Empate:
                f=f+valorF
                print(Fore.YELLOW+ "Você recebe sua aposta de volta")
                print(Style.RESET_ALL)
            elif soma==VitoriaF2:
                f=f+valorF*3
                print(Fore.YELLOW+ "Você ganhou x2")
                print(Style.RESET_ALL)
            elif soma==VitoriaF3:
                f=f+valorF*4
                print(Fore.YELLOW+ "Você ganhou x3")
                print(Style.RESET_ALL)

        #Aposta P        
        if tipoP=="s":
            print("Você apostou no tipo PASS LINE BET:{0} fichas".format(f))
            valorP=int(input(Fore.BLUE+"Quanto você quer apostar?"))
            print(Style.RESET_ALL)
            f=f-valorP
            VitoriaP=7 or 11
            PassouP=4 or 5 or 6 or 8 or 9 or 10
            if soma==VitoriaP:
                f=f+valorP*2
                print(Fore.YELLOW+"Você ganhou")
                print(Style.RESET_ALL)
            elif soma==PassouP:
                #Fase Point
                VitoriaPoint=soma
                POINT=True
                while POINT:
                    input("Você está na fase:point")
                    SOMA=(random.randint(1,6) + random.randint(1,6))
                    if SOMA==VitoriaPoint:
                        f=f+valorP
                        POINT=False
                        input("Você ganhou, saindo da fase:point")
                    elif SOMA==7:
                        f=F+0
                        input("Você perdeu, saindo da fase:point")
                    else:
                        SOMA=True
                        input("Você ainda está na fase:point")


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
    soma=5 #teste
    #Fase e Fichas
    print("Você está na fase:come out")
    print("Você tem:{0} fichas".format(f))
    pergunta=str(input (Fore.BLUE+"Quer apostar ou sair do jogo?"))
    print(Style.RESET_ALL)
    if pergunta=="sair do jogo":
        continuar=False 
    #Escolha do tipo da aposta    
    elif pergunta=="apostar":
        print("Você pode apostar no PASS LINE BELT(P); FIELD(F); ANY CRAPS(A); TWELVE(T).")
        tipoP=str(input(Fore.BLUE+"Quer apostar no P (s/n)?"))
        print(Style.RESET_ALL)
        while tipoP!="s" and tipoP!="n":
            tipoP=str(input(Fore.BLUE+"Quer apostar no P (s/n)?"))
            print(Style.RESET_ALL)         
        tipoF=str(input(Fore.BLUE+"Quer apostar no F (s/n)?"))
        print(Style.RESET_ALL)
        while tipoF!="s" and tipoF!="n":
            tipoF=str(input(Fore.BLUE+"Quer apostar no F (s/n)?"))
            print(Style.RESET_ALL)
        tipoA=str(input(Fore.BLUE+"Quer apostar no A (s/n)?"))
        print(Style.RESET_ALL)
        while tipoA!="s" and tipoA!="n":
            tipoA=str(input(Fore.BLUE+"Quer apostar no A (s/n)?"))
            print(Style.RESET_ALL)
        tipoT=str(input(Fore.BLUE+"Quer apostar no T (s/n)?"))
        print(Style.RESET_ALL)
        while tipoT!="s" and tipoT!="n":
            tipoT=str(input(Fore.BLUE+"Quer apostar no T (s/n)?"))
            print(Style.RESET_ALL)

        #Aposta T
        if tipoT=="s":
            print("Você apostou no tipo TWELVE:{0} fichas".format(f))
            valorT=int(input(Fore.BLUE+"Quanto você quer apostar?"))
            print(Style.RESET_ALL)
            f=f-valorT
            if soma==12:
                f=f+valorT*31
                print(Fore.YELLOW+"Você ganhou")
                print(Style.RESET_ALL)
            elif soma==2 or soma==3 or soma==4 or soma==5 or soma==6 or soma==7 or soma==8 or soma==9 or soma==10 or soma==11:
                print(Fore.YELLOW+"Você perdeu") 
                print(Style.RESET_ALL)
        #Aposta A
        if tipoA=="s" and f>0:
            print("Você apostou no tipo ANY CRAPS:{0} fichas".format(f))
            valorA=int(input(Fore.BLUE+"Quanto você quer apostar?"))
            print(Style.RESET_ALL)
            f=f-valorA
            if soma==2 or soma==3 or soma==12:
                f=f+valorA*8
                print(Fore.YELLOW+"Você ganhou")
                print(Style.RESET_ALL)
            elif soma==4 or soma==5 or soma==6 or soma==7 or soma==8 or soma==9 or soma==10 or soma==11:
                print(Fore.YELLOW+"Você perdeu")
                print(Style.RESET_ALL)

        #Aposta F        
        if tipoF=="s" and f>0:
            print("Você apostou no tipo FIELD:{0} fichas".format(f))
            valorF=int(input(Fore.BLUE+"Quanto você quer apostar?")) 
            print(Style.RESET_ALL)
            f=f-valorF
            if soma==5 or soma==6 or soma==7 or soma==8:
               #f foi mantido ja que nao ha alteracoes
                print(Fore.YELLOW+ "Você perdeu" )
                print(Style.RESET_ALL)
            elif soma==3 or soma==4 or soma==9 or soma==10 or soma==11:
                f=f+valorF
                print(Fore.YELLOW+ "Você recebe sua aposta de volta")
                print(Style.RESET_ALL)
            elif soma==2:
                f=f+valorF*3
                print(Fore.YELLOW+ "Você ganhou x2")
                print(Style.RESET_ALL)
            elif soma==12:
                f=f+valorF*4
                print(Fore.YELLOW+ "Você ganhou x3")
                print(Style.RESET_ALL)

        #Aposta P        
        if tipoP=="s" and f>0:
            print("Você apostou no tipo PASS LINE BET:{0} fichas".format(f))
            valorP=int(input(Fore.BLUE+"Quanto você quer apostar?"))
            print(Style.RESET_ALL)
            f=f-valorP
            if soma==7 or soma==11:
                f=f+valorP*2
                print(Fore.YELLOW+"Você ganhou")
                print(Style.RESET_ALL)
            elif soma==4 or soma==5 or soma==6 or soma==8 or soma==9 or soma==10:
                #Fase Point
                VitoriaPoint=soma
                Point=True
                while Point:
                    print("Você está na fase:point")
                    print("Você pode apostar no FIELD(F); ANY CRAPS(A); TWELVE(T).")
                    SOMA=(random.randint(1,6) + random.randint(1,6))
                    if SOMA==VitoriaPoint:
                        f=f+valorP
                        POINT=False
                        print("Você ganhou, saindo da fase:point")
                    elif SOMA==7:
                        #f foi mantido ja que nao ha alteracoes
                        print("Você perdeu, saindo da fase:point")
                        Point=False
                    else:
                        SOMA=True
                        print("Você ainda está na fase:point")
                    #Apostas dentro do Point
                    continuapoint=True
                    while continuapoint and f>0:
                        print("Você tem:{0} fichas".format(f))
                        perguntaP=str(input (Fore.BLUE+"Quer apostar mais(s/n)?"))
                        print(Style.RESET_ALL)
                        while perguntaP!="s" and perguntaP!="n":
                            perguntaP=str(input (Fore.BLUE+"Quer apostar mais(s/n)?"))
                            if perguntaP=="n":
                                continuapoint=False
                            #Escolha do tipo da aposta    
                            elif perguntaP=="s":
                                print("Você pode apostar no FIELD(F); ANY CRAPS(A); TWELVE(T).")  
                                tipoF=str(input(Fore.BLUE+"Quer apostar no F (s/n)?"))
                                print(Style.RESET_ALL)
                                while tipoF!="s" and tipoF!="n":
                                    tipoF=str(input(Fore.BLUE+"Quer apostar no F (s/n)?"))
                                    print(Style.RESET_ALL)
                                tipoA=str(input(Fore.BLUE+"Quer apostar no A (s/n)?"))
                                print(Style.RESET_ALL)
                                while tipoA!="s" and tipoA!="n":
                                    tipoA=str(input(Fore.BLUE+"Quer apostar no A (s/n)?"))
                                    print(Style.RESET_ALL)
                                tipoT=str(input(Fore.BLUE+"Quer apostar no T (s/n)?"))
                                print(Style.RESET_ALL)
                                while tipoT!="s" and tipoT!="n":
                                    tipoT=str(input(Fore.BLUE+"Quer apostar no T (s/n)?"))
                                    print(Style.RESET_ALL)
    # garante que a resposta seja apenas apostar ou sair do jogo 
    else:
         pass
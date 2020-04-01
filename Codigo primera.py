#imports
import math
import random

#conceitos basicos do codigo
#dados
n1=random.randint(1,6)
n2=random.randint(1,6)
soma=n1+n2

#fases
fc="Come Out"
fp="Point"

#fichas
f=100

#apostas
P="Pass Line Belt"
F="Field"
A="Any Craps"
T="Twelve"

continuar=True
while continuar and f>0:
    print("Você está na fase:come out")
    print("Você tem:{0} fichas".format(f))
    pergunta=str(input("Quer apostar ou sair do jogo?"))
    if pergunta=="sair do jogo":
        continuar=False
    else:
        print("Você pode apostar no PASS LINE BELT(P); FIELD(F); ANY CRAPS(A); TWELVE(T).")
        tipoP=str(input("Quer apostar no P (s/n)?"))
        tipoF=str(input("Quer apostar no F (s/n)?"))
        tipoA=str(input("Quer apostar no A (s/n)?"))
        tipoT=str(input("Quer apostar no T (s/n)?"))
        if tipoT=="s":
            print("Você tem:{0} fichas".format(f))
            valorT=int(input("Quanto você quer apostar?"))
            f=f-valorT
            V=12
            if soma==V:
                f=f+valorT*31
                print("Você ganhou")
            else:
                print("Você perdeu") 
        elif tipoA=="s":
            print("Você tem:{0} fichas".format(f))
            valorA=int(input("Quanto você quer apostar?"))
            f=f-valorA
            V=2 or V=3 or V=12
            if soma==V:
                f=f+valorA*8
                print("Você ganhou")
            else:
                print("Você perdeu")
        elif tipoF=="s"
            print("Você tem:{0} fichas".format(f))
            valorF=int(input("Quanto você quer apostar?")) 
            f=f-valorT
            v1=5 or v1=6 or v1=7 or v1=8
            v2=3 or v=4 or v2=9 or v2=10 or v2=11
            v3=2
            v4=12
            if soma==v1:
                f=0
                print("Você perdeu")
            elif soma==v2:
                f=f+valorT
                print("Você recebe sua aposta de volta")
            elif soma==v3:
                f=f+valorT*3
                print("Você ganhou")
            elif soma==v4:
                f=f+valorT*4
                print("Você ganhou")
    
    
    
    
    
    
    
    
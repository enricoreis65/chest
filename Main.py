
import sys
from os import path
from mapa import *
for i in range(8):
    pioes=piao("b",f"{chr(65+i)}2")
    pioes=piao("p",f"{chr(65+i)}7")


game=True
tabuleiro.printar_tabuleiro()
while game==True:
    jogar=input("s ou n ")
    if jogar=="s":
        movi=str(input("movimento ")).upper()
        identifica=movi[0:2]
        
        
        tabuleiro.atualiza_tabuleiro(movi)
    else:
        game=False



import sys
import numpy as np
from os import path
from scaner import *
from pecas import *
from Main import lista2
dicionario_pos={}
class tabuleiro:
    def __init__(self):
        
        self.ta=lista2
    def printar_tabuleiro(self):
        print(*self.ta ,sep = "\n")
        
    def atualiza_tabuleiro(self,pos):
        if len(pos)==4:
            if dicionario_pos[pos[0:2]][0].verifica_mov(pos)==True:
                self.ta[scaner(pos)[0]][scaner(pos)[1]]="  "
                self.ta[scaner(pos)[2]][scaner(pos)[3]]=dicionario_pos[pos[0:2]][1]
            
                dicionario_pos[pos[2:4]]=dicionario_pos[pos[0:2]][1]
                dicionario_pos[pos[0:2]]='  '
                self.printar_tabuleiro()
            else:
                self.printar_tabuleiro()
        if len(pos)==2:
            self.ta[scaner(pos)[0]][scaner(pos)[1]]=dicionario_pos[pos[0:2]][1]
            
tabuleiro=tabuleiro()   



for i in range(8):
    pioes=piao("b",f"{chr(65+i)}2")
    pioes=piao("p",f"{chr(65+i)}7")


game=True
tabuleiro.printar_tabuleiro()
while game==True:
    jogar=input("s ou n ")
    if jogar=="s":
        movi=str(input("movimento")).upper()
        identifica=movi[0:2]
        
        tabuleiro.atualiza_tabuleiro(movi)
    else:
        game=False
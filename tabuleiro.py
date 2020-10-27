import sys
import numpy as np
from os import path
from scaner import *
from pecas import *

class tabuleiro:
    def __init__(self):
        self.ta=np.zeros((8,8), dtype=int)
        self.ta=self.ta.tolist()
    def printar_tabuleiro(self):
        print(*self.ta ,sep = "\n")
        print(*".",sep="\n")
    def atualiza_tabuleiro(self,pos):
        if len(pos)==4:
            
            self.ta[scaner(pos)[0]][scaner(pos)[1]]=0
            self.ta[scaner(pos)[2]][scaner(pos)[3]]=dicionario_pos[pos[0:2]][1]

            dicionario_pos[pos[2:4]]=dicionario_pos[pos[0:2]][1]
            dicionario_pos[pos[0:2]]=0
            self.printar_tabuleiro()
        if len(pos)==2:
            self.ta[scaner(pos)[0]][scaner(pos)[1]]=dicionario_pos[pos[0:2]][1]
            
        

class piao:
    def __init__(self,cor,inicial):
        global dicionario_pos
        self.cor=cor
        self.inicialx=scaner(inicial)[0]
        self.inicialy=scaner(inicial)[1]
        dicionario_pos[inicial]=(self,f"p{self.cor}")
        self.posicionamento(inicial)
    def posicionamento(self,posicao):
        global tabuleiro
        tabuleiro.atualiza_tabuleiro(posicao)


dicionario_pos={}

tabuleiro=tabuleiro()
piao2=piao("b","B2")
piao1=piao("b","D2")

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
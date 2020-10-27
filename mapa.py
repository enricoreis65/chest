import sys
from os import path
from scaner import *
from pecas import *
lista2=[['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '], ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '], ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '], ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '], ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '], ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '], ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']]
dicionario_pos={}

class tab:
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
            
class piao():
    def __init__(self,cor,inicial):
        global dicionario_pos
        self.cor=cor
        dicionario_pos[inicial]=(self,f"p{self.cor}")
        self.posicionamento(inicial)
    def posicionamento(self,posicao):
        global tabuleiro
        tabuleiro.atualiza_tabuleiro(posicao)
    def verifica_mov(self,pos):
        if self.cor=="b":
            if int(pos[3])==int(pos[1])+1:
                return True
            else:
                print("esse movimento é ilegal")
                return False
        if self.cor=="p":
            if int(pos[3])==int(pos[1])-1:
                return True
            else:
                print("esse movimento é ilegal")
                return False
tabuleiro=tab() 




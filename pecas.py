import sys
import numpy as np
from os import path
from scaner import *
from pecas import *
from Main import lista2

class piao:
    def __init__(self,cor,inicial):
        global dicionario_pos
        self.cor=cor
        dicionario_pos[inicial]=(self,f"p{self.cor}")
        self.posicionamento(inicial)
    def posicionamento(self,posicao):
        global tabuleiro
        tabuleiro.atualiza_tabuleiro(posicao)
    def verifica_mov(self,pos):
        if int(pos[3])==int(pos[1])+1:
            return True
        else:
            print("esse movimento é ilegal")
            return False

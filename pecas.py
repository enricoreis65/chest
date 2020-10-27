from os import path
from scaner import *
from tabuleiro import *

class piao():
    def __init__(self,cor,inicial):
        self.cor=cor
        self.inicialx=scaner(inicial)[0]
        self.inicialy=scaner(inicial)[1]
        
    def posicionamento(self,posicao):
        global tabuleiro
        tabuleiro.atualiza_tabuleiro(posicao,self)




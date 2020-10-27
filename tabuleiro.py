import sys
import numpy as np
from os import path
from scaner import *
from pecas import *
class tabuleiro:
    def __init__(self):
        self.ta=np.zeros((8,8))
        self.ta=self.ta.tolist()
    def printar_tabuleiro(self):
        print(*self.ta ,sep = "\n")
        print(*".",sep="\n")
    def atualiza_tabuleiro(pos,peca):
        self.ta[scaner(pos)[0]][scaner(pos)[1]]=0
        self.ta[scaner(pos)[2]][scaner(pos)[3]]=peca
        self.printar_tabuleiro()

tabuleiro=tabuleiro()

piao1=piao("b","D2")
piao1.posicionamento("D2")
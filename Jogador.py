# -*- coding: utf-8 -*-
"""
Trabalho Ludo - Programação Modular 2020.2
Grupo 1:
    Daniel Guimarães
    Gabriel Galvão
    Guilherme Bizzo
"""

from Peão import Peao
from Dado import Dado

class Jogador(Peao, Dado):
    
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
        
    def rodar_dado(self):
        return Dado.gera_numero()
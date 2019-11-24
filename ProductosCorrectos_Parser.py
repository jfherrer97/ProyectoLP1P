'''
PROYECTO LENGUAJES DE PROGRAMACIÓN
INTEGRANTES: JOEL ESPINOZA - CHRISTIAN GUERRERO - FABRICIO HERRERA
PARALELO 1
'''

import ply.yacc as yacc

import os
import codecs
import re
from ProductosCorrectos_Lexer import tokens
from sys import stdin

'''precedence = (
    ('right', 'ID', 'IF', 'WHILE'),
    ('right', 'VAR'),
    ('right', 'EQUALS'),
    ('left', 'LT', 'LTE', 'GT', 'GTE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'LPAREN', 'RPAREN'),
)'''

listYacc = []

def p_empty(p):
    '''empty :'''
    listYacc.append("nulo GENERAL")
    pass


def p_error(p):
    print("Error de sintaxis ", p)
    print("Error en la línea " + str(p.lineno))


def analisis_parser(entrada):
    listaYacc2 = []
    parser = yacc.yacc()
    result = parser.parse(entrada)
    listaYacc2.append(result)
    return listYacc

'''
PROYECTO LENGUAJES DE PROGRAMACIÓN
INTEGRANTES: JOEL ESPINOZA - CHRISTIAN GUERRERO - FABRICIO HERRERA
PARALELO 1
'''

import ply.lex as lex
import sys
import re
import os
import codecs

reservadas = ['INPUT', 'PRINT', 'BREAK', 'DO', 'WHILE', 'IF', 'ELSE', 'FOR', 'IN', 'RETURN', 'TRUE', 'FALSE']

tokens = ['NAME', 'PRODUCTO', 'NUMBER', 'EQUALS', 'LPAR', 'RPAR', 'COMILLA', 'COMA'] + list(reservadas.values())

t_ignore = ' \t'
t_NAME = r'[a-zA-Z_ ][a-zA-Z0-9_: ]*'
t_PRODUCTO = r'[A-Z][a-zA-Z0-9 ]*'
t_COMA = r','
t_COMILLA = r'\"'
t_NUMBER = r'[0-9]+'
t_EQUALS = '='
t_EQUAL = r'=='
t_NOTEQUAL = r'!='
t_MAYOR = r'>'
t_MENOR = r'<'
t_LPAR = r'\('
t_RPAR = r'\)'


def t_INPUT(t):
    r'input'
    t.type = reservadas.get(t.value, 'input')
    return t

def t_PRINT(t):
    r'print'
    t.type = reservadas.get(t.value, 'print')
    return t

def t_TRUE(t):
    r'True'
    t.type = reservadas.get(t.value, 'True')
    return t

def t_FALSE(t):
    r'False'
    t.type = reservadas.get(t.value, 'False')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Caracter no reconocido: '%s'" % t.value[0])
    t.lexer.skip(1)


lex.lex()

lexer = lex.lex()


def analisis_lexer(entrada):
    lista_tok = []
    lexer = lex.lex()
    lexer.input(entrada)
    while True:
        tok = lexer.token()
        if not tok: break
        lista_tok.append(tok)
    return lista_tok


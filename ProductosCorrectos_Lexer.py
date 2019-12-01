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

reservadas = ['INPUT', 'PRINT', 'ISALPHA', 'APPEND', 'WHILE', 'IF', 'ELIF', 'ELSE', 'FOR', 'IN', 'NOT']

tokens = ['EQUALS', 'PRODUCTO', 'LBRACE', 'RBRACE', 'LPAREN', 'RPAREN', "NEWLINE", "TAB", "COMMENT",
          'LBRACKET', 'RBRACKET', 'COMILLA', 'COMMA', 'LT', 'GT', 'LTE', 'GTE', 'EQUALV', 'NOTEQUALV'] + reservadas


t_VARIABLE = r'[a-z][a-zA-Z]*'
t_EQUALS = r'='
t_COMMA = r','
t_COMILLA = r'\"'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_EQUALV = r'=='
t_NOTEQUALV = r'!='

t_ignore = ' '


def t_INPUT(t):
    r'input'
    t.type = reservadas.get(t.value, 'input')
    return t


def t_PRINT(t):
    r'print'
    t.type = reservadas.get(t.value, 'print')
    return t


def t_ISALPHA(t):
    r'isalpha()'
    t.type = reservadas.get(t.value, 'isalpha()')
    return t


def t_APPEND(t):
    r'append'
    t.type = reservadas.get(t.value, 'append')
    return t


def t_WHILE(t):
    r'while'
    t.type = reservadas.get(t.value, 'while')
    return t


def t_IF(t):
    r'if'
    t.type = reservadas.get(t.value, 'if')
    return t


def t_ELIF(t):
    r'elif'
    t.type = reservadas.get(t.value, 'elif')
    return t


def t_ELSE(t):
    r'else'
    t.type = reservadas.get(t.value, 'else')
    return t


def t_FOR(t):
    r'for'
    t.type = reservadas.get(t.value, 'for')
    return t


def t_IN(t):
    r'in'
    t.type = reservadas.get(t.value, 'in')
    return t


def t_NOT(t):
    r'not'
    t.type = reservadas.get(t.value, 'not')
    return t


def t_NEWLINE(t):
    r'\n+'
    print("Newline found")
    t.lexer.lineno += len(t.value)


def t_TAB(t):
    r'\t+'
    print("Tab found")
    t.lexer.lineno += len(t.value)


def t_COMMENT(t):
    r'\#.*'
    pass
    # No return value. Token discarded


def t_error(t):
    print("Caracter no reconocido: '%s'" % t.value[0])
    t.lexer.skip(1)


analizar = lex.lex()


def analisis_lex(entrada):
    lista_tok = []
    analizar = lex.lex()
    analizar.input(entrada)
    while (True):
        tok = analizar.token()
        if not tok: break
        lista_tok.append(tok)
    return lista_tok

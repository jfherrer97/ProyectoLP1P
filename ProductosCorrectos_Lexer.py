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

reservadas = ['INPUT', 'PRINT', 'BREAK','ISALPHA','APPEND', 'DO', 'WHILE', 'IF', 'ELSE','ELSEIF', 'FOR', 'IN', 'RETURN', 'TRUE', 'FALSE']

tokens = ['ID', 'VAR', 'PLUS','DOT' ,'MINUS', 'STRING', 'COMMENT', 'TIMES', 'DIVIDE', 'NUMBER', 'PLUSPLUS', 'SEMICOLON',
          'EQUALS', 'PRODUCTO', 'EQUAL' 'NUMBER', 'LBRACE', 'RBRACE', 'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET',
          'COMILLA', 'COMMA', 'LT', 'GT', 'LTE', 'GTE', 'EQUALV', 'NOTEQUALV'] + reservadas

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_PLUSPLUS = r'\+\+'
t_INPUT = r'input'
t_FOR = r'for'
t_DOT = r'\.'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_SEMICOLON = r';'
# t_NAME = r'[a-zA-Z_ ][a-zA-Z0-9_: ]*'
t_PRODUCTO = r'[A-Z][a-zA-Z0-9 ]*'
t_COMMA = r','
t_COMILLA = r'\"'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LT = r'<'
t_GT = r'>'
t_LTE = r'<='
t_GTE = r'>='
t_EQUALV = r'=='
t_NOTEQUALV = r'!='
t_STRING = r'\"[a-zA-Z0-9]+\"'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in reservadas:
        t.value = t.value.upper()
        # reservadas.get(t.value,'ID')
        t.type = t.value
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
    print("Newline found")
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'


def t_single_line_comment(t):
    r'^//.*'
    pass


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


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

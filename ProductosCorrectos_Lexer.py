'''
PROYECTO LENGUAJES DE PROGRAMACIÓN
INTEGRANTES: JOEL ESPINOZA - CHRISTIAN GUERRERO - FABRICIO HERRERA
PARALELO 1
'''

import ply.lex as lex

lista_tok = []
list_error=[]

reservadas = ['INPUT','AND','PRINT','ISALPHA','APPEND', 'WHILE', 'IF', 'ELSE', 'FOR', 'NOT','IN','TRUE', 'FALSE']

tokens = ['ID','DOT' , 'STRING', 'COMMENT','NUMBER',
          'EQUALS', 'LBRACE', 'RBRACE', 'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET',
           'COMMA', 'LT', 'GT', 'LTE', 'GTE', 'EQUALV', 'NOTEQUALV'] + reservadas


t_INPUT = r'input'
t_FOR = r'for'
t_DOT = r'\.'
t_EQUALS = r'='
t_COMMA = r','
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
t_STRING = r'\"[a-zA-Z0-9-_ ]+\"'


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
    lista_tok.append("caracter no reconocido"+t.value[0])
    list_error.append(1)
    print("Caracter no reconocido: '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()


file = open("codigo.txt", "r")

for linea in file:
    #parser.parse(linea)
    lexer.input(linea)
    while True:
        token = lexer.token()
        if not token:
            break
        else:
            print(token)

print()

def error_lex(entrada):
    analizar = lex.lex()
    analizar.input(entrada)
    ban = 1 in list_error
    return ban

def analisis_lex(entrada):
    analizar = lex.lex()
    analizar.input(entrada)
    lista_tok.clear()
    list_error.clear()
    while (True):
        tok = analizar.token()
        if not tok: break
        lista_tok.append(tok)
    return lista_tok

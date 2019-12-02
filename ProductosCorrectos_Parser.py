'''
PROYECTO LENGUAJES DE PROGRAMACIÓN
INTEGRANTES: JOEL ESPINOZA - CHRISTIAN GUERRERO - FABRICIO HERRERA
PARALELO 1
'''

import ply.yacc as yacc
from ProductosCorrectos_Lexer import *

precedence = (
    ('right', 'ID', 'IF', 'WHILE','FOR'),
    ('right', 'EQUALS'),
    ('left', 'LT', 'LTE', 'GT', 'GTE'),
    ('left', 'LPAREN', 'RPAREN'),
)
listYacc = []
errorParser=[]


def p_programa(p):
    '''program : block'''
    print("Programa")
    listYacc.append("programa")

def p_block(p):
    '''block :  statementList'''
    print("Bloque de codigo")
    listYacc.append("bloque de codigo")


def p_elements(t):
    '''
    elements : expression
            | expression COMMA elements
    '''


def p_print(p):
    'statement : PRINT LPAREN STRING RPAREN '
    listYacc.append("Print Simple")

def p_print_expressioin(p):
    'statement : PRINT LPAREN expression RPAREN '
    listYacc.append("Print Expression")

def p_statement_assign_print(p):
        '''statement :  PRINT LPAREN expression COMMA STRING COMMA expression RPAREN'''
        print(p[3], p[5], p[7])

def p_statement_Append(t):
    '''statement : ID DOT APPEND LPAREN expression RPAREN'''
    print("function apppend")
    listYacc.append("function append")

def p_statementPrincipal(p):
    '''statement : ID EQUALS expression'''
    print("statement Principal")
    listYacc.append("Statement ID = EXPRESSION")


def p_statementIFPrinciapl(p):
    '''statement : IF condition LBRACE statementList RBRACE  statementIF '''
    print("statement If principal")
    listYacc.append("Statement IFPrincipal")


def p_statementWhile(p):
    '''statement : WHILE condition LBRACE statementList RBRACE '''
    print("statement WHIlE")
    listYacc.append("Statement WHILE")

def p_statementFor(p):
    '''statement : FOR ID IN ID LBRACE statementList RBRACE'''
    print("statement 5 FOR IN")
    listYacc.append("Statement FOR IN")


def p_statementEmpty(p):
    '''statement : empty'''
    print("nulo")
    listYacc.append("Nulo Statement")


def p_statementElse(p):
    '''statementIF : ELSE LBRACE statementList RBRACE'''
    print("Statement ELSE Secundario")
    listYacc.append("Statement ELSE")


def p_statementElseIF(p):
    '''statementIF : ELSE IF condition LBRACE statementList RBRACE statementIF'''
    print("Statement Else If")
    listYacc.append("Statement Else If")


def p_statementIFEmpty(p):
    '''statementIF : empty'''
    print("Nulo Statement if")
    listYacc.append("Nulo Statement if")


def p_statementListMultiple(p):
    '''statementList : statement
                    | statement statementList'''
    print("statementList Multiple")
    listYacc.append("Statement Multiple")



def p_conditionPrinciapl(p):
    '''condition : expression relation expression
                    | expression relation expression relation expression relation expression '''
    print("condicion Principal")
    listYacc.append("condition principla")

def p_relationAND(p):
    '''relation : AND'''
    print("Realacion AND")
    listYacc.append("AND")

def p_relationEQUAL(p):
    '''relation : EQUALV'''
    print("Relacion Equal")
    listYacc.append("EQUAL")

def p_relationNotEqula(p):
    '''relation : NOTEQUALV'''
    print("Relacion NotEqual")
    listYacc.append("NotEqual")

def p_relationLessThan(p):
    '''relation : LT'''
    print("Relacion Less than")
    listYacc.append("Less Than")


def p_relationGreaterThan(p):
    '''relation : GT'''
    print("relacion Greater than")
    listYacc.append("Greater than")


def p_relationLessThanEquals(p):
    '''relation : LTE'''
    print("Relacion Less than equal")
    listYacc.append("LTE")


def p_relationGreaterThanEqual(p):
    '''relation : GTE'''
    print("Relacion Greater Than Eqaul")
    listYacc.append("Greater than equal")

def p_relationNotIN(p):
    '''relation : NOT IN'''
    print("relacion NOT IN")
    listYacc.append("Not in")

def p_expressionType(p):
    '''expression : term'''
    print("expresion type")
    listYacc.append("expresion type")


def p_expresion_isAlpha(t):
    '''factor : ID DOT ISALPHA LPAREN RPAREN'''
    print("function isAlpha()")
    listYacc.append("isAlpha")

def p_termPrincipal(p):
    '''term : factor'''
    print("termPrincipal")
    listYacc.append("term")


def p_factorID(p):
    '''factor : ID'''
    print("factor ID")
    listYacc.append("factor 1D")


def p_factorString(p):
    '''factor : STRING'''
    print("factor String")
    listYacc.append("factor string")

def p_factorListStruc(p):
    '''factor : LBRACKET elements RBRACKET
                | LBRACKET  RBRACKET'''
    print("factor List Struct")
    listYacc.append("factor List Struct")

def p_factorInput(p):
    '''factor : INPUT LPAREN STRING RPAREN  '''
    print("factor Input")
    listYacc.append("factor Input")

def p_factorNumber(p):
    '''factor : NUMBER'''
    print("factor Number")
    listYacc.append("factor Number")

def p_factor_Bool_False(p):
    '''factor : FALSE'''
    print("boolean FALSE")
    listYacc.append("factor boolean FALSE")

def p_factor_Bool_True(p):
    '''factor : TRUE'''
    print("boolean TRUE")
    listYacc.append("factor boolean TRUE")


def p_empty(p):
    '''empty :'''
    listYacc.append("nulo")
    pass


def p_error(p):
    print("Error de sintaxis ", p)
    listYacc.append("Error de sintaxis: "+str(p))
    errorParser.append(1)

def error_Parser(entrada):
    parser = yacc.yacc()
    parser.parse(entrada)
    ban = 1 in errorParser
    return ban

def analisis_sem(entrada):
    listaYacc2 = []
    parser = yacc.yacc()
    listYacc.clear()
    errorParser.clear()
    result = parser.parse(entrada)
    listaYacc2.append(result)
    return listYacc


parser = yacc.yacc()
file = open("codigo.txt", "r")
result = parser.parse(file.read())


'''
PROYECTO LENGUAJES DE PROGRAMACIÓN
INTEGRANTES: JOEL ESPINOZA - CHRISTIAN GUERRERO - FABRICIO HERRERA
PARALELO 1
'''

import ply.yacc as yacc
import os
import codecs
import re
from ProductosCorrectos_Lexer import *
from sys import stdin

'''precedence = (
    ('right', 'ID', 'IF', 'WHILE','FOR'),
    ('right', 'VAR'),
    ('right', 'EQUALS'),
    ('left', 'LT', 'LTE', 'GT', 'GTE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'LPAREN', 'RPAREN'),
)'''

# Prioridades
precedence = (
    ('right', 'ID', 'IF', 'WHILE','FOR'),
    ('right', 'VAR'),
    ('right', 'EQUALS'),
    ('left', 'LT', 'LTE', 'GT', 'GTE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'LPAREN', 'RPAREN'),
)
# GENERALES
listYacc = []


def p_program(p):
    '''program : block'''
    print("program")
    listYacc.append("program")

def p_block(p):
    '''block :  statementList'''
    # p[0] = block(p[1],p[2],p[3],p[4],"block")
    print("block")


def p_elements(t):
    '''
    elements : expression
            | expression COMMA elements
    '''


def p_print(p):
        'statement : PRINT LPAREN STRING RPAREN '
        print(p[3])


def p_print_expressioin(p):
    'statement : PRINT LPAREN expression RPAREN '
    print(p[3])

def p_statement_assign_print(p):
        '''statement :  PRINT LPAREN expression COMMA STRING COMMA expression RPAREN'''
        print(p[3], p[5], p[7])

def p_statement_Append(t):
    '''statement : ID DOT APPEND LPAREN expression RPAREN'''
    print("function apppend")
    listYacc.append("function append")

def p_statement1(p):
    '''statement : ID EQUALS expression'''
    # p[0] = statement1(Id(p[1]),Update(p[2]),p[3],"statement1")
    print("statement 1")
    listYacc.append("Statement ID = EXPRESSION")


def p_statement2(p):
    '''statement : IF condition LBRACE statementList RBRACE  statementIF '''
    # p[0] = statement4(p[2],p[4],"statement4")
    print("statement 2")
    listYacc.append("Statement IF")


def p_statement3(p):
    '''statement : WHILE condition LBRACE statementList RBRACE '''
    # p[0] = statement5(p[2],p[4],"statement5")
    print("statement 3 WHIlE")
    listYacc.append("Statement WHILE")

def p_statement5(p):
    '''statement : FOR ID IN ID LBRACE statementList RBRACE'''
    # p[0] = statement5(p[2],p[4],"statement5")
    print("statement 5 FOR IN")
    listYacc.append("Statement FOR IN")


def p_statementEmpty(p):
    '''statement : empty'''
    # p[0] = Null()
    print("nulo")
    listYacc.append("Nulo Statement")


def p_statementIF1(p):
    '''statementIF : ELSE LBRACE statementList RBRACE'''
    print("Statement if1")
    listYacc.append("Statement if1")


def p_statementIF2(p):
    '''statementIF : ELSE IF condition LBRACE statementList RBRACE statementIF'''
    print("Statement if2 else")
    listYacc.append("Statement if2")


def p_statementIFEmpty(p):
    '''statementIF : empty'''
    print("Nulo Statement if")
    listYacc.append("Nulo Statement if")


def p_statementList1(p):
    '''statementList : statement
                    | statement statementList'''
    # p[0] = statementList1(p[1],"statementList1")
    print("statementList 1")
    listYacc.append("StatementList 1")



def p_condition1(p):
    '''condition : expression relation expression
                    | expression relation expression relation expression relation expression '''
    # p[0] = condition2(p[1],p[2],p[3],"condition2")
    print("condition 1")
    listYacc.append("condition 1")

def p_relationAND(p):
    '''relation : AND'''
    # p[0] = relation1(Assign(p[1]),"relation1")
    print("relation AND")
    listYacc.append("relation AND")
def p_relation1(p):
    '''relation : EQUALV'''
    # p[0] = relation1(Assign(p[1]),"relation1")
    print("relation 1")
    listYacc.append("relation 1")

def p_relationNotEqula(p):
    '''relation : NOTEQUALV'''
    # p[0] = relation1(Assign(p[1]),"relation1")
    print("relation NotEqual")
    listYacc.append("relation 1")

def p_relation2(p):
    '''relation : LT'''
    # p[0] = relation3(LT(p[1]),"relation3")
    print("relation 2")
    listYacc.append("relation 2")


def p_relation3(p):
    '''relation : GT'''
    # p[0] = relation4(GT(p[1]),"relation4")
    print("relation 3")
    listYacc.append("relation 3")


def p_relation4(p):
    '''relation : LTE'''
    # p[0] = relation5(LTE(p[1]),"relation5")
    print("relation 4")
    listYacc.append("relation 4")


def p_relation5(p):
    '''relation : GTE'''
    # p[0] = relation6(GTE(p[1]),"relation6")
    print("relation 5")
    listYacc.append("relation 5")

def p_relationNotIN(p):
    '''relation : NOT IN'''
    # p[0] = relation6(GTE(p[1]),"relation6")
    print("relation NOT IN")
    listYacc.append("relation Not in")

def p_expression1(p):
    '''expression : term'''
    # p[0] = expression1(p[1],"expression1")
    print("expresion 1")
    listYacc.append("expresion 1")


def p_expresion_isAlpha(t):
    '''factor : ID DOT ISALPHA LPAREN RPAREN'''
    print("function isAlpha()")
    listYacc.append("isAlpha")


def p_expression2(p):
    '''expression : addingOperator term'''
    # p[0] = expression2(p[1],p[2],"expression2")
    print("expresion 2")
    listYacc.append("expresion 2")


def p_expression3(p):
    '''expression : expression addingOperator term'''
    # p[0] = expression3(p[1],p[2],p[3],"expression3")
    print("expresion 3")
    listYacc.append("expresion 3")


def p_addingOperator1(p):
    '''addingOperator : PLUS'''
    # p[0] = addingOperator1(Plus(p[1]),"addingOperator")
    print("addingOperator 1")
    listYacc.append("addingOperator 1")


def p_addingOperator2(p):
    '''addingOperator : MINUS'''
    # p[0] = addingOperator2(Minus(p[1]),"subtractionOperator")
    print("addingOperator 2")
    listYacc.append("addingOperator 2")

def p_term1(p):
    '''term : factor'''
    # p[0] = term1(p[1],"term1")
    print("term 1")
    listYacc.append("term 1")


def p_term2(p):
    '''term : term multiplyingOperator factor'''
    # p[0] = term2(p[1],p[2],p[3],"term2")
    print("term 2")
    listYacc.append("term 2")


def p_multiplyingOperator1(p):
    '''multiplyingOperator : TIMES'''
    # p[0] = multiplyingOperator1(Times(p[1]),"multiplyingOperator")
    print("multiplyingOperator 1")
    listYacc.append("multiplyingOperator 1")


def p_multiplyingOperator2(p):
    '''multiplyingOperator : DIVIDE'''
    # p[0] = multiplyingOperator2(Divide(p[1]),"divisiongOperator")
    print("multiplyingOperator 2")
    listYacc.append("multiplyingOperator 2")


def p_factor1(p):
    '''factor : ID'''
    # p[0] = factor1(Id(p[1]),"factor1")
    print("factor 1")
    listYacc.append("factor 1")


def p_factor0(p):
    '''factor : STRING'''
    # p[0] = factor1(Id(p[1]),"factor1")
    print("factor 0 String")
    listYacc.append("factor 0")
def p_factor0ListStruc(p):
    '''factor : LBRACKET elements RBRACKET
                | LBRACKET  RBRACKET'''
    # p[0] = factor1(Id(p[1]),"factor1")
    print("factor List Struct")
    listYacc.append("factor 0")
def p_factorInput(p):
    '''factor : INPUT LPAREN STRING RPAREN  '''
    # p[0] = factor1(Id(p[1]),"factor1")
    print("factor Input")
    listYacc.append("factor Input")
def p_factor2(p):
    '''factor : NUMBER'''
    # p[0] = factor2(Number(p[1]),"factor2")
    print("factor 2")
    listYacc.append("factor 2")
def p_factor_Bool_False(p):
    '''factor : FALSE'''
    # p[0] = factor2(Number(p[1]),"factor2")
    print("boolean FALSE")
    listYacc.append("factor boolean FALSE")
def p_factor_Bool_True(p):
    '''factor : TRUE'''
    # p[0] = factor2(Number(p[1]),"factor2")
    print("boolean TRUE")
    listYacc.append("factor boolean TRUE")

def p_factor3(p):
    '''factor : LPAREN expression RPAREN'''
    # p[0] = factor3(p[2],"factor3")
    print("factor 3")
    listYacc.append("factor 3")


def p_empty(p):
    '''empty :'''
    listYacc.append("nulo GENERAL")
    pass


def p_error(p):
    print("Error de sintaxis ", p)
    print("Error en la linea " + str(p.lineno))


def analisis_sem(entrada):
    listaYacc2 = []
    parser = yacc.yacc()
    result = parser.parse(entrada)
    listaYacc2.append(result)
    return listYacc


#entrada = input("Introduce una cadena: ")
parser = yacc.yacc()
file = open("codigo.txt", "r")
print("***Challenge Complete***")
#print(file.read())
result = parser.parse(file.read())
print(result)
#lexer.input(file.read())



"""
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

"""

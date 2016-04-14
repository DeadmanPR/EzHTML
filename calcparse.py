# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 22:27:05 2016

@author: emmanuelramos
"""

import ply.yacc as yacc 

from calclex import tokens

def p_start(p):
    '''start : EZHTML_START '{' title '}' '''
    p[0] = p[3]
    
def p_title(p):
    '''title : TITLE EQ value; program'''
    p[0] = (p[3], p[4])

def p_program(p):
    '''program : body '{'  statement_list '}' '''
    p[0] = p[3]

def p_statement_list(p):
    '''statement_list : statement
                        | statement ';' statement_list'''
    if len(p) > 2:
        p[0] = (p[1], p[3])
    else:
        p[0] = p[1]

#TODO
def p_statement(p):
    '''statement : assignment
                    | attr LP  ID RP LB statement_list RB '''
    p[0] = [1]
    if len(p)>2:
        p[3] = p[6]
#TODO
    
def p_assignment(p):
    '''assignment : TYPE ID '=' value
                    | attrtype '=' value
                    | styleattr '=' CONSTANTVALUE'''
    p[1] = p[3]
    if len(p)>4:
        p[2] = p[4]


def p_value(p):
    '''value : STRINGVALUE | NUMERICVALUE '''
    p[0] = p[1]

def p_attr(p):
    '''attr : STYLE | LINKATTR | IMAGEATTR'''
    p[0] = p[1]

def p_attrtype(p):
    '''attrtype : DESTINATION | WIDTH | HEIGHT | SOURCE | TEXT'''
    p[0] = p[1]

def p_styleattrtype(p):
    '''styleattrtype : COLOR | ALIGNMENT | FONT | BOLD | UNDERLINE | ITALIC'''
    p[0] = p[1]
    
    
    
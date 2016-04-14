# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 22:27:05 2016

@author: emmanuelramos
"""

from Interpreter import *

import ply.yacc as yacc 

import myLex
tokens = myLex.tokens



def p_start(p):
    '''start : title LB program RB SEMICOLON'''
 #   p[0] = (p[6])
    

def p_title(p):
    '''title : TITLE EQ STRINGVALUE SEMICOLON'''
    p[0] = p[3]
    unquotedTitle = p[3]
    unquotedTitle = unquotedTitle[1:len(unquotedTitle)-1]
    initialize(unquotedTitle)
    
def p_program(p):
    '''program : BODY LB  statement_list RB SEMICOLON '''
    p[0] = p[3]
    
#TODO: Fix Syntax Error at line ##, token = ????

def p_statement_list(p):
    '''statement_list : statement SEMICOLON
                        | statement SEMICOLON statement_list'''
    if len(p) > 2:
        p[0] = (p[1], p[3])
    else:
        p[0] = p[1]
        
#TODO
def p_statement(p):
    '''statement : assignment
                    | attr LP  ID RP LB statement_list RB'''
    p[0] = p[1]
    if len(p)>2:
        p[3] = p[6]
#TODO
    
def p_assignment(p):
    '''assignment : type ID EQ value
                    | attrtype EQ value
                    | styleattrtype EQ CONSTANTVALUE'''
    p[1] = p[3]
    if len(p)>4:
        p[2] = p[4]
    
    print type
    if type in [H1, H2, H3, H4, H5, H6]:
        writeHeader(ID, int(type[1]), value)
        
def p_type(p):
    ''' type : H1
                    | H2
                    | H3
                    | H4
                    | H5 
                    | H6
                    | PARAGRAPH
                    | LINK
                    | IMAGE'''
    p[0] = p[1]
        
def p_value(p):
    '''value : STRINGVALUE 
                     | NUMERICVALUE '''
    p[0] = p[1]

def p_attr(p):
    '''attr : STYLE 
                | LINKATTR 
                | IMAGEATTR'''
    p[0] = p[1]

def p_attrtype(p):
    '''attrtype : DESTINATION 
                            | WIDTH 
                            | HEIGHT 
                            | SOURCE 
                            | TEXT'''
    p[0] = p[1]

def p_styleattrtype(p):
    '''styleattrtype : COLOR
                                     | ALIGNMENT 
                                     | FONT 
                                     | BOLD 
                                     | UNDERLINE 
                                     | ITALIC'''
    p[0] = p[1]
    
#Test
testData = 'TITLE = "My Website";\nbody{paragraph p1 = "Test";\n};'
    

y = yacc.yacc()
result = y.parse(testData)
print result
 


    
import ply.lex as lex

#List of token names
tokens = ('EQ', 'LP', 'RP', 'LB', 'RB', 'SEMICOLON', 'TITLE', 'BODY', 
          'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'STYLE', 'COLOR', 'ALIGNMENT',
          'FONT', 'PARAGRAPH', 'BOLD', 'ITALIC', 'UNDERLINE', 'LINK', 'IMAGE',
          'ID', 'STRINGVALUE', 'CONSTANTVALUE', 'NUMERICVALUE',
          'COMMENT', 'LINKATTR', 'IMAGEATTR', 'DESTINATION', 'WIDTH', 'HEIGHT',
          'SOURCE', 'TEXT')
          

#Regular Expressions for some tokens
t_EQ = r'\='
t_LP = r'\('
t_RP = r'\)'
t_LB = r'\{'
t_RB = r'\}'
t_SEMICOLON = r'\;'
t_ID = r'[a-z]([A-Za-z]|[0-9]+)*'
t_STRINGVALUE = r'(["]([^,\n\t]+)["])'
t_CONSTANTVALUE = r'[A-Z]{2,}'
t_NUMERICVALUE = r'[0-9]+'
t_COMMENT = r'\/{2}(.)+(\n)|\/\*(.)+\\*\/'

#============================================================
#                                Definitions for the rest of the tokens
#============================================================
def t_TITLE(t):
    r'TITLE'
    t.value = 'TITLE'
    return t

def t_BODY(t):
    r'body'
    t.value = 'body'
    return t

def t_H1(t):
    r'heading1'
    t.value = 'heading1'
    return t

def t_H2(t):
    r'heading2'
    t.value = 'heading2'
    return t

def t_H3(t):
    r'heading3'
    t.value = 'heading3'
    return t

def t_H4(t):
    r'heading4'
    t.value = 'heading4'
    return t

def t_H5(t):
    r'heading5'
    t.value = 'heading5'
    return t

def t_H6(t):
    r'heading6'
    t.value = 'heading6'
    return t

def t_STYLE(t):
    r'style'
    t.value = 'style'
    return t

def t_COLOR(t):
    r'color'
    t.value = 'color'
    return t

def t_ALIGNMENT(t):
    r'alignment'
    t.value = 'alignment'
    return t

def t_FONT(t):
    r'font'
    t.value = 'font'
    return t

def t_PARAGRAPH(t):
    r'paragraph'
    t.value = 'paragraph'
    return t

def t_BOLD(t):
    r'isBold'
    t.value = 'isBold'
    return t

def t_ITALIC(t):
    r'isItalic'
    t.value = 'isItalic'
    return t

def t_UNDERLINE(t):
    r'isUnderline'
    t.value = 'isUnderline'
    return t

def t_LINKATTR(t):
    r'linkAttr'
    t.value = 'linkAttr'
    return t

def t_IMAGEATTR(t):
    r'imageAttr'
    t.value = 'imageAttr'
    return t
def t_LINK(t):
    r'link'
    t.value = 'link'
    return t

def t_IMAGE(t):
    r'image'
    t.value = 'image'
    return t

def t_DESTINATION(t):
    r'destination'
    t.value = 'destination'
    return t

def t_WIDTH(t):
    r'width'
    t.value = 'width'
    return t

def t_TEXT(t):
    r'text'
    t.value ='text'
    return t

def t_SOURCE(t):
    r'source'
    t.value = 'source'
    return t

def t_HEIGHT(t):
    r'height'
    t.value = 'height'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


#====================================================

#Ignored tokens/characters
t_ignore  = ' \t,'


#Defines error behavior
def t_error(t):
    print("Illegal character '%s'" % t.value[0])

    t.lexer.skip(1)

#Initialize Lex
lexer = lex.lex()

#Try to open the "input.in" file
try:
    input = open('input.in', 'r')
except FileNotFoundException:
    print 'File "input.in" not found!'
    
#Open the output file
output = open('output.out', 'w')

#Pass the contents of the input file to the scanner
lexer.input(input.read())

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    output.write(tok.type + '(' + tok.value + ')\n')
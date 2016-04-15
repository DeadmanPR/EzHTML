__author__ = "Jose Antonio Rodriguez Rivera"
import ply.yacc as yacc 

import myLex
tokens = myLex.tokens

#=======================================================================
#                                                                    Grammar Rules
#=======================================================================
def p_start(p):
    '''start : title'''
    p[0] = p[1]
    finalize()
    return

def p_title(p):
    '''title : TITLE EQ STRINGVALUE SEMICOLON body'''
    p[0] = p[5]
    initialize(unquoteString(p[3]))
    return

def p_body(p):
    '''body : BODY LB statement_list RB SEMICOLON'''
    p[0] = p[3]
    return

def p_statement_list(p):
    '''statement_list : statement 
                                        | statement statement_list
                                        | BACKGROUND_COLOR EQ CONSTANTVALUE SEMICOLON statement_list'''
    if len(p) is 3:
        p[0] = p[2]
    elif len(p) is 6:
        setBGColor(p[3])
    else:
        p[0] = p[1]
    return
 
def p_statement(p):
     '''statement : type_assignment
                                 | attr_definition
                                 | link_definition
                                 | image_definition'''
     p[0] = p[1]
     return
 
def p_type_assignment(p):
     '''type_assignment : type ID EQ STRINGVALUE SEMICOLON'''
     if p[1] in ['heading1', 'heading2', 'heading3', 'heading4', 'heading5', 'heading6']:
         writeHeader(p[2], int(p[1][7]), unquoteString(p[4]))
     else:
        writeParagraph(p[2], unquoteString(p[4]))
     return
 
def p_type(p):
   '''type : H1
                | H2
                | H3
                | H4
                | H5
                | H6
                | PARAGRAPH'''
   p[0] = p[1]
   return
            
def p_attr_definition(p):
    '''attr_definition : STYLE LP ID RP LB COLOR EQ CONSTANTVALUE SEMICOLON ALIGNMENT EQ CONSTANTVALUE SEMICOLON FONT EQ CONSTANTVALUE SEMICOLON FONTSIZE EQ NUMERICVALUE SEMICOLON BOLD EQ CONSTANTVALUE SEMICOLON ITALIC EQ CONSTANTVALUE SEMICOLON UNDERLINE EQ CONSTANTVALUE SEMICOLON RB SEMICOLON'''
    setColor(p[3], p[8])
    setAlignment(p[3], p[12]) 
    setFont(p[3], p[16])
    setFontSize(p[3], p[20])
    setBold(p[3], p[24])
    setItalic(p[3], p[28])
    setUnderline(p[3], p[32]) 
    return


def p_link_definition(p):
    '''link_definition : LINK ID SEMICOLON LINKATTR LP ID RP LB DESTINATION EQ STRINGVALUE SEMICOLON TEXT EQ STRINGVALUE SEMICOLON ALIGNMENT EQ CONSTANTVALUE SEMICOLON FONTSIZE EQ NUMERICVALUE SEMICOLON RB SEMICOLON'''
    if p[2] == p[6]:
        writeHyperlink(p[2], unquoteString(p[11]), unquoteString(p[15]))
        setAlignment(p[2], p[19])
        setFontSize(p[2], p[23])
    else:
        print 'IDs must match in link attributes definition!'
        raise Exception
    return

def p_image_definition_error(p):
    '''image_definition : IMAGE ID SEMICOLON IMAGEATTR LP ID RP LB SOURCE EQ STRINGVALUE SEMICOLON HEIGHT EQ NUMERICVALUE SEMICOLON WIDTH EQ NUMERICVALUE SEMICOLON DESTINATION EQ STRINGVALUE SEMICOLON RB SEMICOLON'''
    if p[2] == p[6]:
        writeImage(p[2], unquoteString(p[11]), p[15], p[19], unquoteString(p[23]))
    else:
        print 'IDs must match in image attributes definition!'
        raise Exception
    return 

 #=============================================================================================
 #                                                                                                   INTERMEDIATE CODE 
 #=============================================================================================
from Element import *
import os
import webbrowser

elements = [];

f = open('MyWebpage.html', 'w')
styles = open ('MyWebpage.css', 'w')

def initialize(webpageTitle):    
    global title
    title  = webpageTitle
    os.rename('MyWebpage.html', webpageTitle + '.html')
    os.rename('MyWebpage.css', webpageTitle + '.css')

    f.write('<!DOCTYPE html>\n')
    f.write('<head>\n')
    f.write('\t<title>' + webpageTitle + '</title>\n')
    f.write('\t<link rel="stylesheet" href="' + webpageTitle + '.css">\n')
    f.write('</head>\n')

    f.write('\n<body>\n')
    return;

def searchElement(identifier):
    for e in elements:
      
        if e.getID() == identifier:
            return e

    print 'Error: Element with identifier = ' + identifier + ' does not exist!\n'
    raise Exception

  
def setBGColor(backgroundColor):
    if backgroundColor is not None:
        styles.write('body{\n\tbackground-color: ' + backgroundColor + ';\n}\n\n')
    return
          
def writeHeader(identifier, number, text):
    if number < 1 or number > 6:
        raise ValueError('Invalid header number: ' + str(number) + '\n')

    f.write('\t<h' + str(number) + ' id="' + identifier + '">' + text + '</h' + str(number) + '>\n')
    elements.append(Element(identifier, 'heading' + str(number), text))
    return

def writeParagraph(identifier, text):
    f.write('\t<p id="' + identifier + '">' + text + '</p>\n')
    elements.append(Element(identifier, 'paragraph', text))
    return 

def writeHyperlink(identifier, link, text):
    if identifier is None:
        f.write('\t<a href="' + link + '";>' + text + '</a>\n')
    else:
        f.write('\t<a id="' + identifier + '" href="' + link + '";>' + text + '</a>\n')
    elements.append(Element(identifier, 'hyperlink', text))
    return

def writeImage(identifier, source, height, width, link):
    if link is None:
        f.write('\t<img id="' + identifier + '" src="' + source + '" height = "' + height + '" width = "' + width + '"/>\n')
        elements.append(Element(identifier, 'image', None))
    else:
        writeHyperlink(identifier, link, '<img id="' + identifier + '" src="' + source + '" height = "' + height + '" width = "' + width + '"/>')
    return

def  setColor(identifier, color):
    elm = searchElement(identifier)
    elm.setColor(color)
    return

def  setAlignment(identifier, alignment):
    elm = searchElement(identifier)
    elm.setAlignment(alignment)
    return

def  setFont(identifier, font):
    elm = searchElement(identifier)
    elm.setFont(font)
    return

def setFontSize(identifier, fontSize):
    elm = searchElement(identifier)
    elm.setFontSize(fontSize)
    return

def  setBold(identifier, isBold):
    elm = searchElement(identifier)
    elm.setBold(isBold)
    return

def  setItalic(identifier, isItalic):
    elm = searchElement(identifier)
    elm.setItalic(isItalic)
    return

def  setUnderline(identifier, isUnderline):
    elm = searchElement(identifier)
    elm.setUnderline(isUnderline)
    return

def unquoteString(stringValue):
    return stringValue[1:len(stringValue) - 1]

def finalize():
    f.write('</body>\n')
    f.write('</html>')
    
    for e in elements:
        styles.write('#' + e.getID() + '{\n')
        if e.getColor() is not '':
            styles.write('\tcolor: ' + e.getColor() + ';\n')
        if e.getAlignment() is not '':
            if e.getType() == 'image':
                styles.write('\talign: ' + e.getAlignment() + ';\n')
            else:
                styles.write('\tdisplay: block;\n')
                styles.write('\ttext-align: ' + e.getAlignment() + ';\n')
        if e.getFont() is not '':
            styles.write('\tfont: ' + e.getFont() + ';\n')
        if e.getFontSize() is not 0:
            styles.write('\tfont-size: ' + str(e.getFontSize()) + 'px;\n')
        if e.getBold() == 'TRUE':
            styles.write('\tfont-weight: bold;\n')
        if e.getItalic() == 'TRUE':
            styles.write('\tfont-style: italic;\n')
        if e.getUnderline() == 'TRUE':
            styles.write('\ttext-decoration: underline;\n')
        styles.write('}\n\n')
        
    styles.close()

    f.close()
    
    #Opens the website in the web browser
    webbrowser.open(title + '.html')
    return

#=================================================
#=================================================

# Test
print '================EzHTML===============' 
try:
    sourceCodeName = raw_input('Please enter the name of the source code file: ')
except NameError:
    print 'The file name you entered does not exist!'
    exit()
sourceCode = open(sourceCodeName, 'r')
testData = sourceCode.read()
    
y = yacc.yacc()
result = y.parse(testData)

 


    

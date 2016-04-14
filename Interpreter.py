#This program reads the syntax of our created language, and converts it to HTML code
from Element import *

title = '';
elements = [];

def initialize(webpageTitle):
    title = webpageTitle
    global f, styles;
    f= open(title + '.html', 'w')
    styles = open(title + '.css', 'w')
    
    f.write('<!DOCTYPE html>\n')
    f.write('<head>\n')
    f.write('\t<title>' + title + '</title>\n')
    f.write('\t<link rel="stylesheet" href="' + title + '.css">\n')
    f.write('</head>\n')

    f.write('\n<body>\n')
    return;

def searchElement(identifier):
    for e in elements:
        if e.getID() is identifier:
            return e

    return None
        
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

def writeImage(identifier, source, link):
    if link is None:
        f.write('\t<img id="' + identifier + '" src="' + source + '"/>\n')
    else:
        writeHyperlink(None, link, '<img id="' + identifier + '" src="' + source + '"/>')
    elements.append(Element(identifier, 'image', None))
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

def finalize():
    f.write('</body>\n')
    f.write('</html>')

    f.close();
    
    for e in elements:
        styles.write('#' + e.getID() + '{\n\t')
        styles.write('color: ' + e.getColor() + ';\n')
        styles.write('text-align: ' + e.getAlignment() + ';\n')
        styles.write('font: ' + e.getFont() + ';\n') #TODO: Fix
        if e.getBold() is True:
            styles.write('font-weight: bold;\n')
        if e.getItalic() is True:
            styles.write('font-style: italic;\n')
        if e.getUnderline() is True:
            styles.write('text-decoration: underline;\n')
        styles.write('}\n\n')
        
    styles.close()
    return





#This program reads the syntax of our created language, and converts it to HTML code
from Element import Element
from CSSEditor import CSSEditor


f= open('MyWebsite.html', 'w')
styles = open('MyWebsite.css', 'w')
elements = [""];


def writeHeader(identifier, number, text):
    if number < 1 or number > 6:
        raise ValueError('Invalid header number: ' + str(number) + '\n')

    f.write('\t<h' + str(number) + ' id="' + identifier + '">' + text + '</h' + str(number) + '>\n')
    elements.append(Element(identifier, 'header' + str(number), text))
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
        elements.append(Element(identifier, 'image', None))
    else:
        writeHyperlink(None, link, '<img id="' + identifier + '" src="' + source + '"/>')
        elements.append(Element(identifier, 'image', None))
    return

f.write('<!DOCTYPE html>\n')
f.write('<head>\n')
f.write('\t<title>My Website</title>\n')
f.write('\t<link rel="stylesheet" href="MyWebsite.css">\n')
f.write('</head>\n')

f.write('\n<body>\n')

f.write('</body>\n')
f.write('</html>')

f.close();
styles.close()

editor = CSSEditor(elements[1:])




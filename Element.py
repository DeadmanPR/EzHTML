__author__ = "Jose Antonio Rodriguez Rivera"
#This class is responsible of storing the parameters of 
#each element of the program.
class Element():
	__id=""
	__type=""
	__text=""
	__color=""
	__alignment=""
	__font=""
	__fontSize = 0
	__isBold=""
	__isItalic=""
	__isUnderline=""
	
	#Method for initializing an element by adding the ID, 
	#type of element and text.
	def __init__(self, id, type, text):
		self.__id = id
		self.__type = type
		if text is not None:
			self.__text = text
		return;
	
	#Method for giving a printable representation of the element.
	def __repr__(self):
		return ('id = ' + self.__id + ' | type = ' + self.__type + ' | text = ' + self.__text[:30])

	#Method for setting the color parameter of the element.
	def setColor(self, color):
		self.__color = color;
		return
	
	#Method for setting the aligNment parameter of the element.
	def setAlignment(self, alignment):
		self.__alignment = alignment;
		return
	
	#Method for setting the Font parameter of the element.
	def setFont(self, font):
		self.__font = font;
		return
	
	#Method for setting the Font size parameter of the element.
	def setFontSize(self, fontSize):
		self.__fontSize = fontSize;
		return 
	
	#Method for setting the Bold parameter of the element.
	def setBold(self, isBold):
		self.__isBold = isBold;
		return
	
	#Method for setting the Italic parameter of the element.
	def setItalic(self, isItalic):
		self.__isItalic = isItalic;
		return
	
	#Method for setting the Underline parameter of the element.
	def setUnderline(self, isUnderline):
		self.__isUnderline = isUnderline;
		return
	
	#This method returns the ID parameter of the element
	def getID(self):
		return self. __id
	
	#This method returns the Type parameter of the element
	def getType(self):
		return self.__type
	
	#This method returns the Text parameter of the element
	def getText(self):
		return self.__text
	
	#This method returns the color parameter of the element
	def getColor(self):
		return self.__color
	
	#This method returns the Alignment parameter of the element
	def getAlignment(self):
		return self.__alignment
	
	#This method returns the Font parameter of the element
	def getFont(self):
		return self.__font
	
	#This method returns the Font size parameter of the element
	def getFontSize(self):
		return self.__fontSize
	
	#This method returns the Bold parameter of the element
	def getBold(self):
		return self.__isBold
	
	#This method returns the Italic parameter of the element
	def getItalic(self):
		return self.__isItalic
	
	#This method returns the Underline parameter of the element
	def getUnderline(self):
		return self.__isUnderline
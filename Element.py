__author__ = "Jose Antonio Rodriguez Rivera"
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
	
	def __init__(self, id, type, text):
		self.__id = id
		self.__type = type
		if text is not None:
			self.__text = text
		return;
	
	def __repr__(self):
		return ('id = ' + self.__id + ' | type = ' + self.__type + ' | text = ' + self.__text[:30])

	def setColor(self, color):
		self.__color = color;
		return
	
	def setAlignment(self, alignment):
		self.__alignment = alignment;
		return
	
	def setFont(self, font):
		self.__font = font;
		return
	
	def setFontSize(self, fontSize):
		self.__fontSize = fontSize;
		return 
	
	def setBold(self, isBold):
		self.__isBold = isBold;
		return
	
	def setItalic(self, isItalic):
		self.__isItalic = isItalic;
		return
	
	def setUnderline(self, isUnderline):
		self.__isUnderline = isUnderline;
		return
	
	def getID(self):
		return self. __id
	
	def getType(self):
		return self.__type
	
	def getText(self):
		return self.__text
	
	def getColor(self):
		return self.__color
	
	def getAlignment(self):
		return self.__alignment
	
	def getFont(self):
		return self.__font
	
	def getFontSize(self):
		return self.__fontSize
	
	def getBold(self):
		return self.__isBold
	
	def getItalic(self):
		return self.__isItalic
	
	def getUnderline(self):
		return self.__isUnderline
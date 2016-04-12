class Element():
	__id=""
	__type=""
	__text=""
	
	def __init__(self, id, type, text):
		self.__id = id
		self.__type = type
		if text is not None:
			self.__text = text
		return
	
	def __repr__(self):
		return ('id = ' + self.__id + ' | type = ' + self.__type + ' | text = ' + self.__text[:30])


	def getID(self):
		return self. __id
	
	def getType(self):
		return self.__type
	
	def getText(self):
		return self.__text
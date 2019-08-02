import re
import string
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))
ps = PorterStemmer()

class DocRef():
	
	file = ''
	length = 0.0
	
	def __init__(self,file='',length=0.0):
		self.file = file
		self.length = length

	def get_path(self):
		return self.file

	def get_length(self):
		return self.length
		
	def set_length(self,length):
		self.length = length

	def toVector1(self):
		file = open(self.file,'r')

		doc = file.read()
		file.close()
		doc = re.sub(r'[^a-z^A-Z]',' ',doc)
		doc = word_tokenize(doc)
		
		list1 = dict([])
		
		for w in doc:
			w = w.lower()
			if w in stop_words:
				continue
	
			if list1.__contains__(w):
				list1[w] = list1[w] + 1 
			else:
				list1[w] = 1
		return list1
		

	def toVector(self):
		file = open(self.file,'r')

		doc = file.read()
		file.close()
		doc = re.sub(r'[^a-z^A-Z]',' ',doc)
		doc = word_tokenize(doc)
		
		list1 = dict([])
		
		for w in doc:
			w = w.lower()
			if w in stop_words:
				continue
			w = ps.stem(w)
			if list1.__contains__(w):
				list1[w] = list1[w] + 1 
			else:
				list1[w] = 1
		return list1

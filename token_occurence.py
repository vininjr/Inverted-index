from document import DocRef

class TokenOccurence(object):
	doc = DocRef()
	count = 0
	size_d = 0.0
	tf = 0.0

	def __init__(self,doc,count=0):
		self.doc = doc
		self.count = count

	def set_doc(self, doc):
		self.doc = doc

	def get_doc(self):
		return self.doc
		
	def get_count(self):
		return self.count

	def set_count(self,count):
		self.count = count

	def set_tf(self,tf):
		self.tf = tf

	def get_tf(self):
		return self.tf




from document import DocRef
from token_occurence import TokenOccurence

class TokenInfo(object):
	idf = 0.0
	df = 0
	docs = [TokenOccurence]

	def __init__(self, idf, df, docs):
		self.idf = idf
		self.docs = docs
		self.df = df
	
	def get_idf(self):
		return self.idf
		
	def get_df(self):
		return self.df

	def get_docs(self):
		return self.docs

	def set_idf(self,idf):
		self.idf = idf

	def add_doc(self,t,count):
		doc_aux = DocRef(t.get_path())
		tk = TokenOccurence(doc_aux,count)
		self.df = self.df + 1
		self.docs.append(tk)

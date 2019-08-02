from indexer import read_docs
from token_info import TokenInfo
from token_occurence import TokenOccurence
from document import DocRef
from math import log2,sqrt
import pickle

class Index_inverted(object):

	h = dict()
	freq = dict()
	docs_size = dict()
	n_doc = 0
	Id = 0

	def printf(self):
		for t in self.h:
			print('termo = ',t)
			print('idf = ',self.h[t].idf)
			print('df = ',self.h[t].df)
			for w in self.h[t].get_docs():
				print('doc = ',w.doc.file)
				print('count = ',w.count)
				print('tf = ',w.tf)
				print('length = ',w.size_d)
				print('len1 = ',w.doc.length)
				print()
			print(' ----- ')

	def sref(self,path):

		list_docs = read_docs(path)
		self.n_doc = len(list_docs)
		d = dict()
		c = 0

		for path_doc in list_docs:
			d = DocRef(path_doc)
			v = d.toVector()
			c = c + 1
			for t in v.keys():
				if not self.h.__contains__(t):
					self.h[t] = TokenInfo(0,0,[])

				if self.freq.__contains__(path_doc):
					if v[t] > self.freq[path_doc][0]:
						self.freq[path_doc] = (v[t],t)
				else:
					self.freq[path_doc] = (v[t],t) 

				self.h[t].add_doc(d,v[t])
			self.docs_size[d.get_path()] = 0.0
			print(c)

		print('calculando tf')
		self.calc_tf()
		print('finalizou tf')
		print('calculando docsize')
		self.size_doc()
		print('finalizou docsize')
		print('salvando no arquivo')
		self.write_file()
		self.write_file1()
		print('salvou')

		return self.h

	def sref1(self,path):

		list_docs = read_docs(path)
		self.n_doc = len(list_docs)
		d = dict()
		c = 0

		for path_doc in list_docs:
			d = DocRef(path_doc)
			v = d.toVector1()
			c = c + 1
			for t in v.keys():
				if not self.h.__contains__(t):
					self.h[t] = TokenInfo(0,0,[])

				if self.freq.__contains__(path_doc):
					if v[t] > self.freq[path_doc][0]:
						self.freq[path_doc] = (v[t],t)
				else:
					self.freq[path_doc] = (v[t],t) 

				self.h[t].add_doc(d,v[t])
			self.docs_size[d.get_path()] = 0.0
			print(c)

		print('calculando tf')
		self.calc_tf()
		print('finalizou tf')
		print('calculando docsize')
		self.size_doc()
		print('finalizou docsize')
		print('salvando no arquivo')
		self.write_file()
		self.write_file1()
		print('salvou')

		return self.h

	def size_doc(self):
		for t in self.h.keys():
			self.h[t].set_idf(log2(self.n_doc/self.h[t].get_df()))
			for w in self.h[t].get_docs():
				self.docs_size[w.get_doc().get_path()] += (w.count*self.h[t].get_idf())**2
				#w.doc.length = (w.get_count()*self.h[t].get_idf())**2 
		for k in self.docs_size.keys():
			self.docs_size[k] = sqrt(self.docs_size[k])
		

	def calc_tf(self):
		for t in self.h.keys():
			for w in self.h[t].get_docs():
				w.set_tf(w.get_count()/self.freq[w.get_doc().get_path()][0])

	def write_file(self):
		file = open('data.pickle', 'wb')
		pickle.dump(self.h, file, pickle.HIGHEST_PROTOCOL)
		file.close()

	def write_file1(self):
		file = open('data1.pickle', 'wb')
		pickle.dump(self.docs_size, file, pickle.HIGHEST_PROTOCOL)
		file.close()

	def read_file1(self):
		file = open('data1.pickle', 'rb')
		self.docs_size = pickle.load(file)
		file.close()	

	def read_file(self):
		file = open('data.pickle', 'rb')
		self.h = pickle.load(file)
		file.close()	

	def read_index(self,index):
		file = open(index,'rb')
		self.h = pickle.load(file)
		file.close()

	def query1(self,path):
		r = dict()
		d = DocRef(path)
		q = d.toVector1()
		peso = 0.0

		for t in q.keys():
			if not(self.h.__contains__(t)):
				continue
			I = self.h[t].get_idf()
			K = q[t]
			W = K*I
			peso = peso + (W**2)

			L = self.h[t].get_docs()

			for O in L:
				T = O.get_doc()
				D = T.file
				C = O.count

				if not r.__contains__(D):
					r[D] = 0.0
				r[D] = r[D] + (W*I*C)
		
		L = 0.0
		L = sqrt(peso)

		for D in r.keys():
			r[D] = r[D] / (L * self.docs_size[D])
		
		list1 = sorted(r,key=r.get,reverse=True)
		l1 = []

		for w in list1:
			aux = w.split('/')
			l1.append(aux[len(aux)-1])
		#mude pfv, return l1 se e somente se vc estiver fazendo a avaliacao
		return l1[:100]

	def query(self,path):
		r = dict()
		d = DocRef(path)
		q = d.toVector()
		peso = 0.0

		for t in q.keys():
			if not(self.h.__contains__(t)):
				continue
			I = self.h[t].get_idf()
			K = q[t]
			W = K*I
			peso = peso + (W**2)

			L = self.h[t].get_docs()

			for O in L:
				T = O.get_doc()
				D = T.file
				C = O.count

				if not r.__contains__(D):
					r[D] = 0.0
				r[D] = r[D] + (W*I*C)
		
		L = 0.0
		L = sqrt(peso)

		for D in r.keys():
			r[D] = r[D] / (L * self.docs_size[D])
		
		list1 = sorted(r,key=r.get,reverse=True)
		l1 = []

		for w in list1:
			aux = w.split('/')
			l1.append(aux[len(aux)-1])
		#mude pfv, return l1 se e somente se vc estiver fazendo a avaliacao
		return l1[:100]

	def busca(self,str1):
		file = open('query.story','w')
		file.write(str1)
		file.close()
		return self.query('query.story')

	def busca1(self,str1):
		file = open('query.story','w')
		file.write(str1)
		file.close()
		return self.query1('query.story')
	
	def esta(self, lst, tk):
		for w in lst.keys():
			if w.file == tk.file:
				return w
		return False

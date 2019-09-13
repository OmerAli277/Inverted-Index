import sys

path = sys.path
temp = ['\\Users\\omerali\\AppData\\Local\\Programs\\Python\\Python37\\python37.zip', 'C:\\Users\\omerali\\AppData\\Local\\Programs\\Python\\Python37\\DLLs', 'C:\\Users\\omerali\\AppData\\Local\\Programs\\Python\\Python37\\lib', 'C:\\Users\\omerali\\AppData\\Local\\Programs\\Python\\Python37', 'C:\\Users\\omerali\\Desktop\\Semester # 7\\Information Retrieval\\Assignment 1 (inverted index)\\code\\venv', 'C:\\Users\\omerali\\Desktop\\Semester # 7\\Information Retrieval\\Assignment 1 (inverted index)\\code\\venv\\lib\\site-packages']
path += temp

import glob
import re

from bs4 import BeautifulSoup
from nltk.stem import PorterStemmer
from nltk import word_tokenize  
import pdb;


# Tokenizer class
class tokenizer: 

	# init method or constructor  
    def __init__(self, directory): 

    	self.all_documents = glob.glob(directory)

    	stop_wording = open('../stoplist.txt')
    	word = stop_wording.read()
    	stop_wording.close()
    	self.stop_word = re.split('\n+', word)

    	self.doc_ids = {}
    	self.term_ids = {} # dictionary of the term

    	self.dictionary = {}

    	self.hashmap_index = {}
    	self.term_id_count = 1

    	self.tuple_array = []
    	self.sorted_index = {}

    def make_tokens(self, html):

    	html_lowercase_text = html.lower()
    	tokens = re.split('[\s,.\':(){}?*!>>\\-\"&/|’“”»—]+', html_lowercase_text)
    	# print(tokens)
    	# scan = input()
    	return tokens 

    def apply_stop_word(self, tokens):

    	if len(tokens)>0:
    		for i in self.stop_word:
    			word_count = tokens.count(i)
    			if word_count > 0:
    				for j in range(word_count):
    					tokens.remove(i)

    	for i in tokens:
    		if len(i) == 1 or len(i) == 0:
    			tokens.remove(i)

    	return tokens

    def apply_stemming(self, tokens):

    	temp_tokens = []
    	ps = PorterStemmer()
    	for word in tokens:
    		temp_tokens.append(ps.stem(word))

    	return temp_tokens

    def add_position(self, term_id, docid, position):
    	if self.hashmap_index.get(term_id).get('posting').get(docid) != None:
    		self.hashmap_index[term_id]['posting'][docid].append(position)
    	else:
    		self.hashmap_index[term_id]['total_doc'] += 1
    		self.hashmap_index[term_id]['posting'][docid] = []
    		self.hashmap_index[term_id]['posting'][docid].append(position)

    def make_hashmap_index(self, docid, tokens):

    	position = 1
    	for term in tokens:

    		if self.dictionary.get(term) != None:

    			term_id = self.dictionary[term]
	    		self.tuple_array.append((term_id, docid, position))

	    		# if term exist in dictionary, it will exist in index
	    		self.hashmap_index[term_id]['occrances'] += 1
	    		self.add_position(term_id, docid, position)

	    	else:
	    		self.dictionary[term] = self.term_id_count 
	    		self.tuple_array.append((self.term_id_count, docid, position))
	    		self.hashmap_index[self.term_id_count] = {'occrances': 1, 'total_doc': 1,
	    		'posting':{ docid: [position] } }
	    		self.term_id_count += 1

	    	position += 1

    def sort_tuples(self):

    	# tuple (term_id, doc_id, positon_of_term)

    	counter = 0
    	# Traverse through 1 to len(arr) 
    	for i_tuple in self.tuple_array:
    		key = i_tuple[0]

    		# Move elements of arr[0..i-1], that are 
    		# greater than key, to one position ahead 
    		# of their current position 
    		j = counter - 1
    		check_value = self.tuple_array[j]
    		while j >=0 and key < check_value[0] : 

    			self.tuple_array[j+1] = self.tuple_array[j]
    			j -= 1
    			check_value = self.tuple_array[j]


    		self.tuple_array[j+1] = i_tuple
    		counter += 1

    def make_sorted_index(self):

    	print('Sorting the tuples according to term id...')
    	self.sort_tuples()

    	print('Createing Inverted index of sorted tuples...')
    	# tuple (term_id, doc_id, positon_of_term)
    	term_id_counter = 1
    	for i_tuple in self.tuple_array:

    		tuple_term_id = i_tuple[0]
    		tuple_doc_id = i_tuple[1]
    		tuple_term_pos = i_tuple[2]

    		if tuple_term_id != term_id_counter:
    			term_id_counter += 1

    		if tuple_term_id == term_id_counter:

    			if self.sorted_index.get(term_id_counter) == None:

    				self.sorted_index[term_id_counter] =  {'occrances': 1, 'total_doc': 1,
    				'posting':{ tuple_doc_id: [tuple_term_pos] } }

    			else:
    				self.sorted_index[term_id_counter]['occrances'] += 1

    				if self.sorted_index.get(term_id_counter).get('posting').get(tuple_doc_id) == None:
    					self.sorted_index[term_id_counter]['total_doc'] += 1
    					self.sorted_index[term_id_counter]['posting'][tuple_doc_id] = []
    					self.sorted_index[term_id_counter]['posting'][tuple_doc_id].append(tuple_term_pos)
    				else:
    					self.sorted_index[term_id_counter]['posting'][tuple_doc_id].append(tuple_term_pos)

    def tokenize(self):
    	term_id_count1 = 0
    	for i in range(len(self.all_documents)):
    		self.doc_ids[i] = self.all_documents[i]
    		file = open(self.all_documents[i], 'rb')
    		html_file = file.read()
    		file.close()
    		soup = BeautifulSoup(html_file, 'html.parser')

    		if soup.find('html'):
    			html = soup.find('html')

    		if html.find('script'):
    			for s in html('script'):
    				s.extract()

    		if html.find('style'):
    			for s in html('style'):
    				s.extract()

    		tokens = self.make_tokens(html.text)
    		clean_tokens = self.apply_stop_word(tokens)
    		stemmed_tokens = self.apply_stemming(clean_tokens)

    		self.make_hashmap_index(i+1, stemmed_tokens)

    		# for gh in self.hashmap_index:
    		# 	print(self.hashmap_index[gh])
    		# input()

    		# for count in range(len(stemmed_tokens)):
    		# 	try:
    		# 		self.term_ids[stemmed_tokens[count]]
    		# 	except KeyError:
    		# 		self.term_ids[stemmed_tokens[count]] = term_id_count1
    		# 		term_id_count1 += 1

    def make_files(self):

    	doc_ids_file = open('docids.txt', 'w+', encoding='utf-8')
    	for i in range(len(self.doc_ids)):
    		f_id = str(i+1) 
    		x = self.doc_ids[i].split('\\')
    		# print(x)
    		# input()
    		doc_ids_file.write(f_id + '\t' + x[1] + '\n')

    	term_ids_file = open('termids1.txt', 'w+', encoding='utf-8')
    	counter = 1
    	for i in self.dictionary:
    		f_id = str(counter) 
    		term_ids_file.write(f_id + '\t' + i + '\n')
    		counter += 1

    def save_index(self):
    	# print(self.hashmap_index)
    	# print(len(self.hashmap_index))
    	# for jj in self.hashmap_index:
    	# 	print('Term ID:' + str(jj))
    	# 	print(self.hashmap_index[jj])

    	# print(self.tuple_array)
    	self.make_sorted_index()
    	# print(self.tuple_array)
    	# print(len(self.hashmap_index))
    	for jj in self.sorted_index:
    		print('Term ID:' + str(jj))
    		print(self.sorted_index[jj])
    		

    	# print(self.dictionary)
    	# index_file = open('index.txt', 'w+')
    	# term_id = 1
    	# for index_object in self.hashmap_index:
    	# 	index_file.write(index_object[term_id] + ' ' + str(index_object[term_id]['occrances']) + ' ' +
    	# 	 str(index_object[term_id]['total_doc']) + ' ')
    	# 	for post in index_object[term_id]['posting']:
    	# 		for pos in post:
    	# 			index_file.write(pos + ',')
    	# 	index_file.write('\n')

    	# index_file.close()
 

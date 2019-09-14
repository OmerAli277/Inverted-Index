import sys

path = sys.path
temp = ['\\Users\\omerali\\AppData\\Local\\Programs\\Python\\Python37\\python37.zip', 'C:\\Users\\omerali\\AppData\\Local\\Programs\\Python\\Python37\\DLLs', 'C:\\Users\\omerali\\AppData\\Local\\Programs\\Python\\Python37\\lib', 'C:\\Users\\omerali\\AppData\\Local\\Programs\\Python\\Python37', 'C:\\Users\\omerali\\Desktop\\Semester # 7\\Information Retrieval\\Assignment 1 (inverted index)\\code\\venv', 'C:\\Users\\omerali\\Desktop\\Semester # 7\\Information Retrieval\\Assignment 1 (inverted index)\\code\\venv\\lib\\site-packages']
path += temp

import glob

from tokenizer import tokenizer


# inverted index class
class index: 

	# init method or constructor  
    def __init__(self, directory):
    	self.all_documents = glob.glob(directory)
    	
    	self.dictionary = {}
    	self.doc_ids = {}


    	self.hashmap_index = {}
    	self.term_id_count = 1

    	self.tuple_array = []
    	self.sorted_index = {}

    def make_files_of_terms_and_documents(self):

    	doc_ids_file = open('docids.txt', 'w+', encoding='utf-8')
    	for i in range(len(self.doc_ids)):
    		f_id = str(i+1) 
    		x = self.doc_ids[i+1].split('\\')
    		doc_ids_file.write(f_id + '\t' + x[1] + '\n')

    	term_ids_file = open('termids1.txt', 'w+', encoding='utf-8')
    	counter = 1
    	for i in self.dictionary:
    		f_id = str(counter) 
    		term_ids_file.write(f_id + '\t' + i + '\n')
    		counter += 1

    def add_position(self, term_id, docid, position):
    	if self.hashmap_index.get(term_id).get('posting').get(docid) != None:
    		self.hashmap_index[term_id]['posting'][docid].append(position)
    	else:
    		self.hashmap_index[term_id]['total_doc'] += 1
    		self.hashmap_index[term_id]['posting'][docid] = []
    		self.hashmap_index[term_id]['posting'][docid].append(position)

    def addto_hashmap_index(self, docid, tokens):

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
	    		# for sorted method of creating index 
	    		self.tuple_array.append((self.term_id_count, docid, position))

	    		# making index directly form tokens
	    		self.hashmap_index[self.term_id_count] = {'occrances': 1, 'total_doc': 1,
	    		'posting':{ docid: [position] } }
	    		self.term_id_count += 1

	    	position += 1

    def parse_documents(self):
    	print('Parsing the documents and creating Hashmap index ...')
    	tokenizer_obj = tokenizer()
    	for i in range(len(self.all_documents)):
    		self.doc_ids[i+1] = self.all_documents[i]
    		tokens = tokenizer_obj.parse(self.all_documents[i])
    		# Creating Index while parsing
    		self.addto_hashmap_index(i+1, tokens)

    	print('Saving the term id and document id files...')
    	# Files of term id and document id
    	self.make_files_of_terms_and_documents()

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

    def save_index(self):
    	# print(self.hashmap_index)
    	# print(len(self.hashmap_index))
    	# for jj in self.hashmap_index:
    	# 	print('Term ID:' + str(jj))
    	# 	print(self.hashmap_index[jj])

    	# print(self.tuple_array)

    	# self.make_sorted_index()


    	# print(self.tuple_array)
    	# print(len(self.hashmap_index))

    	for jj in self.sorted_index:
    		print('Term ID:' + str(jj))
    		print(self.sorted_index[jj])
    		

    	# print(self.dictionary)

    	index_file = open('index.txt', 'w+')
    	term_id = 1

    	for index_key in self.hashmap_index:

    		index_file.write(str(index_key) + ' ' + str(self.hashmap_index[index_key]['occrances']) + ' ' +
    		 str(self.hashmap_index[index_key]['total_doc']) + ' ')

    		temp_posting = self.hashmap_index[index_key]['posting']

    		first = True
    		previous_key = -1

    		for key in temp_posting:

    			if first == True:
    				first = False
    				index_file.write(str(key))
    				previous_key = key

    			else: 
    				index_file.write(str(key-previous_key))
    				previous_key = key

    			positions = temp_posting[key]
    			flag = True
    			previous_position = -1
    			for i in positions:
    				if flag == True:
    					flag = False
    					index_file.write(',' + str(i))
    					previous_position = i
    				else:
    					index_file.write(',' + str(i-previous_position))
    					previous_position = i

    			index_file.write(' ')

    		index_file.write('\n')

    	index_file.close()



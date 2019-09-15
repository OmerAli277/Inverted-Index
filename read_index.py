import sys

index = {}
dictionary = {}

def read_index():

	index_file = open('index.txt', 'r')
	content = index_file.readlines()
	index_file.close()

	number_string = ''
	number = -1

	for line in content:

		flag_term = True
		flag_occrances = True
		flag_total_doc = True
		flag = False
		flag2 = False
		flag_first_doc = True

		term_id = -1
		occrances = -1
		total_doc = -1

		doc_id = -1
		pre_doc_id = 0

		position = -1
		pre_position = 0


		for ch in line:

			if ch == ' ':
				number = int(number_string)
				number_string = ''

				if flag_term == True:
					flag_term = False
					term_id = number

				elif flag_occrances == True:
					flag_occrances = False
					occrances = number

				elif flag_total_doc == True:
					flag_total_doc = False
					total_doc = number

				if flag == True:
					flag = False

					if flag2 == True:
						pre_position = 0
						position = -1

					position = pre_position + number
					pre_position = position
					index[term_id]['posting'][doc_id].append(position)

			elif ch == ',':

				number = int(number_string)
				number_string = ''

				if flag_first_doc == True:
					flag_first_doc = False
					doc_id = number + pre_doc_id
					index[term_id] = {'occrances': occrances, 'total_doc': total_doc, 'posting': {doc_id: []}}
					pre_doc_id = doc_id
				else:
					if number != 0:
						doc_id = number + pre_doc_id
						flag2 = True
						index[term_id]['posting'][doc_id] = []
						pre_doc_id = doc_id
					else:
						flag2 = False

				flag = True

			else:
				number_string += ch

def read_dictionary():

	dictionary_file = open('termids1.txt', 'r')
	content = dictionary_file.readlines()
	dictionary_file.close()

	number_string = ''
	term_id = 0

	for line in content:

		for ch in line:

			if ch == '\t':
				term_id = int(number_string)
				number_string = ''

			elif ch == '\n':
				dictionary[number_string] = term_id
				number_string = ''

			else:
				number_string += ch



def main():
	if sys.argv[1] == '--term':
		read_dictionary()
		read_index()

		if dictionary.get(sys.argv[2]) != None:
			term = sys.argv[2]
			term_id = dictionary[term]
			occrances = index[term_id]['occrances']
			total_doc = index[term_id]['total_doc']
			print('Listing for term:' + str(term))
			print('TERMID:' +  str(term_id))
			print('Number of documents containing term:' + str(total_doc))
			print('Term frequency in corpus:' + str(occrances))
		else:
			print('Term defined by the user does not exist in index.')
	else:
		print('Command line arguments are not correct.')

main()

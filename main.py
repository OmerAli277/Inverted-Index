from inverted_index import index

def main():
	print("Enter the diretory(use * for multiple files):")
	diretory = input()

	index_obj = index(diretory)
	index_obj.parse_documents()

	index_obj.make_sorted_index()

	index_obj.save_index()

main()
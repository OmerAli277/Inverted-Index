from tokenizer import tokenizer

def main():
	print("Enter the diretory(use * for multiple files):")
	diretory = input()
	tokenizer1 = tokenizer(diretory);
	tokenizer1.tokenize()
	tokenizer1.make_files()
	tokenizer1.save_index()	

main()
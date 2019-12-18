import glob
import re
import pdb

from bs4 import BeautifulSoup
from nltk.stem import PorterStemmer
from nltk import word_tokenize  


# Tokenizer class
class tokenizer: 

	# init method or constructor  
    def __init__(self): 
    	stop_wording = open('../stoplist.txt')
    	word = stop_wording.read()
    	stop_wording.close()
    	self.stop_word = re.split('\n+', word)

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

    	# Remove tokens which are only alphabets because they are meaningless
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

    def parse(self, directory):
    	file = open(directory, 'rb')
    	html_file = file.read()
    	file.close()
    	soup = BeautifulSoup(html_file, 'html.parser')

    	if soup.find('html'):
    		html = soup.find('html')
    	else:
    		html = soup

    	if html.find('script'):
    		for s in html('script'):
    					s.extract()

    	if html.find('style'):
    		for s in html('style'):
    					s.extract()

    	# content preprocessing
    	tokens = self.make_tokens(html.text)
    	clean_tokens = self.apply_stop_word(tokens)
    	stemmed_tokens = self.apply_stemming(clean_tokens) 

    	return stemmed_tokens

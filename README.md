# Inverted Index
## Description
Inverted index is a underlying data structure used by search engines nowadays. It maps the words to their locations in documents. As, it is implmented using hashmap data structure. The searching is very fast and it is constant time.  
## Environment
Python       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   3.7.3<br/>

beautifulsoup4 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 4.8.0<br/>

bs4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0.0.1<br/>

nltk      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3.4.5<br/>

## tokenizer.py
It is the implementation of tokenizer which break down the sentences into words, stem them using nltk Porter stemmer and remove the stop words from these tokens.
## inverted_index.py
It creates inverted index using two methods. 
#### 1. [Sorting-based inverted index construction](https://nlp.stanford.edu/IR-book/html/htmledition/a-first-take-at-building-an-inverted-index-1.html "A first take at building an inverted index") 
It is first sort the token id and document id tuples, then create list by squeezing this array into inverted index.
![alt text](https://github.com/OmerAli277/HelloWorld/blob/master/sorting_index.PNG "Sorting-based inverted index")
#### 2. Hashmap Inverted index
In this project, python dictionary is used instead of the hashmap. The Single-pass in-memory indexing is used to construct the index.

![alt text](https://github.com/OmerAli277/HelloWorld/blob/master/spimi.PNG "SPIMI")
#### 3. Delta Encoding

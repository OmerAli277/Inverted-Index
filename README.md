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
After the construction, index is stored in the index.txt which is zipped. The index.txt is containing the file position for each occurrence of each term in the collection. Each line contain the complete inverted list for a single term. Each line contain a list of DOCID,POSITION values. Each line of this file contain a TERMID followed by a space-separated list of properties as
follows:<br/>
347 1542 567 432,43 456,33 456,41<br/>
o 347: TERMID<br/>
o 1542: Total number of occurrences of the term in the entire corpus<br/>
o 567: Total number of documents in which the term appears<br/>
o 432: Document Id in which term appears<br/>
o 43: Position of term in document 432<br/>
In order to support more efficient compression, delta encoding is applied to the inverted list. The first DOCID for a term and the first POSITION for a document will be stored normally. Subsequent values stored as the offset from the prior value.
Instead of encoding an inverted list like this:<br/>
347 1542 567 432,43 456,33 456,41<br/>
It is encoded like this:<br/>
347 1542 567 432,43 24,33 0,8<br/>

## read_index.py
This file reads the index from index.txt and allocate the index into memory. The file accept the word as command line argument and search it into the index like following:<br/>
$ ./read_index.py --term apple

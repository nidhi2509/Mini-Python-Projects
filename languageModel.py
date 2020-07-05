import nltk
class LanguageModel:
	def __init__(self, textFileList):
		bigramList = []
		N_c
		vocabSize
		Vocab
		vocabCount
		
		
	def smoothed_count(self, bigram):
		#input = bigram
		#return smoothed count 
		
	def build_ngram_data(self, textFileList): #model file
		#tokenize	
		punct = r"(['.,\?!``()\";'':/|`])"
		listOfTokenizedFiles = []
		
    for textFile in textFileList:   #open every file
    	open(textFile, 'r')
    	toks = nltk.word_tokenize(textFile)
      listOfTokenizedFiles.append(toks) #list of lists containing unigrams from model file
      for m in listOfTokenizedFiles:
      	if m in punct:
        	listOfTokenizedFiles.remove(m) #exclude punctuations
					
		#dictionary or count of the unigrams
		
		for item in listOfTokenizedFiles:
			
			
		
		
		
	def get_logProb(self, tokenList):
		
		
	def get_ngram_logProb(slef, ngram):
		
		
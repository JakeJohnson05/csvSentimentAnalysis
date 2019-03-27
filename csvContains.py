import re, csv
from string import punctuation

txt = 'You are a good friend. You are amazing! I love you so much'

def getSentimentRating(txt):
	# alphabet = 'abcdefghijklmnopqrstuvwxyz'
	txt = txt.translate(str.maketrans('', '', punctuation)).lower()
	txtList = txt.split(' ')
	txtList.sort()
	
	positiveWords = 0;
	with open('positiveWords.csv', 'r') as csvFile:
		fileReader = csv.reader(csvFile, delimiter=',')
		
		for row in fileReader:
			for word in txtList:
				if word in row: positiveWords += 1

	print('--%i-- positive words of --%i-- total words ' %(positiveWords, len(txtList)))
		


print (getSentimentRating(txt))
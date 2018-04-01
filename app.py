import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def print_def(word):
	definition = data[word]
	if len(definition) > 1 :
		print ("The word %s has multiple definitions :" % word)
		for i in definition:
			print ("* ",i)
		return ""
	else:
		print ("* ", data[word][0])
		return ""

def define(word):
	if word in data :
		return print_def(word)
	else:
		word = word.lower()
		if word in data:
			return print_def(word)
		elif len(get_close_matches(word, data.keys()) ) > 0 :
			close_matches = get_close_matches(word,data.keys())
			yn = input ("Do you mean %s instead ? Y/N :" % close_matches[0]).upper()
			if yn == "Y":
				return print_def(close_matches[0])
			elif yn == "N":
				return "This word does not exist, sorry...!"
			else :
				return "We didn't get your choice, sorry...!"
		else:
			return "This word does not exist, please double check!"
	
word = input("Enter word: ")

print(define(word))
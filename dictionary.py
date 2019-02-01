import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def getmeaning(w):
	w=w.lower()
	
	if w in data:
		return data[w]		
	elif w.title() in data:
		return data[w.title()]
	elif w.upper() in data:
		return data[w.upper()]
	
	closematches=get_close_matches(w,data.keys())
	if len(closematches)>0:
		ch=input("Did you mean %s instead? (y/n): " %closematches[0])
		if ch=="y":
			return data[closematches[0]]
	else:
		return "Word doesn't exist"


while (True):

	word=input("\nEnter the word: ")
	output=getmeaning(word)
	if type(output)==list:
		for word in output:
			print(word)
	else:
		print(output)	
	ch=input("Continue? (y/n): ")
	if ch=="n":
		break;
print("Bye\n")

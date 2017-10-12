#Fetch that

import urllib.request
#import enchant

def findWord():
	req = urllib.request.Request('http://www.voidspace.org.uk')
	with urllib.request.urlopen(req) as response:
	   the_page = response.read()
	page = str(the_page)
	page = page.split()


	cleanPage = []
	abc = 'abcdefghijklmnopqrstuvwxyz'
	ABC = abc.upper()
	letters = abc + ABC
	for e in page:
	    word = ''
	    for c in e:
	        if c in letters:
	            word += c
	    if word != '':
	        cleanPage.append(word)

	#print(cleanPage[1:100])
	'''
	d = enchant.Dict("en_US")

	cleanPage = []
	for i in page:
	    if d.check(page[i]):
	        cleanPage.append(page[i])

	print(cleanPage[1:100])
	'''

	val = input("What word would you like to find: ")
	x = 0
	for i in range(len(cleanPage)):
	    if cleanPage[i] == val:
	        x += 1
	print("The word", val, "was found", x, "times")
findWord()
time = input(" ")
import urllib.request
#import enchant

def findWord():
    while(True):
        try:
            url = input("Enter in any website you want: ")
            req = urllib.request.Request(url)
            with urllib.request.urlopen(req) as response:
               the_page = response.read()
            page = str(the_page)
            page = page.split()
            break
        except:
            print("Your url is invalid")


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
        if cleanPage[i].lower() == val.lower():
            x += 1
    print("The word", val, "was found", x, "times")
    findWord()
    
findWord()

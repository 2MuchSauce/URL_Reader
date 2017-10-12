from newspaper import Article

def findWord():
    while(True):
        try:
            url = input("URL: ")
            article = Article(url, language='en') # English
            article.download()
            article.parse()
            break
        except:
            print("Your url is invalid")

    #url = 'http://www.cnn.com/2017/10/10/entertainment/donna-karan-harvey-weinstein/index.html'
    
    print(article.text[:])  
    while(True):
        print("[Input 0 to Quit]")
        val = input("What word would you like to find: ")
        if(val == "0"):
            print("Program has ended")
            break
        x = 0

        articleArray = article.text.split()
        for i in range(len(articleArray)):
            if val.lower() in articleArray[i].lower():
                x += 1
        print("The word", val, "was found", x, "times")
    

findWord()

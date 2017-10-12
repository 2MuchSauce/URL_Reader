import newspaper
from newspaper import Article

'''

Program is designed to check every article on CNN to see if it says trump
it takes awhile....

Update: works with other news websites now!

Article check goes through every website in newspaper.popular_urls()
and says how many articles are on each website

Category check goes through every website in newspaper.popular_urls()
and says how many categoryies are on each website

'''

def articleCheck():
    websiteArray = newspaper.popular_urls()
    #print(websiteArray)
    for url in range (len(websiteArray)):
        paper = newspaper.build(websiteArray[url], memoize_articles=False)
        for article in paper.articles:
            print(article.url)
        print ("\n")
        print ("{} has {} articles.\n".format(websiteArray[url],paper.size()))

def categoryCheck():
    websiteArray = newspaper.popular_urls()
    #print(websiteArray)
    for url in range (len(websiteArray)):
        paper = newspaper.build(websiteArray[url])
        categoryArray = paper.category_urls()
        print ("{} has {} Categories.\n".format(websiteArray[url],len(categoryArray)))
        for category in categoryArray:
            print(category)
        print ("\n")
        

        
def trumpCheck(websiteName, url):
    cnn_paper = newspaper.build(url, memoize_articles=False)
    '''
    for article in cnn_paper.articles:
        print(article.url)
    '''
    x = 0
    val = "trump"
    maxNumArticles = cnn_paper.size()
    print ("{} has {} articles.\n".format(websiteName,maxNumArticles))
    for i in range(len(cnn_paper.articles)):
        article = cnn_paper.articles[i]
        article.download()
        article.parse()
        #print(article.text[:])
        articleArray = article.text.split()
        for j in range(len(articleArray)):
            if val.lower() in articleArray[j].lower():
                x += 1
        print ("{} - Article: {}/{} - Trumps: {}\n".format(websiteName,i,maxNumArticles,x))
            

    print("The word", val, "was found", x, "times")

while(True):
    choice = input("Run Trump Check [t], Article Check [a] or Category Check [c]       [q] to Quit")

    if(choice == "t"):
        print ("what website?")
        website = input("ABC News [a], BBC News [b], CNN [c], Huffington Post [h], Fox News [f], NBC News [n]")
        if(website == "a"):
            trumpCheck('ABC News','http://abcnews.go.com/')
        elif(website == "c"):
            trumpCheck('CNN','http://cnn.com')
        elif(website == "b"):
            trumpCheck('BBC News','http://www.bbc.com/news')
        elif(website == "h"):
            trumpCheck('Huffington Post','https://www.huffingtonpost.com/')
        elif(website == "f"):
            trumpCheck('Fox News','http://www.foxnews.com/')
        elif(website == "n"):
            trumpCheck('NBC News','https://www.nbcnews.com/')
    elif(choice == "a"):
        articleCheck()
    elif(choice == "c"):
        categoryCheck()
    elif(choice == "q"):
        print("Program ended...");
        break

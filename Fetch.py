from newspaper import Article
url = input("URL: ")
#url = 'http://www.cnn.com/2017/10/10/entertainment/donna-karan-harvey-weinstein/index.html'

article = Article(url, language='en') # English

article.download()
article.parse()

print(article.text[:])

val = input("What word would you like to find: ")
 
x = 0

articleArray = article.text.split()
for i in range(len(articleArray)):
        if val.lower() in articleArray[i].lower():
                x += 1
print("The word", val, "was found", x, "times")

import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import os

name = input("Enter The Author's name : ")
n_split = name.split(' ')
if len(n_split) > 1:
    n1 = n_split[0]
    n2 = n_split[1]

url = "https://www.goodreads.com/search?q=" + n1 + "+" + n2 + "&search%5Bsource%5D=goodreads&search_type=quotes&tab=quotes"
#url = r"https://www.goodreads.com/quotes/search?q=" + n1 + '+' + n2 + "&commit=Search"

url = url.strip()

page = urllib.request.urlopen(url)

soup = BeautifulSoup(page,"html.parser")

#print(soup.prettify())

divs = soup.find_all('div',class_="quoteText")

authors = []
quotes = []

with open("quotes.txt",'w') as f:
    f.write("The famous Quote of " + name + " are : \n\n")

for div in divs:
    #print(div.text)
    text = div.text
    text = text.replace('“','"')
    text = text.replace('”','"')
    text = text.replace('\n','')
    text = text.replace('  ','')
    split = text.split('"')
    quote = split[1]
    author = split[2]
    author = author.replace('―','')
    author = author.split(',')[0]
    #print(quote)
    #print(author)
    #authors.append(author)
    #quotes.append(quote)

    if os.path.exists("quotes.txt"):
        append_write = 'a'
    else:
        append_write = 'w'
    
    with open("quotes.txt",append_write) as f:
        f.write(str(quote)+'\n'+'\n')

print("\nAll the quotes are saved in the file : quotes.txt\n")
#data = pd.DataFrame()

#print(len(authors))
#print(len(quotes))

#data['Authors'] = authors
#data['Quotes'] = quotes


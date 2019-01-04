import urllib.request, urllib.parse, urllib.error


#this opens the url on the internet and returns a encoded version of the website source code
fHand = urllib.request.urlopen('url for the website you want to scrape')

#this will print the decoded source code of the site out.
for line in fHand:
    print(line.decode())




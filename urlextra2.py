from urllib.request import urlopen

page = urlopen('https://www.geeksforgeeks.org')

sourcecode = page.read()
print(sourcecode)

# extre all the tags o this page
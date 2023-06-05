from urllib.request import urlopen


page = urlopen(input('entre the HTTP request'))

print(page.headers)
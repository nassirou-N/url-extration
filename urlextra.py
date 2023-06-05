from urllib.request import urlopen


page = urlopen("https://www.geeksforgeeks.org")

print(page.headers)
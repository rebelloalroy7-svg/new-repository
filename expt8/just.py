from bs4 import BeautifulSoup
html = "<html><body><h1>Hello, world!</h1></body></html>"
soup = BeautifulSoup(html, "html.parser")
print("Text inside h1:", soup.h1.text)

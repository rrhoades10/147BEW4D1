import requests 
from bs4 import BeautifulSoup

# fetching data from a website
response = requests.get("https://www.codingtemple.com")
print(response)
# specifically accessin the status code
print(response.status_code)
# print(response.content)

# parsing html from a website
soup = BeautifulSoup(response.content, "html.parser")

# print website title
print(soup.title.text)

print(soup.p)

print(soup.find_all('p'))
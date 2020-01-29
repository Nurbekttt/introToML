from bs4 import BeautifulSoup
import urllib
soup = BeautifulSoup(urllib.request.urlopen("krisha.kz"))

print(soup.find_all('p'))

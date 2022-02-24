from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
textOfPage = response.text

soup = BeautifulSoup(textOfPage, 'html.parser')
nameOffilms = soup.find_all(name='h3',class_='title')
arrayOfmovie = []

for film in nameOffilms:
    arrayOfmovie.append(film.getText())


arrayOfmovie.reverse()

try:
    data = open("movie.txt","w")
except FileNotFoundError:
    data = open("movie.txt","w")

for file in arrayOfmovie:
    data.write(file)
    data.write("\n")
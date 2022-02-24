import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="77c0810d116944bab3b68371e229c735",client_secret="408eb40232654d11ac835b6ea810ea67"))


# val = input("YYYY-MM-DD")
# print(val)


def findSong():
    response = requests.get("https://www.billboard.com/charts/hot-100/2000-08-12/")
    html_container = response.text
    soup= BeautifulSoup(html_container,"html.parser")
    print("This is song from 2008:")
    songFinds = soup.find_all(name = 'h3', class_="a-no-trucate" )
    for song in songFinds:
        print(song.getText())


findSong()




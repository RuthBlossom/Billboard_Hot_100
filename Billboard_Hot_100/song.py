from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify credentials
SPOTIPY_REDIRECT_URI = 'http://example.com'
SPOTIPY_CLIENT_ID='your_spotify_client_id'
SPOTIPY_CLIENT_SECRET='your_spotify_client_secret'

# Billboard Hot 100 URL
BILLBOARD_HOT_TOP_100_URL = "https://www.billboard.com/charts/hot-100/"

# Get user input for the date
date = input("Which year do you want to travel to? type the date in this format 'YYYY-MM-DD':\n")

# Scraping Billboard 100 to get a list of song titles
response = requests.get(url=BILLBOARD_HOT_TOP_100_URL + date)
html_page = response.text
soup = BeautifulSoup(html_page, "html.parser")
music_list = soup.select(selector='li button span.chart-element__information__song')
music_titles = [element.getText().strip() for element in music_list]
print(music_titles)

# Spotify authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope="playlist-modify-private",
    show_dialog=True,
    cache_path=".cache"
))

# Search Spotify for each song title and create a dictionary of song titles and their Spotify URLs
musics_dict = {}
for album in music_titles:
    try:
        result = sp.search(q=f"track:{album} year:{date.split('-')[0]}", type="track", limit=1, offset=0)
        song_dic = result["tracks"]
        song_items = song_dic["items"]
        song = song_items[0]["external_urls"]["spotify"]
        musics_dict[album] = song
    except IndexError:
        pass

print(musics_dict)

# Creating a new private playlist on Spotify
playlist = sp.user_playlist_create(user=sp.current_user()["id"], name=f"{date} Billboard 100", public=False, collaborative=False, description='')

# Adding songs to the created playlist
for title, url in musics_dict.items():
    try:
        song_id = url.split("/")[-1]
        sp.playlist_add_items(playlist_id=playlist["id"], items=[f'spotify:track:{song_id}'])
    except Exception as e:
        print(f"Error adding {title} to the playlist: {e}")

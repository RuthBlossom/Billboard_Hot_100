# Import necessary libraries
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Scraping Billboard 100
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# Make a GET request to the Billboard Hot 100 chart URL for the specified date and parse the HTML content
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
soup = BeautifulSoup(response.text, 'html.parser')

# Use CSS selector to select the <h3> elements nested within <li> elements within <ul> elements within <li> elements
# This is done to target the specific structure of the Billboard Hot 100 chart HTML
song_names_spans = soup.select("li ul li h3")

# Extract the text content of each <h3> element (song name) and strip any leading or trailing whitespace
song_names = [song.getText().strip() for song in song_names_spans]

# Spotify Authentication
# Create a Spotify instance with authentication using the SpotifyOAuth
# This involves providing client ID, client secret, redirect URI, and setting up the required scope for playlist modification
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com",
        client_id="73127468045d4d3da581040e285c5264",
        client_secret="4d97a2371cba4dd3805913038eeff959",
        show_dialog=True,
        cache_path="token.txt"
    )
)

# Get the current user's Spotify ID
user_id = sp.current_user()["id"]
print(user_id)

# Searching Spotify for songs by title
# Iterate through each song name, search for it on Spotify using the track and year information
# Retrieve the URI (Uniform Resource Identifier) for each found track and append it to the song_uris list
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist on Spotify. Skipped.")

# Creating a new private playlist in Spotify
# Create a new private playlist on the user's Spotify account with the name based on the specified date and Billboard 100
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

# Adding songs found into the new playlist
# Add the songs identified by their URIs to the newly created playlist on Spotify
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)



























































































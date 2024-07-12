# Billboard_Hot_100
 create a Spotify playlist based on the Billboard Hot 100 chart for a specific date. The script scrapes the Billboard website for song data and then uses the Spotify API to create a playlist with those songs.
 
![song](https://github.com/user-attachments/assets/c2e29748-3df5-4df0-8033-03b23d825149)


## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your machine.
- A Spotify Developer account to create a Spotify app and get your `client_id` and `client_secret`.
- Install the required Python packages:
  - `beautifulsoup4`
  - `requests`
  - `spotipy`
  - `python-dotenv`

You can install the required packages using pip:

```bash
pip install beautifulsoup4 requests spotipy python-dotenv
```

## Getting Started

1. **Clone the repository:**


2. **Set up Spotify Developer Application:**

   - Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
   - Create a new application to get your `Client ID` and `Client Secret`.
   - Set the Redirect URI to `https://example.com` (you can use any valid URI, but it should match the redirect URI specified in your script).

3. **Configure your private keys:**

   Create a file named `.env` in the project directory and add the following:

```env
SPOTIPY_CLIENT_ID='your_spotify_client_id'
SPOTIPY_CLIENT_SECRET='your_spotify_client_secret'
SPOTIPY_REDIRECT_URI='your_redirect_uri'
```

Replace `your_spotify_client_id`, `your_spotify_client_secret`, and `your_redirect_uri` with your actual Spotify API credentials.

4. **Run the script:**

```bash
python song.py
```

## How It Works

1. **User Input:**
   - The script prompts the user to enter a date in the format 'YYYY-MM-DD'.
   
2. **Scraping Billboard 100:**
   - The script makes a GET request to the Billboard Hot 100 chart URL for the specified date and parses the HTML content using BeautifulSoup.
   - It extracts the song titles from the HTML.

3. **Spotify Authentication:**
   - The script uses the Spotipy library to authenticate with the Spotify API using the credentials provided in the `.env` file.
   - It requests the `playlist-modify-private` scope to create and modify a private playlist.

4. **Searching Spotify:**
   - For each song title, the script searches Spotify to find the corresponding track and retrieves its URI.
   - It creates a dictionary mapping song titles to their Spotify URLs.

5. **Creating and Populating Playlist:**
   - The script creates a new private playlist on the user's Spotify account with the name based on the specified date and Billboard 100.
   - It adds the songs to the playlist using their Spotify URIs.

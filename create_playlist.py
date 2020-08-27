import json
import requests
from secrets import spotify_user_id, spotify_token

class CreatePlaylist:

    def _init_(self):
        self.user_id = spotify_user_id
        self.spotify_token = spotify_token

    #Step 1: Log into youtube
    def get_youtube_client(self):
        pass

    #Step 2: Grab Liked Videos
    def get_liked_videos(self):
        pass

    #Step 3: Create a new playlist
    def create_playlist(self):

        request_body = json.dumps({
            "name":"Youtube Liked Vids",
            "description": "All Liked Youtube Videos",
            "public": True
        })

        query = "https://api.spotify.com/v1/users/{}/playlists".format(self.user_id)
        response = requests.post{
            query,
            data = request_body,
            headers={
                "Content-Type":"application/json",
                "Authorization":"Bearer {}".format(spotify_token)
            }
        }
        response_json = response.json()

        #playlist id
        return response_json["id"]

    #Step 4: Search for the song
    def get_spotify_uri(self, song_name, artist):
        query = "https://api.spotify.com/v1/search?query=track%3A{}+artists%3A{}&type=track&offset=0&limit=20".format(
            song_name,
            artist
        )
        response = requests.get(
            query,
            headers={
                "Content-Type":"application/json",
                "Authorization":"Bearer {}".format(spotify_token)
            }
        )
        response_json = response.json()
        songs = response_json["tracks"]["items"]

        #only use the first song
        uri = songs[0]["uri"]

        return uri

    #Step 5: Add this song into the new Spotify PLaylist
    def add_song_to_playlist(self):
        pass

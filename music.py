import spotipy
import csv
import json
import requests
from spotipy.oauth2 import SpotifyClientCredentials
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

music = []
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

genres = ["Rap", "Rock", "Pop", "Blues", "R&B", "Country", "Latin", "EDM", "Folk", "Metal"]
music_list = []

def add_to_music(list):
    for i, t in enumerate(list['tracks']['items']):
        tids = [t['id']]
        features = sp.audio_features(tids)
        if (features[0] is None) or (len(features) == 0):
            print 'no features'
        else:
            print(len(music_list), ': ', t['name'])
            song_info = [tids[0], t['name'], t['artists'][0]['name'], features[0]['tempo'], genres[x]]
            if song_info not in music_list:
                music_list.append(song_info)

for x in range(0, len(genres)):
    print genres[x]
    results = sp.search(q='genre:' + genres[x], limit=50, type='track')
    add_to_music(results)
    results = sp.search(q='genre:' + genres[x], limit=50, offset=50, type='track')
    add_to_music(results)

print len(music_list)

with open('music.csv', 'w') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(music_list)

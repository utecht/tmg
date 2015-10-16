import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(requests.get('http://songmeanings.com/artist/view/songs/7770/').content)

songs = soup.find(id='songslist')

for song in songs.find_all('tr'):
    title = song.td.a.text
    link = song.td.a.get('href')
    lyrics_page = BeautifulSoup(requests.get(link).content)
    try:
        [x.decompose() for x in lyrics_page.find(class_='holder lyric-box').find_all('a')]
        lyrics = lyrics_page.find(class_='holder lyric-box').text.strip()
        print("{} {}".format(title, len(lyrics)))
        with open(title, 'w') as f:
            f.write(lyrics)
    except:
        print("Error {} {}".format(title, link))

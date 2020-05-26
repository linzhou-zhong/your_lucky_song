import sys
import requests
import urllib.request

from bs4 import BeautifulSoup
from datetime import datetime

__all__ = ['your_lucky_song']


class your_lucky_song:

    url_billboard = 'https://www.billboard.com/charts/hot-100/'
    url_youtube = 'https://www.youtube.com/results?search_query='

    def __init__(self, day=None, month=None, year=None):
        self.day = day or datetime.now().day
        self.month = month or datetime.now().month
        self.year = year or datetime.now().year
        self.birthday = datetime(self.year, self.month, self.day)
        self.url_billboard += self.birthday.strftime("%Y-%m-%d")

    def __generate_youtube_url(self, first_class_song, first_class_singer):
        try:
            # Generate search query with key words, ex : banana+conkarah
            query = urllib.parse.quote(first_class_song + ' ' + first_class_singer)

            r = requests.get(self.url_youtube + query)

            if r.status_code != 200:
                raise r.raise_for_status()

            soup = BeautifulSoup(r.text, 'html.parser')

        except Exception as e:
            print(e)
            sys.exit(1)

        # Return the top ranked playlist
        return ['https://www.youtube.com' + vid['href'] for vid in soup.findAll(attrs={'class': 'yt-uix-tile-link'})][0]

    def feel_lucky(self):
        try:
            r = requests.get(url=self.url_billboard)

            if r.status_code != 200:
                raise r.raise_for_status()

            else:
                soup = BeautifulSoup(r.text, 'html.parser')
                songs_list = soup.find_all('span', attrs={
                    'class': 'chart-element__information__song text--truncate color--primary'})
                singers_list = soup.find_all('span', attrs={
                    'class': 'chart-element__information__artist text--truncate color--secondary'})

                if not songs_list or not singers_list:
                    raise Exception("Cannot find any useful information from your given date...")

                else:
                    songs_list = [song.get_text() for song in songs_list]
                    singers_list = [singer.get_text() for singer in singers_list]
                    first_class_song = songs_list[0]
                    first_class_singer = singers_list[0]
                    return self.__generate_youtube_url(first_class_song, first_class_singer)

        except Exception as e:
            print(e)
            sys.exit(1)

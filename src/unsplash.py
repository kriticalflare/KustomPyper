import requests
import secrets
import wall

import urllib.parse


class Unsplash:
    def __init__(self, width, height):
        self.BASE_URL = "https://source.unsplash.com"
        self.width = width
        self.height = height
        self.query = None
        self.headers = {"user-agent": secrets.user_agent}

    def set_featured(self, state):
        if state:
            self.is_featured = True
        else:
            self.is_featured = False

    def set_query(self, query):
        self.query = query

    def url_builder(self):
        if self.is_featured:
            url = self.BASE_URL + f"/featured"
        else:
            url = self.BASE_URL
        url += f"/{self.width}x{self.height}"
        if self.query != None:
            self.query = urllib.parse.quote_plus(self.query)
            url += f"/?{self.query}"
        print(f"url : {url}")
        return url

    def get_image_extension(self):
        return self.download_extension

    def get_download_path(self):
        # find image extension
        self.download_file = "pic1.jpg"
        self.download_extension = ".jpg"

        if "fm=png" in str(self.wallpaper_url):
            self.download_file = self.download_file.replace("jpg", "png")
            self.download_extension = ".png"

        self.download_path = wall.temp_download_dir() + "\\" + self.download_file
        print(self.download_path)
        return self.download_path

    def get_unsplash_pic(self):
        response = requests.get(self.url_builder(), headers=self.headers)
        self.query = None
        if response.status_code == 200:
            self.wallpaper_url = response.url
            print(f"wallpaper_url : {self.wallpaper_url}")

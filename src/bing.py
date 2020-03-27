import requests
import secrets
import random
import wall


class Bing:
    def __init__(self):
        self.BASE_URL = "http://www.bing.com"
        self.WALL_API_URL = "http://www.bing.com//HPImageArchive.aspx?format=js&idx=0&n=8&mkt=en-{country}"
        self.headers = {"user-agent": secrets.user_agent}
        self.country = "init"
        self.prev_wall = ""

    def set_country(self, country):
        if (self.country != country) or (self.country == "init"):
            self.country_specific_wall = True
            self.country = country
        else:
            self.country_specific_wall = False

    def url_builder(self):
        if self.country == "India":
            return self.WALL_API_URL.replace("{country}", "in")
        elif self.country == "US":
            return self.WALL_API_URL.replace("{country}", "us")
        elif self.country == "China":
            self.WALL_API_URL = self.WALL_API_URL.replace("en", "zh")
            return self.WALL_API_URL.replace("{country}", "cn")

    def get_wallpapers(self):
        url = self.url_builder()
        # print(url)
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            limit = 0
            for image in response.json()["images"]:
                limit += 1

            if self.country_specific_wall:
                self.random_index = 0
            else:
                self.random_index = random.randint(1, limit - 1)

            self.wallpaper_url = (
                self.BASE_URL + response.json()["images"][self.random_index]["url"]
            )
            
            if (self.prev_wall == self.wallpaper_url) and (not self.country_specific_wall):
                self.get_wallpapers()
            self.prev_wall = self.wallpaper_url
            print(self.wallpaper_url)

    def get_download_path(self):
        self.download_file = "pic1.jpg"
        self.download_extension = ".jpg"

        if ".png" in str(self.wallpaper_url):
            self.download_file = self.download_file.replace("jpg", "png")
            self.download_extension = ".png"

        self.download_path = wall.temp_download_dir() + "\\" + self.download_file
        # print(self.download_path)
        return self.download_path

    def get_image_extension(self):
        return self.download_extension

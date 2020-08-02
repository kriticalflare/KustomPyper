import random
import secrets
import wall
import requests
import exception_handle


class Wallhaven:
    def __init__(self, width, height):
        self._query = None
        self.__BASE_URL = "https://wallhaven.cc/api/v1/search"
        self._width = str(width)
        self._height = str(height)
        self._prev_wall = ""

    def _build_headers(self):
        headers = {
            "user-agent": secrets.user_agent,
            "X-API-Key": secrets.wallhaven_api_key,
        }
        return headers

    def _build_categories(self):
        _categories = ""
        if self._general:
            _categories = _categories + "1"
        else:
            _categories = _categories + "0"

        if self._anime:
            _categories = _categories + "1"
        else:
            _categories = _categories + "0"

        if self._people:
            _categories = _categories + "1"
        else:
            _categories = _categories + "0"

        return _categories

    def _build_purity(self):
        _purity = ""
        if self._sfw:
            _purity = _purity + "1"
        else:
            _purity = _purity + "0"

        if self._sketchy:
            _purity = _purity + "1"
        else:
            _purity = _purity + "0"

        if self._nsfw:
            _purity = _purity + "1"
        else:
            _purity = _purity + "0"

        return _purity

    def _screen_res(self):
        return self._width + "x" + self._height

    def _build_params(self):
        parameters = {
            "q": self._query,
            "categories": self._build_categories(),
            "purity": self._build_purity(),
            "sorting": self._sort,
            "atleast": self._screen_res(),
        }
        return parameters

    def wallpapers(self):
        response = requests.get(
            self.__BASE_URL, headers=self._build_headers(), params=self._build_params()
        )

        if response.status_code == 200:
            image_count = 0
            for _ in response.json()["data"]:
                image_count += 1
            if image_count == 0:
                raise exception_handle.NoResultsFound()
            else:
                index = random.randint(0, image_count - 1)
                print(image_count)
                print(index)
                image = response.json()["data"][index]
                self._wallpaper_url = image["path"]
                if self._prev_wall == self._wallpaper_url:
                    self.wallpapers()
                self._prev_wall =  self._wallpaper_url
                print(self._wallpaper_url)
                self._image_extension = image["file_type"].replace("image/", ".")
                # print(self._image_extension)

    def get_download_path(self):
        self.download_file = "pic1.jpeg"

        if ".png" in str(self._image_extension):
            self.download_file = self.download_file.replace("jpeg", "png")

        self._download_path = wall.temp_download_dir() + "\\" + self.download_file
        return self._download_path

    @property
    def wallpaper_url(self):
        return self._wallpaper_url

    @wallpaper_url.setter
    def wallpaper_url(self, w):
        pass

    @property
    def image_extension(self):
        return self._image_extension

    @image_extension.setter
    def image_extension(self, i):
        pass

    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, query):
        self._query = query

    @property
    def general(self):
        return self._general

    @general.setter
    def general(self, general):
        self._general = general

    @property
    def anime(self):
        return self._anime

    @anime.setter
    def anime(self, anime):
        self._anime = anime

    @property
    def people(self):
        return self._people

    @people.setter
    def people(self, people):
        self._people = people

    @property
    def sfw(self):
        return self._sfw

    @sfw.setter
    def sfw(self, sfw):
        self._sfw = sfw

    @property
    def sketchy(self):
        return self._sketchy

    @sketchy.setter
    def sketchy(self, sketchy):
        self._sketchy = sketchy

    @property
    def nsfw(self):
        return self._nsfw

    @nsfw.setter
    def nsfw(self, nsfw):
        self._nsfw = nsfw

    @property
    def sort(self):
        return self._sort

    @sort.setter
    def sort(self, sort):
        self._sort = sort


if __name__ == "__main__":
    wallhaven = Wallhaven("1920", "1080")
    wallhaven.general = False
    wallhaven.anime = False
    wallhaven.people = False
    wallhaven.sort = "views"
    wallhaven.sfw = False
    wallhaven.sketchy = False
    wallhaven.nsfw = False
    wallhaven.wallpapers()
    wallhaven.get_download_path()

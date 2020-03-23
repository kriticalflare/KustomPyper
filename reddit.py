import praw
import requests
import random
import secrets
import wall


class Reddit:
    def __init__(self):
        self.instance = praw.Reddit(
            client_id=secrets.reddit_client_id,
            client_secret=secrets.reddit_client_secret,
            user_agent=secrets.user_agent,
        )
        self.query = None
        self.blacklistUrl = ("imgur.com/gallery/", "imgur.com/a/", "v.redd.it")

    def setSubreddit(self, subreddit):
        self.subreddit = subreddit

    def setCategory(self, category):
        self.category = category

    def setLimit(self, limit):
        self.limit = limit

    def setSearchQuery(self, query):
        self.query = query

    def getSearchResults(self):
        self.wallpaper_sub = self.instance.subreddit(self.subreddit)
        return self.wallpaper_sub.search(query=self.query, sort="top", limit=self.limit)

    def getSubmissions(self):
        self.wallpaper_sub = self.instance.subreddit(self.subreddit)
        if self.category == "hot":
            return self.wallpaper_sub.hot(limit=self.limit)
        elif self.category == "top":
            return self.wallpaper_sub.top(limit=self.limit)
        elif self.category == "new":
            return self.wallpaper_sub.new(limit=self.limit)
        elif self.category == "controversial":
            return self.wallpaper_sub.controversial(limit=self.limit)
        elif self.category == "rising":
            return self.wallpaper_sub.rising(limit=self.limit)

    def nextWallpaper(self):
        print(self.subreddit)
        if self.query != None:
            wallpaper_submissions = self.getSearchResults()
            self.query = None
        else:
            wallpaper_submissions = self.getSubmissions()
        submission_list = []
        for submission in wallpaper_submissions:
            submission_list.append(submission)
            # print(submission.title)

        random_int = random.randint(0, self.limit - 1)
        # print(random_int)
        self.submission = submission_list[random_int]
        self.wallpaper_url = submission_list[random_int].url
        print(self.wallpaper_url)
        if any(_ in self.wallpaper_url for _ in self.blacklistUrl):
            #  pass on blacklisted urls (ie not direct image links)
            self.nextWallpaper()

    def downloadPath(self):
        # find image extension
        self.download_file = "pic1.jpg"
        self.download_extension = ".jpg"

        if "png" in str(self.wallpaper_url):
            print("contains")
            self.download_file = self.download_file.replace("jpg", "png")
            self.download_extension = ".png"
            print(self.download_extension)
        self.download_path = wall.temp_download_dir() + "\\" + self.download_file
        return self.download_path

    def getDownloadFile(self):
        return self.download_file

    def getImageExtension(self):
        return self.download_extension

    def getImageTitle(self):
        return self.submission.title

    def downloadWall(self):
        with open(self.download_path, "wb") as handle:

            response = requests.get(self.wallpaper_url, stream=True)

            if not response.ok:
                print(response)

            for block in response.iter_content(1024):
                if not block:
                    break

                handle.write(block)

import praw
import requests
import random
import secrets
import wall
import exception_handle

class Reddit:
    def __init__(self):
        self.instance = praw.Reddit(
            client_id=secrets.reddit_client_id,
            client_secret=secrets.reddit_client_secret,
            user_agent=secrets.user_agent,
        )
        self.query = None
        self.prev_wall = ""
        self.blacklistUrl = ("imgur.com/gallery/", "imgur.com/a/", "v.redd.it")

    def set_subreddit(self, subreddit):
        self.subreddit = subreddit

    def set_category(self, category):
        self.category = category

    def set_limit(self, limit):
        self.limit = limit

    def set_search_query(self, query):
        self.query = query

    def get_search_results(self):
        self.wallpaper_sub = self.instance.subreddit(self.subreddit)
        return self.wallpaper_sub.search(query=self.query, sort="top", limit=self.limit)

    def get_submissions(self):
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

    def next_wallpaper(self):
        print(self.subreddit)
        self.count = 0
        if self.query != None:
            wallpaper_submissions = self.get_search_results()
            self.query = None
        else:
            wallpaper_submissions = self.get_submissions()
        submission_list = []
        for submission in wallpaper_submissions:
            self.count = self.count + 1
            submission_list.append(submission)
            # print(submission.title)

        if self.limit >= self.count:
            self.upperlimit = self.count - 1
        else:
            self.upperlimit = self.limit - 1
        
        if self.upperlimit <= 0:
            self.error_text = "No walls found"
            raise exception_handle.NoResultsFound()
        else:
            self.error_text = ""
            print(self.upperlimit)
            random_int = random.randint(0, self.upperlimit)
            # print(random_int)
            self.submission = submission_list[random_int]
            self.wallpaper_url = submission_list[random_int].url
            print(self.wallpaper_url)
            if any(_ in self.wallpaper_url for _ in self.blacklistUrl):
                #  pass on blacklisted urls (ie not direct image links)
                self.next_wallpaper()
            if self.prev_wall == self.wallpaper_url:
                self.next_wallpaper()
            self.prev_wall = self.wallpaper_url
        
        

    def get_download_path(self):
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

    def get_download_file(self):
        return self.download_file

    def get_image_extension(self):
        return self.download_extension

    def get_image_title(self):
        return self.submission.title

import praw
import requests
import random
import secrets


class Reddit:

    def __init__(self):
        self.instance = praw.Reddit(client_id=secrets.client_id,
                     client_secret=secrets.client_secret,
                     user_agent=secrets.user_agent)

    def nextWallpaper(self):
        wallpaper_sub = self.instance.subreddit('wallpaper')
        wallpaper_hot = wallpaper_sub.hot(limit=25)
        submission_list = []
        for submission in wallpaper_hot:
            submission_list.append(submission.url)

        random_int = random.randint(0,24)
        # print(random_int)
        self.wallpaper_url = submission_list[random_int]
        print(self.wallpaper_url)
        if 'imgur.com/a/' in self.wallpaper_url:
            #  pass on imgur albums for now 
            self.nextWallpaper()

    def download_path(self):
        # find image extension
        self.downloadpath = 'pic1.jpg'

        if 'png' in str(self.wallpaper_url):
            print('contains')
            self.downloadpath = self.downloadpath.replace('jpg', 'png')
            print(self.downloadpath)
        return self.downloadpath
            
        
    def download_wall(self):
        with open(self.downloadpath, 'wb') as handle:
                
                response = requests.get(self.wallpaper_url, stream=True)

                if not response.ok:
                    print(response)

                for block in response.iter_content(1024):
                    if not block:
                        break

                    handle.write(block)
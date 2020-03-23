# KustomPyper
### Get amazing wallpapers from reddit for your Desktop
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![issues](https://img.shields.io/github/issues/kriticalflare/KustomPyper)](https://github.com/kriticalflare/KustomPyper/issues)
[![forks](https://img.shields.io/github/forks/kriticalflare/KustomPyper)](https://github.com/kriticalflare/KustomPyper/network/members)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![GitHub stars](https://img.shields.io/github/stars/kriticalflare/KustomPyper.svg?style=social&label=Star&cacheSeconds=3600)](https://GitHub.com/kriticalflare/KustomPyper/stargazers/)

<img  src="https://user-images.githubusercontent.com/42350771/76681229-dd84c100-6616-11ea-9266-5fa8ab6e20f1.gif" height="280">


GUI tool to get random wallpapers from the subreddit of your choice:

- Choose from default subreddits
- Or even add your own!
- Get wallpapers according to relevance
- Search for wallpapers
- Set the range of random posts
- Toggle Windows dark mode from the app itself!
- Save your favourite walls 

### Built With

* [Python](https://www.python.org/)
* [Praw](https://github.com/praw-dev/praw)
* [PyQt5](https://pypi.org/project/PyQt5/)

## Getting Started

First of all make sure to get your own Reddit client id and secret from https://old.reddit.com/prefs/apps/.

Create a ```secrets.py``` file as shown below with your own client id and secret
```
reddit_client_id = '<client-id>'
reddit_client_secret = '<client-secret>'
user_agent = '<your-useragent>'
```

Now make sure you have installed all the required dependencies, preferrably in a virtual environment.
Run the following commands in the command prompt:
To create a virtual environment
```
python -m venv Venv
```
Now to activate the virtual environment
```
Venv\Scripts\activate.bat
```
Install the requirements
```
pip install -r requirements.txt
``` 
To run the app without building an exe
```
python app.py
```
One can also build the project by 
``` 
 python setup.py bdist_msi
```
 You will find an executable installer in the ```KustomPyper\dist``` folder that can be used to install KustomPyper on the supported platforms
 
## Supported Platforms
- Windows 10 1809 and later

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
[GPL](https://github.com/kriticalflare/KustomPyper/blob/master/LICENSE)

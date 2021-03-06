# KustomPyper
### Get amazing wallpapers from reddit, unsplash , wallhaven and bing for your Desktop
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![issues](https://img.shields.io/github/issues/kriticalflare/KustomPyper)](https://github.com/kriticalflare/KustomPyper/issues)
[![forks](https://img.shields.io/github/forks/kriticalflare/KustomPyper)](https://github.com/kriticalflare/KustomPyper/network/members)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![GitHub stars](https://img.shields.io/github/stars/kriticalflare/KustomPyper.svg?style=social&label=Star&cacheSeconds=3600)](https://GitHub.com/kriticalflare/KustomPyper/stargazers/)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

<img  src="https://user-images.githubusercontent.com/42350771/76681229-dd84c100-6616-11ea-9266-5fa8ab6e20f1.gif" height="280">


GUI tool to get random wallpapers:

- Choose from default subreddits
- Or even add your own!
- Get wallpapers according to relevance
- Search for wallpapers
- Find wallpapers featured by unsplash
- find the best anime walls from wallhaven
- Set the range of random posts
- Get the wallpapers of the day from bing
- Toggle Windows dark mode from the app itself!
- Keep track of the wallpapers you have set before
- Save your favourite walls 

### Built With

* [Python](https://www.python.org/)
* [Praw](https://github.com/praw-dev/praw)
* [PyQt5](https://pypi.org/project/PyQt5/)

## Getting Started

First of all make sure to get your own set of api keys as mentioned [here](#api-key-requirements).

Create a ```secrets.py``` file inside ```KustomPyper\src``` folder as shown below 
```
reddit_client_id = '<client-id>'
reddit_client_secret = '<client-secret>'
user_agent = '<your-useragent>'
wallhaven_api_key = '<your-wallhaven-api-key>'
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
 You will find an executable installer in the ```KustomPyper\src\dist``` folder that can be used to install KustomPyper on the supported platforms
 
## Supported Platforms
- Windows 10 1809 and later

## API Key Requirements
- reddit and wallhaven require your own api keys
  - [reddit](https://old.reddit.com/prefs/apps/)
  - [wallhaven](https://wallhaven.cc/settings/account)
- bing and unsplash dont require keys as of now

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
[GPL](https://github.com/kriticalflare/KustomPyper/blob/master/LICENSE)

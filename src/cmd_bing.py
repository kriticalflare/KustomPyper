import argparse
import bing
import utils
import wall


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("country")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    bing = bing.Bing()
    bing.set_country(args.country)
    bing.get_wallpapers()
    path = bing.get_download_path()
    utils.Helpers.download_wall(path, bing.wallpaper_url)
    wall.changeBG(path)

from datetime import datetime
import requests
import sqlite3


class Helpers:
    @staticmethod
    def download_wall(download_path, download_url):
        with open(download_path, "wb") as handle:

            response = requests.get(download_url, stream=True)

            if not response.ok:
                print(response)

            for block in response.iter_content(1024):
                if not block:
                    break

                handle.write(block)

    @staticmethod
    def saved_wall_path(image_path, image_extension):
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        timestamp = str(int(timestamp))
        return "KustomPyper_" + timestamp + image_extension

    @staticmethod
    def insert_history(wallpaper_url, source):
        try:
            conn = sqlite3.connect("wall_history.db")
            c = conn.cursor()
            c.execute(
                "INSERT OR IGNORE INTO history (wallpaper,source) VALUES (?,?)",
                (wallpaper_url, source),
            )
            conn.commit()
            c.close()
            conn.close()
            return True
        except Exception as e:
            print(e)
            return False

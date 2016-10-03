from .utils import load_file, write_file
from random import choice


class Autoplaylist:
    """
    Autoplaylist manages loading saving urls to play from a file on the harddrive
    """

    def __init__(self, filepath: str, auto_manage: bool = False):
        self.filepath = filepath
        self.urls = load_file(filepath)
        self.auto_manage = auto_manage


    @property
    def has_songs(self):
        return len(self.urls) > 0


    def get_song(self) -> str:
        return choice(self.urls)

    def play_song(self, url: str):
        if self.auto_manage:
            if not url in self.urls:
                self.urls.append(url)
                self.save()

    def skip_song(self, url: str):
        self.remove(url, force_save=self.auto_manage)

    def remove(self, url: str, force_save: bool = False):
        self.urls = [u for u in self.urls if u != url]
        if force_save or self.auto_manage:
            self.save()

    def save(self):
        write_file(self.filepath, self.urls)
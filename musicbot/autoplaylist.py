from .utils import load_file, write_file
from random import choice


class Autoplaylist:
    """
    Autoplaylist manages loading saving urls to play from a file on the harddrive
    """

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.urls = load_file(filepath)


    @property
    def has_songs(self):
        return len(self.urls) > 0


    def get_song(self) -> str:
        return choice(self.urls)


    def remove(self, url: str, force_save: bool = False):
        self.urls = [u for u in self.urls if u != url]
        if force_save:
            self.save()

    def save(self):
        write_file(self.filepath, self.urls)
from PySide2.QtCore import QObject
from .songs_manager import SongsManager

class SongsManagerModel(QObject, SongsManager):
    pass

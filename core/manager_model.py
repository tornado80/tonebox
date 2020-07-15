from PySide2.QtCore import QObject
from .manager import Manager

class Model(QObject, Manager):
    def __init__(self, db_path):
        QObject.__init__(self)
        Manager.__init__(self, db_path)
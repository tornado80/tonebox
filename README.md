# ToneBox a Music Player

This project was first aimed to meet the needs of final project of Adavanced Programming course but could reach amazing points with your contribution to be an advanced user-friendly app.

## Requirements
Only [tinytag](https://pypi.org/project/tinytag) and [PySide2](https://pypi.org/project/PySide2/) together with Python3 are enough for you to listen to ToneBox.

## How to run the project?
You need to just type `python3 main.py` in project directory.

## Features
* Adding songs to library
* Grouping songs for you by Albums, Artists and Genres. Also hierarchical grouping is also possible.
* Managing playlists
* Addings songs to queue and play from it
* Playback rate and fast time seeking
* Songs cover image and details

## What more should be done?
Bugfixes and below options are of paramount importance. 
1. Reordering songs in playlists 
1. Reordering songs in queue
1. Exporting playlists, database

## Design
This project is implemented with Model/View pattern. Views are splitted in **FilterView** and **SongsView** classes in `gui/views.py` which are responsible repectively for viewing categories like albums, artists, etc. and songs TableWidgets. Models are packed in class **Manager** in `core/manager.py` directory. **Model** class in `core/manager_model.py` inherits **Manager** to give it PySide's signals abilities to notify views for changes. **Manager** is responsible for all music files operations and connections to Sqlite database. For example, adding/removing songs to library, adding/removing playlists to library, filtering songs/playlists by categories, adding/removing songs to/from playlists, etc.

## Known Bugs
* Program fails at opening if a music file path available in database file is removed beforehand. (i.e. music file is removed since last session.)

## Contributions
You can use the app and help with feature-requests, bug-reporting, etc. in issues. Of course you can fork and send pull requests and I would be really gratefull of you.

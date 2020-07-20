# ToneBox a Music Player

This project was first aimed to meet the needs of final project of Adavanced Programming course but could reach amazing points with your contribution to be an advanced user-friendly app.

## Requirements
Only [tinytag](https://pypi.org/project/tinytag) and [PySide2](https://pypi.org/project/PySide2/) together with Python3 are enough for you to listen to ToneBox.

## Features
* Adding songs to library
* Grouping songs for you by Albums, Artists and Genres. Also hierarchical grouping is also possible.
* Managing playlists
* Addings songs to queue and play from it
* Playback rate and fast time seeking
* Songs cover image and details

## What more should be done?
[] Reordering songs in playlists 
[] Reordering songs in queue
[] Exporting playlists, database

## Design
This project is implemented with Model/View pattern. Views are splitted in **FilterView**s and **SongsView**s classes in `gui/views.py` which are responsible repectively for viewing categories like albums, artists, etc. and Songs Table Widgets. Models are packed in class **Manager** in `core/manager.py` directory. **Model** in `core/manager_model.py` inherits **Manager** to give it PySide's signals abilities to notify views for changes. **Manager** is responsible for all music files operations and connections to Sqlite database. For example, adding/removing songs to library, adding/removing playlists to library, filtering songs/playlists by categories, adding/removing songs to/from playlists, etc.

## Known Bugs
* Program fails at opening if a music file available in database file is removed. (i.e. music file is removed since last session of program.)

## Contributions
You can use the app and help with feature-requests, bug-reporting, etc. in issues. Of course you can send fork and send pull requests and I would be really gratefull of you.
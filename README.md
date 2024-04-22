# YouTube Downloader

This is a simple Python script for downloading YouTube videos and playlists using the `pytube` library.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo

2. Install the required libraries:
    ```bash
    pip install pytube

# Usage
### Single Video Download
- To download a single video, run the script and choose option '2'. Then enter the video URL when prompted.
    ```bash
    python youtube_downloader.py
    
### Playlist Download
- To download a playlist, run the script and choose option '1'. Then enter the playlist URL when prompted.
    ```bash
    python youtube_downloader.py

## Features
- Download single YouTube videos at the highest resolution.
- Download entire YouTube playlists concurrently (split into 4 threads).

## Program Structure
- youtube_downloader.py: Main script file.

## Author
- [Jetur Gavli](https://www.github.com/jeturgavli)

# License
This project is licensed under the MIT License - see the LICENSE file for details.
from pytube import YouTube, Playlist
from math import ceil
import sys
import threading
import os

# Single Video Downloading
def download_video(url, output_folder):
    try:
        yt = YouTube(url)
        ys = yt.streams.get_highest_resolution()
        filename = ys.download(output_folder)
        print(f"Downloaded: {filename.split('/')[-1]}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")

# handle downloading a playlist
def download_playlist(playlist_url):
    try:
        p = Playlist(playlist_url)
        playlist_name = p.title
        output_folder = os.path.join("output", playlist_name)
        os.makedirs(output_folder, exist_ok=True)

        print("Playlist Name: {}\nChannel Name: {}\nTotal Videos: {}\nTotal Views: {}".format(p.title, p.owner, p.length, p.views))
        links = [url for url in p.video_urls]
    except Exception as e:
        print('Playlist link is not valid.')
        sys.exit(1)

    size = ceil(len(links) / 4)
    link_chunks = list(chunk_list(links, size))

    print("Downloading Started...\n")

    
    def download_chunk(chunk_num):
        for url in link_chunks[chunk_num]:
            download_video(url, output_folder)


    threads = []
    for i in range(4):
        t = threading.Thread(target=download_chunk, args=(i,), name=f'downloader_{i+1}')
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

# Split a list into Chunks
def chunk_list(lst, chunk_size):
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]


def main():
    print("1 For Playlist")
    print("2 For Singl Video ")
    choice = input(":")

    if choice == '1':
        playlist_url = input("Enter Playlist URL: ")
        download_playlist(playlist_url)
    elif choice == '2':
        video_url = input("Enter Video URL: ")
        download_video(video_url, "output")
    else:
        print("Invalid choice. Please enter '1' or '2'.")

if __name__ == "__main__":
    main()

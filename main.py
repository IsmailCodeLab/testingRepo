import youtube_downloader
import file_converter
import logging
import time

print("Welcome to YouTube Downloader and Converter")
print("Loading...")

logging.basicConfig(level=logging.INFO,format="%(levelname)s : %(message)s")
logging.log(level=logging.INFO,msg="""Downloading copyrighted YouTube videos is illegal!
I am not responsible for your downloads! Go at your own risk!""")
time.sleep(2)

print('''
What do you want?

(1) Download YouTube Videos
(2) Download a YouTube Playlist
(3) Download YouTube Videos and Convert Into MP3

''')

choice = input("Choice: ")

if choice == "1" or choice == "2":
    quality = input("Please choose a quality (low(360p), medium(720p), high(1080p), very high(2160p)):")
    if choice == "2":
        link = input("Enter the link of the playlist: ")
        print("Downloading playlist...")
        youtube_downloader.download_playlist(link, quality)
        print("Download finished!")
    if choice == "1":
        links = youtube_downloader.input_links()
        for link in links:
            youtube_downloader.download_video(link, quality)
elif choice == "3":
    links = youtube_downloader.input_links()
    for link in links:
        print("Downloading...")
        filename = youtube_downloader.download_video(link, 'low')
        print("Converting...")
        file_converter.convert_to_mp3(filename)
else:
    print("Invalid input! Terminating...")
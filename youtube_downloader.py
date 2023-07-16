import pytube

def download_video(url, resolution):

    """To download a single Youtube video"""

    itag = choose_resolution(resolution)
    video = pytube.YouTube(url)
    """To get a particular stream based on itag in the available streams for a YouTube video"""
    stream = video.streams.get_by_itag(itag)
    if stream:
        stream.download()
        return stream.default_filename
    else:
        print("Video doesn't have the specified quality")
        print("Available types of quality are:")
        resolutions=[]
        for stream in video.streams:
            resolution=stream.resolution
            if resolution not in resolutions and resolution is not None:
                resolutions.append(resolution)
                print(resolution)
        return None

def download_videos(urls, resolution):
    for url in urls:
        download_video(url, resolution)

def download_playlist(url, resolution):
    """Playlist(url).video_urls : Gives a list of video URLs in the playlist"""
    playlist = pytube.Playlist(url)
    download_videos(playlist.video_urls, resolution)

def choose_resolution(resolution):

    """Video Streams itags:
            18: MP4, 360p, H.264, AAC
            22: MP4, 720p, H.264, AAC
            137: MP4, 1080p, H.264, AAC
            313: WEBM, 2160p, VP9, AAC
    """

    if resolution in ["low", "360", "360p"]:
        itag = 18
    elif resolution in ["medium", "720", "720p", "hd"]:
        itag = 22
    elif resolution in ["high", "1080", "1080p", "fullhd", "full_hd", "full hd"]:
        itag = 137
    elif resolution in ["very high", "2160", "2160p", "4K", "4k"]:
        itag = 313
    else:
        itag = 18
    return itag


def input_links():
    print("Enter the links of the videos (end by entering 'STOP'):")

    links = []
    link = ""

    while link != "STOP" and link != "stop":
        link = input()
        links.append(link)

    links.pop()

    return links
from pytube import YouTube, Playlist

def download(link, path, download_type):
    if download_type == 1:
         YouTube(link).streams.get_by_itag(22).download(output_path=path)
    else:
        playlist = Playlist(link)
        for video in playlist.videos:
            video.streams.get_by_itag(22).download(output_path=path)

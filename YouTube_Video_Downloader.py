"""
Tutorial :https://youtu.be/ZQXd85W3mhs
"""
import pytube
from converter import converter

def Download_Video(url):
    YT_obj = pytube.YouTube(url=url)
    video = YT_obj.streams.get_by_itag('22')
    print("Video is downloading")
    video.download()
    print("Done")
    filename = video.default_filename
    return filename


videos = []

print("Enter STOP keyword to download the videos")

while True:
    url = input()

    if url=='STOP' or url=='stop':
        break
    videos.append(url)

for video in videos:
    file = Download_Video(video)
    converter(file)





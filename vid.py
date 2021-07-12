import pytube
url = 'https://www.youtube.com/watch?v=Qwxz36Hn290&list=RDcHHLHGNpCSA'
youtube = pytube.YouTube(url)
audio=youtube.streams.filter(only_audio=True)
video = youtube.streams.first()
print(video)
video.download()
audio.download()


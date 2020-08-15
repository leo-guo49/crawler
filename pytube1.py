from pytube import YouTube
yt = YouTube('https://www.youtube.com/watch?v=VAWAAifzo6E')
print('start')
yt.streams.first().download()
print('finish')
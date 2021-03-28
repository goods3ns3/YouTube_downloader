import pytube
from pytube.cli import on_progress

url = input("Input playlist's url: ")
playlist = pytube.Playlist(url)
total = len(playlist.video_urls)
print('Total: ' + str(total))
name = playlist.title
counter = 0
for url in playlist:
	video = pytube.YouTube(url, on_progress_callback=on_progress)
	stream = video.streams.get_highest_resolution()
	stream.download(f'C:\\Users\\Workspace\\Downloads\\{name}')
	counter += 1
	print("Video №" + str(counter) + " of " + str(total) + " is ready ")
print('Downloading is done')

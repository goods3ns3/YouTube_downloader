import pytube
from pytube.cli import on_progress


url = input("Input video's url: ")

video = pytube.YouTube(url, on_progress_callback=on_progress)
stream = video.streams.get_highest_resolution()
stream.download('C:\\Users\\Workspace\\Downloads')
print('Done!')

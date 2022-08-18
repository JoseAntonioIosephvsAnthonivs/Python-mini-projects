from pytube import YouTube
import os

yt = YouTube(str(input("Enter the URL of the video you want download: \n >> ")))

video = yt.streams.filter(only_audio=True).first()

#check for destination to save file
print("Enter the destination ( leave blank for current directory)")
destination = str(input(">> ")) or '.'

# download  file
out_file = video.download(output_path= destination)

#save file 
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

#result of sucess
print(yt.title + 'sucessfully downloaded in audio')

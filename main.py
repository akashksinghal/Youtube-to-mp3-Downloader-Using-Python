from youtube_dl import YoutubeDL
ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '/Music/%(title)s.%(ext)s',
        'postprocessors': [
                        {
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                        }
                          ]
            }
files = open('SongsList.txt')
ydl = YoutubeDL(ydl_opts)
for x in files:
    ydl.download([x])        
print("Downloaded All Songs")

# Developed By Akash Kumar Singhal
# https://www.github.com/akashksinghal
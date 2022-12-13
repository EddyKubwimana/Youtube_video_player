import vlc
import urllib.request
import re
import pafy


user = input("Enter the name of the song you want to play")
user_list = user.split(" ")
user = ""
for i in user_list:
    user = user+i
link = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={user}")
videos_id = re.findall(r'watch\?v=(\S{11})', link.read().decode())

# url of the video
url = "https://youtu.be/"+videos_id[0]

# creating pafy object of the video
video = pafy.new(url)

# getting best stream
best = video.getbest()
# creating vlc media player object


media = vlc.MediaPlayer(best.url)

media.play()

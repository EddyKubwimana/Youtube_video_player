from tkinter import*
import urllib.request
import re
import pafy
import vlc

class youtubeplayer:

    def __init__(self, window, Instance):

        self.window = window
        self.Instance = Instance
        self.player = self.Instance.media_player_new()
        self.window.title('Youtube Player')
        self.window.geometry("925x500+100+3")
        self.window.configure(bg ="#fff")
        self.window.resizable(True, True)
        self.frame = Frame(self.window, width = 900, height = 400)
        self.frame.pack(fill = "both", expand =1, padx = 10, pady = 60)
        self.video_name = Entry(self.window,width = 80 , bg = "light gray",border = 0, fg = "black", font = ( "Microsoft Yahei UI Light", 12))
        self.video_name.place(x = 10, y = 10)
        self.button =Button( self.window, width = 10, height= 1, pady = 2, text = "Search", bg = "#57a1f8", fg = "white", border = 0,font = ( "Microsoft Yahei UI Light", 8),
                             command = self.playvideo)
        self.button.place( x = 670, y = 10)
        self.button1 =Button( self.window, width = 10, height= 1, pady = 2, text = "stop", bg = "#57a1f8", fg = "white", border = 0,font = ( "Microsoft Yahei UI Light", 8))
        self.button1.place(x = 500, y = 760)
        self.button2 =Button( self.window, width = 10, height= 1, pady = 2, text = "play", bg = "#57a1f8", fg = "white", border = 0,font = ( "Microsoft Yahei UI Light", 8))
        self.button2.place(x = 600, y = 760)
        self.button3 = Button( self.window, width = 10, height= 1, pady = 2, text = "stop", bg = "#57a1f8", fg = "white", border = 0,font = ( "Microsoft Yahei UI Light", 8))
        self.button3.place(x = 700, y = 760)
        self.size = self.frame.winfo_id()
    
    def playvideo(self):
        self.user = self.video_name.get()
        self.user_list = self.user.split(" ")
        self.user = ""
        for i in self.user_list:
            self.user = self.user+i
        self.link = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={self.user}")
        self.videos_id = re.findall(r'watch\?v=(\S{11})', self.link.read().decode())

        # url of the video
        self.url = "https://youtu.be/"+self.videos_id[0]

        # creating pafy object of the video
        self.video = pafy.new(self.url)

        # getting best stream
        self.best = self.video.getbest()
        # creating vlc media player object
        self.Media = self.Instance.media_new(self.best.url)
        self.player.set_hwnd(self.size)
        self.player.set_media(self.Media)
        self.player.play()

Instance = vlc.Instance()
window = Tk()           
vid = youtubeplayer(window, Instance)
    




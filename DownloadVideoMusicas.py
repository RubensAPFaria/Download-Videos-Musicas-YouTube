from tkinter import Frame, Label, LabelFrame, Entry, Button, Tk, LEFT, messagebox, END, RIGHT, HORIZONTAL
from tkinter.filedialog import askopenfilenames
from tkinter.ttk import Progressbar
from pytube import YouTube
import os
#from moviepy.editor import *
from moviepy.audio.io.AudioFileClip import AudioFileClip, AudioClip
import proglog



class MyApp:
    def __init__(self,master=None):

        
        self.container = Frame(master)
        self.container.pack(fill="both", expand="yes")
        self.container1 = Frame(master)
        self.container1.pack(fill="both", expand="yes")
        self.container2 = Frame(master)
        self.container2.pack(fill="both", expand="yes")
        self.container3 = Frame(master)
        self.container3.pack(fill="both", expand="yes")
        self.container4 = Frame(master)
        self.container4.pack(fill="both", expand="yes")
        


               

        self.tituloFrame = Label(self.container, text="Baixar Vídeos e Músicas do YouTube")
        self.tituloFrame.pack()

        self.byRubens = Label(self.container3, text="By Rubens Augusto")
        self.byRubens.pack(side=RIGHT)

        #self.progressBar = Progressbar(self.container3,orient=HORIZONTAL, mode="determinate")
        #self.progressBar.pack(side=LEFT, ipadx=100)

        self.grupoAudio = LabelFrame(self.container1, text="Audio")
        self.grupoAudio.pack(fill="both", expand="yes", padx=5)
        
        self.linkAudio = Entry(self.grupoAudio)
        self.linkAudio.focus()
        self.linkAudio.pack(side=LEFT, ipadx=100, padx=5)
        
        self.buttonAudio = Button(self.grupoAudio, text="Baixar Audio", command=self.download_Audio)
        self.buttonAudio.pack(padx=5, pady=5)

        self.grupoVideo = LabelFrame(self.container1, text="Video")
        self.grupoVideo.pack(fill="both", expand="yes", padx=5)
        
        self.linkVideo = Entry(self.grupoVideo)
        self.linkVideo.pack(side=LEFT, ipadx=100, padx=5)
        
        self.buttonVideo = Button(self.grupoVideo, text="Baixar Video", command=self.download_Video)
        self.buttonVideo.pack(padx=5, pady=5)

        self.grupoConverte = LabelFrame(self.container1, text="Converte")
        self.grupoConverte.pack(fill="both", expand="yes")

        self.buttonConverte = Button(self.grupoConverte, text="Converter para MP3", command=self.convert)
        self.buttonConverte.pack(fill="both",expand="yes", padx=5, pady=5)
    
    def download_Audio(self):
        yt_link = self.linkAudio.get()
        try:
            if yt_link == '' or yt_link == None:
                messagebox.showerror(f"Aviso","Campo Vazio")
            else:
                path_audio = 'C:/Temp/Musicas'
                
                yt = YouTube(yt_link)
                audio = yt.streams.filter(only_audio=True)[0]
                
                mp4_file = audio.download(path_audio)
                mp3_file = audio.default_filename[:-4]+".mp3"
                
                videoClip = AudioFileClip(mp4_file, fps = 44100)
                audioclip = videoClip
                audioclip.write_audiofile(path_audio +'/'+mp3_file, fps = 44100)

                os.remove(path_audio + '/' + audio.default_filename)
                
                videoClip.close()
                audioclip.close()

                messagebox.showinfo(f"Aviso","Download Completo!")
                self.linkAudio.delete(0,END)
        except:
            messagebox.showerror(f"Erro","Arquivo invalido para Download!")


    def download_Video(self):
        path_video = 'C:\Temp\Videos'

        try:
            yt_link = self.linkVideo.get()
            if yt_link == '' or yt_link == None:
                messagebox.showerror(f"Aviso","Campo Vazio")
            else:
                yt = YouTube(yt_link)
                yt.streams.filter()[0].download(path_video)
                messagebox.showinfo(f"Aviso","Download Completo!")
                self.linkVideo.delete(0,END)
        except:
            messagebox.showerror(f"Erro","Arquivo invalido para fazer Download!")

    
    def convert(self):
        audio = askopenfilenames()

        try:
            for num in audio:
                mp4_file = num
                mp3_file = mp4_file[:-4]+".mp3"

                musica = AudioFileClip(mp4_file,fps = 44100)
                audioClip = musica
                audioClip.write_audiofile(mp3_file,fps = 44100, logger="bar")               
                

                if num[:-4]+".mp4" == num:
                    os.remove(num)

                musica.close()
                audioClip.close()
                messagebox.showinfo(f"Aviso","Convertido para MP3 com sucesso!")
        except:
            
            messagebox.showerror(f"Erro","Arquivo invalido para converter!")




    

root = Tk()
root.title("Baixar Vídeos e Músicas do YouTube")
root.resizable(width=0, height=0)
MyApp(root)
root.mainloop()

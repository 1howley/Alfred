import customtkinter as tk
from tkinter import *

class ScreenMain():
    def createScreen(fun):

        global texto
        global verifica
        verifica = False

        def actionFace():
            window.update()
            global texto 
            texto = None
            global verifica
            verifica = True
            window.destroy()
        
        def actionPlay():
            btnImgPlay.configure(image=None, text="GRAVANDO!", font=("Roboto", 30), background_corner_colors=None)
            btnImgPlay.place(x=250, y=420)
            window.update()
            global texto 
            texto = fun()
            global verifica
            verifica = True
            window.destroy()

        darkgrey = "#272727"

        tk.set_appearance_mode("dark")
        tk.set_default_color_theme("green")

        window = tk.CTk()
        window.geometry("700x500")
        window.title("Alfred")
        window.iconbitmap("assets/alfredo.ico")
        window.resizable(False, False)

        imgSound = PhotoImage(file="assets/sound.png")
        labelImgSound = tk.CTkLabel(master=window, image=imgSound, text=None)
        labelImgSound.place(x=350-128, y=250-128)

        imgFace = PhotoImage(file="assets/face.png")
        topFrame = tk.CTkFrame(master=window, width=700, height=100, fg_color=darkgrey)
        topFrame.pack(side=TOP)
        btnImgFace = tk.CTkButton(master=window, image=imgFace, text=None, fg_color=darkgrey, command=actionFace, background_corner_colors=None, width=80, hover=False)
        btnImgFace.place(x=350-32, y=16)

        imgPlay = PhotoImage(file="assets/play.png")
        lowFrame = tk.CTkFrame(master=window, width=700, height=100, fg_color=darkgrey)
        lowFrame.pack(side=BOTTOM)
        btnImgPlay = tk.CTkButton(master=window, image=imgPlay, text=None, fg_color=darkgrey, command=actionPlay, background_corner_colors=None, width=80, hover=False)
        btnImgPlay.place(x=350-32, y=415)

        window.mainloop()

        return texto, verifica

import customtkinter as tk
from tkinter import *

class ScreenMain():
    def createScreen(fun):

        global texto

        def action():
            btnImgPlay.configure(image=None, text="GRAVANDO!", font=("Roboto", 30), background_corner_colors=None)
            btnImgPlay.place(x=250, y=420)
            window.update()
            global texto 
            texto = fun()

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

        topFrame = tk.CTkFrame(master=window, width=700, height=100, fg_color=darkgrey)
        topFrame.pack(side=TOP)

        imgPlay = PhotoImage(file="assets/play.png")
        lowFrame = tk.CTkFrame(master=window, width=700, height=100, fg_color=darkgrey)
        lowFrame.pack(side=BOTTOM)
        btnImgPlay = tk.CTkButton(master=window, image=imgPlay, text=None, fg_color=darkgrey, command=action, background_corner_colors=None, width=80, hover=False)
        btnImgPlay.place(x=350-32, y=415)

        window.mainloop()

        return texto

import customtkinter as tk
import pyperclip
from tkinter import *

class ScreenResult:

    def createScreen(content):
        
        global boolean
        boolean = True
        global text

        def turnTrue():
            global boolean
            boolean = True
            window.destroy()

        def copyFun():
            pyperclip.copy(content)
        def send():
            global boolean
            boolean = False
            global text
            text = inputUser.get()
            window.destroy()
        
        darkgrey = "#272727"

        tk.set_appearance_mode("dark")
        tk.set_default_color_theme("green")

        window = tk.CTk()
        posix = window.winfo_screenwidth()/2 - 1100/2
        posiy = window.winfo_screenheight()/2 - 700/2
        window.geometry("%dx%d+%d+%d" % (1100, 700, posix, posiy))
        window.title("Alfred's Answer")
        window.iconbitmap("assets/alfredo.ico")
        window.resizable(False, False)

        #imgs
        imgSend = PhotoImage(file="assets/send.png")
        imgCopy = PhotoImage(file="assets/copy.png")
        imgAudio = PhotoImage(file="assets/mic.png")

        scrollableFrame = tk.CTkScrollableFrame(master=window, fg_color=darkgrey, height=600, width=1000)
        scrollableFrame.pack(side=TOP)

        aswerLabel = tk.CTkLabel(
            master=scrollableFrame,
            width=1000,
            height=300,
            fg_color=darkgrey,
            text_color='white',
            font=("Roboto", 20),
            text=content,
            anchor="center",
            compound="center",
            wraplength=1000
        )
        aswerLabel.pack()


        #working with low frame
        lowFrame = tk.CTkFrame(master=window, width=1100, height=100, fg_color=darkgrey)
        lowFrame.pack(side=BOTTOM)
        btnImgCopy = tk.CTkButton(master=window, image=imgCopy, text=None, fg_color=darkgrey, command=copyFun, background_corner_colors=None, width=80)
        btnImgCopy.place(x=100-32, y=650-16)
        btnImgMic = tk.CTkButton(master=window, image=imgAudio, text=None, fg_color=darkgrey, command=turnTrue, background_corner_colors=None, width=80)
        btnImgMic.place(x=1000-32, y=650-16)
        btnImgSend = tk.CTkButton(master=window, image=imgSend, text=None, fg_color=darkgrey, command=send, background_corner_colors=None, width=80)
        btnImgSend.place(x=800+32, y=650-16)

        inputUser = tk.CTkEntry(master=window, placeholder_text="Sua mensagem", width=600, height=50, font=("Roboto", 14))
        inputUser.place(x=200, y=625)

        window.mainloop()

        return boolean, text

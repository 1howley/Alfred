import customtkinter as tk
from tkinter import *

class ScreenResult:

    def createScreen():
        def test():
            print(inputUser.get())
        
        darkgrey = "#272727"

        tk.set_appearance_mode("dark")
        tk.set_default_color_theme("green")

        window = tk.CTk()
        window.geometry("1100x700")
        window.title("Alfred's Answer")
        window.iconbitmap("assets/alfredo.ico")
        window.resizable(False, False)

        #imgs
        imgSend = PhotoImage(file="assets/send.png")
        imgCopy = PhotoImage(file="assets/copy.png")
        imgAudio = PhotoImage(file="assets/mic.png")

        #working with low frame
        lowFrame = tk.CTkFrame(master=window, width=1100, height=100, fg_color=darkgrey)
        lowFrame.pack(side=BOTTOM)
        btnImgCopy = tk.CTkButton(master=window, image=imgCopy, text=None, fg_color=darkgrey, command=test, background_corner_colors=None, width=80, hover=False)
        btnImgCopy.place(x=0, y=600+14)

        inputUser = tk.CTkEntry(master=window, placeholder_text="Sua mensagem", width=600, height=50, font=("Roboto", 14))
        inputUser.place(x=200, y=625)


        window.mainloop()
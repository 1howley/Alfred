import customtkinter as tk
from tkinter import *

class ScreenResult:

    def createScreen(content):
        
        global boolean
        boolean = False

        def turnTrue():
            global boolean
            boolean = True
            window.destroy()

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

        scrollableFrame = tk.CTkScrollableFrame(master=window, fg_color=darkgrey, height=600, width=1000)
        scrollableFrame.pack(side=TOP)

        # Create a text widget with vertical scrollbar
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
        btnImgCopy = tk.CTkButton(master=window, image=imgCopy, text=None, fg_color=darkgrey, command=test, background_corner_colors=None, width=80, hover=False)
        btnImgCopy.place(x=0, y=600+14)
        btnImgMic = tk.CTkButton(master=window, image=imgAudio, text=None, fg_color=darkgrey, command=turnTrue, background_corner_colors=None, width=80, hover=False)
        btnImgMic.place(x=1000, y=600+14)

        inputUser = tk.CTkEntry(master=window, placeholder_text="Sua mensagem", width=600, height=50, font=("Roboto", 14))
        inputUser.place(x=200, y=625)

        window.mainloop()

        return boolean

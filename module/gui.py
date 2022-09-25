import tkinter as tk
from PIL import ImageTk, Image
import cv2 as cv
class Gui:
    def __init__(self, win):
        
        self.win = win
        self.win.title("Attend") 
        self.win.geometry("655x530")

        self.frm = tk.Frame(self.win, bg="white", width=640, height=480) # 프레임 너비, 높이 설정
        self.frm.grid(row=0, column=0) # 격자 행, 열 배치

        self.lbl = tk.Label(self.frm)
        self.lbl.grid()

        self.resultLabel = tk.Label(self.win, 
            width=50,
            height=2,
            font=("", "20"),
            foreground='white',
            background='red'
        )
        self.resultLabel.grid(row=1, column=0)

    def printResult(self, color, message):
        self.resultLabel['background'] = color
        self.resultLabel['text'] = message

    def printImage(self, frame):
        frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        self.lbl.imgtk = imgtk
        self.lbl.configure(image=imgtk)
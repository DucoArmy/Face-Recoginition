import tkinter as tk
from PIL import ImageTk, Image
import cv2 as cv

import sys

sys.path.append('./module/')
from comparer import Comparer
from resultManager import ResultManager
from networkManager import NetworkManager
from gui import Gui

faces = [
    "yjm",
    "kkh",
    "chg",
    "hjb",
    "ljm",
    "sung",
    "suzzing",
    "psh",
    "kyr",
    "csi",
    "jsw",
    "gjh",
    "mini",
    "lsh"
]

# faces = [
#     "kkh",
# ]

class Main:
    def __init__(self):
        self.comparer = Comparer(faces)
        self.resultManager = ResultManager(5)
        self.networkManager = NetworkManager(faces)
        self.capture = cap = cv.VideoCapture(0)
        self.capture.set(cv.CAP_PROP_FRAME_WIDTH, 640)
        self.capture.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

        self.win = tk.Tk() 
        self.gui = Gui(self.win)

        self.update()
        self.win.mainloop()


    def update(self):
        ret, frame = self.capture.read() 
        if not ret:
            self.capture.release() 
            return
        self.gui.printImage(frame)
        result = self.comparer.compare(frame)
        print(result)
        if self.resultManager.push(result):
            if(result == Comparer.undefined or result == Comparer.noMatch):
                self.gui.printResult("red", "")
            else:
                self.gui.printResult("green", result)
        self.win.after(10, self.update)


main = Main()
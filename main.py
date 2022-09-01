import tkinter as tk
from PIL import ImageTk, Image
import cv2 as cv
import sys
sys.path.append('./module/')
from comparer import Comparer

faces = [
    "kkh",
    "chg"
]


win = tk.Tk() # 인스턴스 생성
win.title("Attend") # 제목 표시줄 추가
win.geometry("920x640") # 지오메트리: 너비x높이+x좌표+y좌표

frm = tk.Frame(win, bg="white", width=720, height=480) # 프레임 너비, 높이 설정
frm.grid(row=1, column=0) # 격자 행, 열 배치

lbl = tk.Label(frm)
lbl.grid()

comparer = Comparer(faces)
cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 320)

def video_play():
    ret, frame = cap.read() 
    if not ret:
        cap.release() 
        return
    print(comparer.compare(frame))
    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    img = Image.fromarray(frame)
    imgtk = ImageTk.PhotoImage(image=img)

    lbl.imgtk = imgtk
    lbl.configure(image=imgtk)
    lbl.after(10, video_play)
    

video_play()
win.mainloop()
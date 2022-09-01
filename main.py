import tkinter as tk
from PIL import ImageTk, Image
import cv2 as cv
import sys
sys.path.append('./module/')
from comparer import Comparer
from resultManager import ResultManager

faces = [
    "kkh",
    "chg"
]


win = tk.Tk() # 인스턴스 생성
win.title("Attend") # 제목 표시줄 추가
win.geometry("655x530") # 지오메트리: 너비x높이+x좌표+y좌표

frm = tk.Frame(win, bg="white", width=640, height=480) # 프레임 너비, 높이 설정
frm.grid(row=0, column=0) # 격자 행, 열 배치

lbl = tk.Label(frm)
lbl.grid()

resultLabel = tk.Label(win, 
    width=50,
    height=2,
    font=("", "20"),
    foreground='white',
    background='red'
)
resultLabel.grid(row=1, column=0)

comparer = Comparer(faces)
resultManager = ResultManager(10)
cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

def video_play():
    ret, frame = cap.read() 
    if not ret:
        cap.release() 
        return
    
    result = comparer.compare(frame)
    
    if resultManager.push(comparer.compare(frame)):
        if(result == Comparer.undefined or result == Comparer.noMatch):
            resultLabel['background'] = "red"
            resultLabel['text'] = ""
        else:
            resultLabel['background'] = "green"
            resultLabel['text'] = result


    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    img = Image.fromarray(frame)
    imgtk = ImageTk.PhotoImage(image=img)

    lbl.imgtk = imgtk
    lbl.configure(image=imgtk)
    lbl.after(40, video_play)
    

video_play()
win.mainloop()


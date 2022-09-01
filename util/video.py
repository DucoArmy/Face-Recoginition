import cv2

vidcap = cv2.VideoCapture('./chg.mp4')
success,image = vidcap.read()
count = 1

while success:
    cv2.imwrite("./image/kkh%d.jpg" % count, image)
    success,image = vidcap.read()
    count += 1
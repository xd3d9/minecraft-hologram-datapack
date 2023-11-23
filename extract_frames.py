import cv2
import time
vidcap = cv2.VideoCapture('yoasobi.mp4')
success,image = vidcap.read()

count = 0
frame_rate = 30
prev = 0

total_frames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))

while success:
    time_elapsed = time.time() - prev
    res, image = vidcap.read()
    if time_elapsed > 1./frame_rate:
        prev = time.time()
        cv2.imwrite("frames/frame%d.png" % count, image) 
        success,image = vidcap.read()
        print(f"{count} frames")
        count += 1
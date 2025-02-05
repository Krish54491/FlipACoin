#import cv2
#import random
#import numpy as np
#from ffpyplayer.player import MediaPlayer
#
#
#rand = random.randint(1,2)
#
#if(rand == 1):
#    cap = cv2.VideoCapture('You underestimate my power + I have the high ground.mp4')
#else:
#    cap = cv2.VideoCapture('Hello there + General Kenobi.mp4')
#if (cap.isOpened()== False):
#    print("Error opening video file")
#
#while(cap.isOpened()):
#    
## Capture frame-by-frame
#    ret, frame = cap.read()
#    if ret == True:
#    # Display the resulting frame
#        cv2.imshow('Frame', frame)
#        
#    # Press Q on keyboard to exit
#        if cv2.waitKey(25) & 0xFF == ord('q'):
#            break
#
## Break the loop
#    else:
#        break
#
## When everything done, release
## the video capture object
#cap.release()
#
## Closes all the frames
#cv2.destroyAllWindows()
import cv2
import numpy as np
import random
#ffpyplayer for playing audio
from ffpyplayer.player import MediaPlayer
def PlayVideo1(video_path):
    video=cv2.VideoCapture(video_path)
    player = MediaPlayer(video_path)
    while True:
        grabbed, frame=video.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(20) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    video.release()
    cv2.destroyAllWindows()

def PlayVideo2(video_path):
    video=cv2.VideoCapture(video_path)
    player = MediaPlayer(video_path)
    while True:
        grabbed, frame=video.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            #print("End of video")
            break
        if cv2.waitKey(11) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    video.release()
    cv2.destroyAllWindows()

rand = random.randint(1,2)

if(rand == 1):
    video_path = 'Heads.mp4'
    PlayVideo1(video_path)
    print("Heads")
else:
    video_path = 'Tails.mp4'
    PlayVideo2(video_path)
    print("Tails")


cv2.destroyAllWindows()
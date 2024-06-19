import cv2
from moviepy.editor import VideoFileClip
import random

video_paths = [
    "./motion/videos/3209828-uhd_3840_2160_25fps.mp4",
    "./motion/videos/SampleVideo_1280x720_2mb.mp4", 
    "./motion/videos/5538262-hd_1920_1080_25fps.mp4", 
    "./motion/videos/SampleVideo_1280x720_1mb.mp4"    
    ]



def play_video(): 
    
    selected_video = random.choice(video_paths)
    clip = VideoFileClip(selected_video)
    
    cap = cv2.VideoCapture(selected_video)

    if not cap.isOpened():
        print("Error: Could not open video.")
        exit()
        
    cv2.namedWindow('Video', cv2.WINDOW_NORMAL)
    # Set the window to full screen
    cv2.setWindowProperty('Video', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('Video', frame)

        if cv2.waitKey(int(1000 / clip.fps)) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    
    
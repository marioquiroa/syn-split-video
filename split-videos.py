#libraries
import cv2

#input variables
FOLDER_FRAMES = 'OriginalFrames'
VIDEO_NAME = 'cut.mp4'
LAG = 1000
IX_FRAME = 0
CUT_EVERY = 5

#object instance
vidcap = cv2.VideoCapture(VIDEO_NAME)

#get fps
FPS = vidcap.get(cv2.CAP_PROP_FPS)

#Relative position of the video file: 0 - start of the film, 1 - end of the film.
vidcap.set(cv2.CAP_PROP_POS_AVI_RATIO,1)
#Current position of the video file in milliseconds or video capture timestamp
LENGTH = vidcap.get(cv2.CAP_PROP_POS_MSEC)

#re - object instance
vidcap = cv2.VideoCapture(VIDEO_NAME)

#read
success,imageFrame = vidcap.read()
#output log
print ('Frames: '),

while success:
    #output log numbers
    if (IX_FRAME%100==0):
        print(IX_FRAME),
    
    if (IX_FRAME%FPS < CUT_EVERY):
        # save frame as JPEG file      
        cv2.imwrite(FOLDER_FRAMES + "/%d.jpg" % (IX_FRAME + LAG), imageFrame)     
    
    #read again
    success,image = vidcap.read()

    #counter increase
    IX_FRAME += 1
    
print ('.')
print 'Total Frames: ' + str(IX_FRAME) + ' - FPS: ' + str(FPS) + ' - Duration: ' + str(LENGTH/1000) + ' sec.'
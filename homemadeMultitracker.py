import blobDetect as bd
import trackerFunc as tf
import cv2 as cv
#import NewTracker as nt

class NewTracker():                     #constructor
    def __init__(self):
        self.trackers = []              #makes a list that should contain all trackers

    def add(self, trackerObj):          #method for adding trackers
        self.trackers.append(trackerObj) 

    def pop(self, ind):                 #method for removing tracker
        if ind > len(self.trackers) or ind <0: 
            pass
        else:
            self.trackers.pop(ind)
            
    def update(self, frame):            #method to update multitracker
        boxes = []
        notValid = []
        for idx, el in enumerate(self.trackers):
            retval, box = el.update(frame)
            if retval == True:          #checks if tracker managed to track
                boxes.append(box)       #continues to track if valid
            else:
                notValid.append(idx)    #nonvalid tracker are added to the list
        if len(notValid) > 0:              
            for num in notValid:
                self.pop(num)           #all nonvalid trackers are removed
        return boxes
        

trackerType = "KCF"                 #choosing trackertype
multiTracker = NewTracker()         #making newTracker object
bboxes = []

cap = cv.VideoCapture('vtest.avi')

while(cap.isOpened()):
    #print(len(multiTracker.trackers))
    ret, frame = cap.read()                                     #read frames
    boxes = multiTracker.update(frame)
    if cv.waitKey(0) == ord('s'):
        newBox = cv.selectROI('MultiTracker', frame)
        print(newBox)
        bboxes.append(newBox)
        multiTracker.add(tf.createTrackerByName(trackerType))   #add tracker to multitracker
        ok = multiTracker.trackers[len(multiTracker.trackers)-1].init(frame, newBox)    #initialise the new tracker
        
    elif cv.waitKey(0) == ord("r"):
        try:
            multiTracker.pop(0)                                 #remove first tracker in multitracker
        except:
            pass
    try:
        for i, box in enumerate(boxes):                         #draw all trackers
            p1 = (int(box[0]), int(box[1]))
            p2 = (int(box[0] + box[2]), int(box[1] + box[3]))
            cv.rectangle(frame, p1, p2, (0,0,255), 2, 1)
    except:
        pass
    cv.imshow('MultiTracker', frame)
    if cv.waitKey(0) == 27:
        break


cv.destroyAllWindows()

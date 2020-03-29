import blobDetect as bd
import trackerFunc as tf
import cv2 as cv
#import NewTracker as nt

class NewTracker():                     #constructor
    def __init__(self):
        self.trackers = []              #makes a list that should contain all trackers
        self.trackerFail = []           #list to see how many frames a tracker has been nonvalid

    def add(self, trackerObj):          #method for adding trackers
        self.trackers.append(trackerObj)
        self.trackerFail.append(0)      #also needs to see how many frames it has been nonvalid

    def pop(self, ind):                 #method for removing tracker
        if ind > len(self.trackers) or ind <0: 
            pass
        else:
            self.trackers.pop(ind)      #remove tracker and
            self.trackerFail.pop(ind)   #everything related to it
            
    def update(self, frame):            #method to update multitracker
        boxes = []
        for idx, el in enumerate(self.trackers):
            retval, box = el.update(frame)
            if retval == True:          #checks if tracker managed to track
                boxes.append(box)       #continues to track if valid
                self.trackerFail[idx] = 0   #if track was sucsessful trackerFail is zero
            else:
                self.trackerFail[idx] +=1
        for idx, fails in enumerate(self.trackerFail):  
            if fails > 5:               #needs to iterate throug list of tracker
                self.pop(idx)           #to see how long they have been wrong
        return boxes                    #list of boxes so they can be drawn on the frame
        

trackerType = "KCF"                 #choosing trackertype
multiTracker = NewTracker()         #making newTracker object
bboxes = []

cap = cv.VideoCapture('vtest.avi')

while(cap.isOpened()):
    print(len(multiTracker.trackers))
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

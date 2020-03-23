import blobDetect as bd
import trackerFunc as tf
import cv2 as cv
import NewTracker as nt

class NewTracker(cv.MultiTracker):
    def _init_(self):
        self.create()

    def remove(self,box):
        self.objects.remove(box) 

    def pop(self,index):
        self.objects.pop(index)


trackerType = "KCF"
#multiTracker = cv.MultiTracker_create()
NewTracker = NewTracker.create()
bboxes = []

cap = cv.VideoCapture('vtest.avi')
#ret, frame = cap.read()
while(cap.isOpened()):
    ret, frame = cap.read()
    success, boxes = NewTracker.update(frame)
    if cv.waitKey(0) == ord('s'):
        newBox = cv.selectROI('MultiTracker', frame)
        print(newBox)
        print(type(newBox))
        bboxes.append(newBox)
        NewTracker.add(tf.createTrackerByName(trackerType), frame, newBox)
    if cv.waitKey(0) == ord("r"):
        NewTracker.pop(0)
    for i, box in enumerate(boxes):
        p1 = (int(box[0]), int(box[1]))
        p2 = (int(box[0] + box[2]), int(box[1] + box[3]))
        cv.rectangle(frame, p1, p2, (0,0,255), 2, 1)
    cv.imshow('MultiTracker', frame)
    if cv.waitKey(0) == 27:
        break


cv.destroyAllWindows()

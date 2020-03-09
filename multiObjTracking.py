import blobDetect as bd
import trackerFunc as tf
import cv2

trackerType = "KCF"
multiTracker = cv2.MultiTracker_create()
bboxes = []

cap = cv2.VideoCapture('vtest.avi')
#ret, frame = cap.read()
while(cap.isOpened()):
    ret, frame = cap.read()
    success, boxes = multiTracker.update(frame)
    if cv2.waitKey(0) == ord('s'):
        newBox = cv2.selectROI('MultiTracker', frame)
        print(newBox)
        print(type(newBox))
        bboxes.append(newBox)
        multiTracker.add(tf.createTrackerByName(trackerType), frame, newBox)
    for i, box in enumerate(boxes):
        p1 = (int(box[0]), int(box[1]))
        p2 = (int(box[0] + box[2]), int(box[1] + box[3]))
        cv2.rectangle(frame, p1, p2, (0,0,255), 2, 1)
    cv2.imshow('MultiTracker', frame)
    if cv2.waitKey(0) == 27:
        break


cv2.destroyAllWindows()

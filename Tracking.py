import cv2

def KeypointsToBoxes(keypoints):
    boxes = []
    for keypoint in keypoints:
        point = keypoint.pt
        size = int(keypoint.size)
        box = (int(point[0])- (size),int(point[1]) - (size),2.75*size,2.75*size)
        boxes.append(box)
    return boxes

def removeTrackedBlobs(keypoints, boxes):
    newKeypoints = []
    oldKeypoints = []
    #print(keypoints)
    diff = []
    try:
        for points in keypoints:
            x = points.pt[0]
            y = points.pt[1]
            for box in boxes:
                xb,yb,wb,hb = box
                if xb<x and x<xb+wb and yb<y and y<yb+hb:
                    diff.append(points)
        for point in keypoints:
            if point not in diff:
                newKeypoints.append(point)
            else:
                oldKeypoints.append(point)
    except:
        pass
    return newKeypoints, oldKeypoints

if __name__ == "__main__":
    pass
def makePoint(bbox):
    p1 = (int(bbox[0]) + int(bbox[1]))*0.5
    p2 = (int(bbox[2]) + int(bbox[3]))*0.5
    return [p1,p2]

bbox=(1,1,4,4)
print(makePoint(bbox))
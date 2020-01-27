import cv2

redLower = (0,10,10)                                                            #100,130,50 skal være for å filtrere rød farge
redUpper = (80,255,255)                                                         #200,200,130

def redProsessFrame(frame):
    frame = cv2.resize(frame, (650,500))                        #reskalerer for vindu, fungerer ikke som planlagt (endre pixler)
    
    #blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    #frame = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(frame, redLower, redUpper)               #har ingen anelse hvordan mask opplegget fungerer, men det må til for å filterer bort alt fra bildet
    mask = cv2.erode(mask, None, iterations=0)                  #som ikke er rødt
    mask = cv2.dilate(mask, None, iterations=0) 
    
    maskedFrame = cv2.bitwise_and(frame,frame,mask = mask)            #dette gir et rart bilde
    
    (thres, thresFrame) = cv2.threshold(maskedFrame, 190, 255, cv2.THRESH_BINARY)  #men med å gjøre dette får man svart-rødt bilde
    
    invertedFrame = 255 -thresFrame                                         #her inverteres svart rødt bilde (detector-funksjonen detekterer mørke objekt på lys bakgrunn, dette kan endres though)
    
    grayFrame = cv2.cvtColor(invertedFrame, cv2.COLOR_BGR2GRAY)             #gjør bildet om til gråskala

    (thres, finishedFrame) = cv2.threshold(grayFrame, 190, 255, cv2.THRESH_BINARY)  #her bruker man en treshold så man får bilder i svart-hvitt

    return finishedFrame

if __name__ == "__main__":
    print("you're in the wrong place man")
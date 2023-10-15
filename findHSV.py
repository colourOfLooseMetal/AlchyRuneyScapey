import cv2
import sys
import numpy as np


def nothing(x):
    pass


# Load in image
image = cv2.imread('./mf5.png')


def findHSV_UI(image, type):
    # Create a window
    cv2.namedWindow('image')

    # create trackbars for color change
    cv2.createTrackbar('HMin', 'image', 0, 179, nothing)  # Hue is from 0-179 for Opencv
    cv2.createTrackbar('SMin', 'image', 0, 255, nothing)
    cv2.createTrackbar('VMin', 'image', 0, 255, nothing)
    cv2.createTrackbar('HMax', 'image', 0, 179, nothing)
    cv2.createTrackbar('SMax', 'image', 0, 255, nothing)
    cv2.createTrackbar('VMax', 'image', 0, 255, nothing)

    # Set default value for MAX HSV trackbars.
    cv2.setTrackbarPos('HMax', 'image', 179)
    cv2.setTrackbarPos('SMax', 'image', 255)
    cv2.setTrackbarPos('VMax', 'image', 255)

    # Initialize to check if HSV min/max value changes
    hMin = sMin = vMin = hMax = sMax = vMax = 0
    phMin = psMin = pvMin = phMax = psMax = pvMax = 0

    if type == "ironUM":
        print("eh")
        cv2.setTrackbarPos('HMin', 'image', 8)
        cv2.setTrackbarPos('SMin', 'image', 113)
        cv2.setTrackbarPos('VMin', 'image', 25)
        cv2.setTrackbarPos('HMax', 'image', 16)
        cv2.setTrackbarPos('SMax', 'image', 158)
        cv2.setTrackbarPos('VMax', 'image', 95)

    output = image
    wait_time = 33

    while (1):

        # get current positions of all trackbars
        hMin = cv2.getTrackbarPos('HMin', 'image')
        sMin = cv2.getTrackbarPos('SMin', 'image')
        vMin = cv2.getTrackbarPos('VMin', 'image')

        hMax = cv2.getTrackbarPos('HMax', 'image')
        sMax = cv2.getTrackbarPos('SMax', 'image')
        vMax = cv2.getTrackbarPos('VMax', 'image')

        # Set minimum and max HSV values to display
        lower = np.array([hMin, sMin, vMin])
        upper = np.array([hMax, sMax, vMax])

        # Create HSV Image and threshold into a range.
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower, upper)
        output = cv2.bitwise_and(image, image, mask=mask)

        # Print if there is a change in HSV value
        if ((phMin != hMin) | (psMin != sMin) | (pvMin != vMin) | (phMax != hMax) | (psMax != sMax) | (pvMax != vMax)):
            print("np.array([%d , %d, %d]), np.array([%d , %d, %d])" % (hMin, sMin, vMin, hMax, sMax, vMax))
            phMin = hMin
            psMin = sMin
            pvMin = vMin
            phMax = hMax
            psMax = sMax
            pvMax = vMax
            print("cv2.setTrackbarPos('HMin', 'image', ", hMin, ")")
            print("cv2.setTrackbarPos('SMin', 'image', ", sMin, ")")
            print("cv2.setTrackbarPos('VMin', 'image', ", vMin, ")")
            print("cv2.setTrackbarPos('HMax', 'image', ", hMax, ")")
            print("cv2.setTrackbarPos('SMax', 'image', ", sMax, ")")
            print("cv2.setTrackbarPos('VMax', 'image', ", vMax, ")")

        # Display output image
        cv2.imshow('image', output)

        # Wait longer to prevent freeze for videos.
        if cv2.waitKey(wait_time) & 0xFF == ord('q'):
            return([hMin, sMin, vMin], [hMax, sMax, vMax])

    cv2.destroyAllWindows()

if __name__ == '__main__':
    findHSV_UI(image, None)

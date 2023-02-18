# https://towardsdatascience.com/computer-vision-for-beginners-part-1-7cca775f58ef

import cv2
import numpy as np

dir = '/Users/swagam/Documents/Projects/ImageProcessing/Color_Draw/'

##########################
### Draw Circle on Map ###
##########################

# # Step 1. Define callback function
# def draw_circle(event, x, y, flags, param):
#     if event == cv2.EVENT_LBUTTONDOWN:
#             cv2.circle(img, center = (x, y), radius = 50, 
#                        color = (87, 184, 237), thickness = -1)
#     elif event == cv2.EVENT_RBUTTONDOWN:        
#             cv2.circle(img, center = (x, y), radius = 100,  
#                        color = (87, 184, 237), thickness = 1)

# # Step 2. Call the window
# img = cv2.imread(dir + 'map.jpg')
# cv2.namedWindow(winname = 'my_drawing')
# cv2.setMouseCallback('my_drawing', draw_circle)


# # Step 3. Execution
# while True:
#     cv2.imshow('my_drawing',img)
#     if cv2.waitKey(10) & 0xFF == 27:
#         break
# cv2.destroyAllWindows()



#########################
### Draw Rect. on Map ###
#########################


# Step 1. Define callback function
drawing = False
ix = -1
iy = -1

def draw_rectangle(event, x, y, flags, params):

    global ix, iy, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
        
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img, pt1 = (ix, iy), pt2 = (x, y), 
                          color = (87, 184, 237), thickness = -1)
            
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, pt1 = (ix, iy), pt2 = (x, y), 
                      color = (87, 184, 237), thickness = -1)
        
    
# Step 2. Call the window
img = cv2.imread(dir + 'map.jpg')

cv2.namedWindow(winname = 'my_drawing')
cv2.setMouseCallback('my_drawing', draw_rectangle)


# Step 3. Execution 
while True: 
    cv2.imshow('my_drawing', img)
    if cv2.waitKey(10) & 0xFF == 27:
        break

cv2.destroyAllWindows()

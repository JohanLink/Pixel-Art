import cv2
import sys
import numpy as np

input = cv2.imread(sys.argv[1])

height, width = input.shape[:2]

w, h = (int(sys.argv[3]), int(sys.argv[3]))

image = cv2.resize(input, (w, h), interpolation=cv2.INTER_LINEAR)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

for i in range(0, h):
    for j in range(0, w):

        value = gray[i,j]

        if value <= 51:
            image[i,j] = [56,110,32]           # github's dark green
        elif value > 51 and value <= 102:
            image[i,j] = [78,161,47]           # github's medium-dark green
        elif value > 102 and value <= 153:
            image[i,j] = [100,196,65]          # github's medium green
        elif value > 153 and value <= 204:
            image[i,j] = [168,233,155]         # github's medium-light green
        elif value > 204 and value <= 255:
            image[i,j] = [240,237,235]         # github's light green

width, height = 1000, 1000

output = cv2.resize(image, (width, height), interpolation=cv2.INTER_NEAREST)

for i in range(1, w):
    cv2.line(output, (int(i*width/w), 0), (int(i*width/w), height), (255, 255, 255), thickness=1)
for i in range(1, h):
    cv2.line(output, (0, int(i*height/h)), (width, int(i*height/h)), (255, 255, 255), thickness=1)


#cv2.imshow('Output', output)

folder = sys.argv[2] + "/"

cv2.imwrite(folder+"output"+str(w)+"x"+str(h)+".jpg", output)

#cv2.waitKey(0)
#cv2.destroyAllWindows()

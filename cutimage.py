import cv2
import numpy as np

class CheckboxReader:

    def __init__(self):
        #queue to hold 20 images after main function runs
        self.image_queue = []
        # array of arrays to hold coordinaters of 20 rectangles
        self.coordinates = []
        # for loop to append all rectangles axis arrays into coordinates array above
        for count in range (0,21):
            a = [150,178,45,500]
            b = [179,337,45,345]
            c = [179,362,345,640]
            d = [179,408,640,896]
            e = [179,408,896,1225]
            f = [338,362,45,353]
            g = [363,386,45,429]
            h = [387,410,45,353]
            i = [642,671,45,354]
            j = [642,671,355,641]
            k = [671,715,355,641]
            l = [671,715,641,896]
            m = [671,715,896,1225]
            n = [748,1126,45,354]
            o = [748,773,896,1225]
            p = [773,1126,896,1225]
            q = [1126,1153,45,1225]
            r = [1154,1317,355,641]
            s = [1154,1317,641,896]
            t = [1154,1317,896,1225]
            u = [1598,1624,45,1225]
            alphabet = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u]
            idx = alphabet[count]
            self.coordinates.append(idx)
    
    # use this function to test if image_queue array holds images after main function is run -- will delete later run on line 62
    def showPictures(self, num):
        cv2.imshow("cropped", self.image_queue[num])
        cv2.waitKey(0)

    # main function that reads image, runs crop and appends to image_queue array
    def main(self, y):
        img = cv2.imread(y)
        for i in range (0,21):
            top = self.coordinates[i][0]
            bottom = self.coordinates[i][1]
            left = self.coordinates[i][2]
            right = self.coordinates[i][3]
            crop_img = img[top:bottom, left:right]
            # uncomment this code, if you want to see what every image looks like as this function runs
            # cv2.imshow("cropped", crop_img)
            # cv2.waitKey(0)
            self.image_queue.append(crop_img)


x = CheckboxReader()
x.main("courtwatch.jpg")

# run this function to test if the queue intitialized in image_queue actually stores the images
# x.showPictures(0)






##for initializing and changing x,y axises for rectanlges
##format y1,y2,x1,x2 OR top, bottom, left, right

# a = [150,178,45,500]
# b = [179,337,45,345]
# c = [179,362,345,640]
# d = [179,408,640,896]
# e = [179,408,896,1225]
# f = [338,362,45,353]
# g = [363,386,45,429]
# h = [387,410,45,353]
# i = [642,671,45,354]
# j = [642,671,355,641]
# k = [671,715,355,641]
# l = [671,715,641,896]
# m = [671,715,896,1225]
# n = [748,1126,45,354]
# o = [748,773,896,1225]
# p = [773,1126,896,1225]
# q = [1126,1153,45,1225]
# r = [1154,1317,355,641]
# s = [1154,1317,641,896]
# t = [1154,1317,896,1225]
# u = [1598,1624,45,1225]

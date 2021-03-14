import pycda
from pycda.sample_data import get_sample_image
import PySimpleGUI as sg
from pycda import load_image
import numpy as np
import cv2 

class Detection:

    def helper(self):
        # Making The Blank Image
        image = cv2.imread(self.getImageToDraw())
        #image = cv2.imread('/home/user1/Desktop/Capstone/BeerMartianCrater.jpg')
        drawing = False
        ix = 0
        iy = 0
    
        # Adding Function Attached To Mouse Callback
    def draw(self,event,x,y,flags,params):
        self.helper()
        dt = crater.Detection()
        global ix,iy,drawing, image
        # Left Mouse Button Down Pressed
        if(event==1):
            drawing = True
            ix = x
            iy = y
        if(event==0):
            if(drawing==True):
                #For Drawing Line
                cv2.line(image,pt1=(ix,iy),pt2=(x,y),color=(255,255,255),thickness=3)
                ix = x
                iy = y
                # For Drawing Rectangle
                # cv2.rectangle(image,pt1=(ix,iy),pt2=(x,y),color=(255,255,255),thickness=3)
        if(event==4):
            drawing = False



    def openDraw(self):
        # Making Window For The Image
        cv2.namedWindow("Window")

        # Adding Mouse CallBack Event
        cv2.setMouseCallback("Window",self.draw())

        # Starting The Loop So Image Can Be Shown
        while(True):

            cv2.imshow("Window",image)

            if cv2.waitKey(20) & 0xFF == ord('q'):
                break

        cv2.destroyAllWindows()


    def showImage(self):
        image = get_sample_image()
        #image.show()
        cda = pycda.CDA()
        prediction = cda.get_prediction(image, verbose = True)
        prediction.show()
    
    def getImage(self):
        try:

            layout = [  [sg.Text('Filename')],
                [sg.Input(), sg.FileBrowse(key="-IN-")], 
                [sg.OK(), sg.Exit()]] 

            window = sg.Window('Get filename', layout)

            event, values = window.read()
            window.close()

            if event == 'Exit':
                window.close()
            else:

                image = load_image(values["-IN-"])
                cda = pycda.CDA()
                prediction = cda.get_prediction(image, verbose = True)
                prediction.show()
                prediction.to_csv('/home/user1/Desktop/Capstone/results.csv')
        except:
            print()
        
    def getImageToDraw(self):
        layout = [  [sg.Text('Filename')],
            [sg.Input(), sg.FileBrowse()], 
            [sg.OK(), sg.Cancel()]] 

        window = sg.Window('Get filenameT', layout)

        event, values = window.read()
        print(values['Browse'])
        value = values['Browse']
        print(value)
        #return value
        window.close()
        return value

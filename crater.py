import pycda
from pycda.sample_data import get_sample_image
import PySimpleGUI as sg
from pycda import load_image

class Detection:
    def showImage(self):
        image = get_sample_image()
        #image.show()
        cda = pycda.CDA()
        prediction = cda.get_prediction(image, verbose = True)
        prediction.show()
    
    def getImage(self):
        layout = [  [sg.Text('Filename')],
            [sg.Input(), sg.FileBrowse(key="-IN-")], 
            [sg.OK(), sg.Cancel()]] 

        window = sg.Window('Get filename', layout)

        event, values = window.read()
        window.close()

        image = load_image(values["-IN-"])
        cda = pycda.CDA()
        prediction = cda.get_prediction(image, verbose = True)
        prediction.show()
"""
import PySimpleGUI as sg
sg.theme("DarkTeal2")
layout = [[sg.T("")], [sg.Text("Choose a file: "), sg.Input(), sg.FileBrowse(key="-IN-")],[sg.Button("Submit")]]

###Building Window
window = sg.Window('My File Browser', layout, size=(600,150))
    
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event=="Exit":
        break
    elif event == "Submit":
        print(values["-IN-"])"""
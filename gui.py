import PySimpleGUI as sg
import crater

dt = crater.Detection()

import PySimpleGUI as sg

"""def getFilePath():
    #sg.theme('Dark Blue 3')  # please make your creations colorful

    layout = [  [sg.Text('Filename')],
            [sg.Input(), sg.FileBrowse()], 
            [sg.OK(), sg.Cancel()]] 

    window = sg.Window('Get filename', layout)

    event, values = window.read()
    window.close() """

def func():
    print("Hola")

layout = [[sg.Text('To run crater detection, press the open image and run prediction buttonn')],
          [sg.Button('Open Image and Run Prediction'), sg.Button('Detect on Sample Image'), sg.Exit()] ]

window = sg.Window('Crater Detector', layout, font=("Roboto", 12), size=(1000, 400), finalize=True)

while True:             # Event Loop
    event, values = window.Read()
    if event in (None, 'Exit'):
        break
    if event == 'Open Image and Run Prediction':
        dt.getImage()
    elif event == 'Detect on Sample Image':
        dt.showImage()
window.Close()
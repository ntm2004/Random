# -*- coding: utf-8 -*-


import PySimpleGUI as sg

import random

for i in range(1):
    value = random.randint(1, 100)
    

layout = [[sg.Text(value)], [sg.Button("OK")]]

# Create the window
window = sg.Window("Random", layout, margins=(100, 50))

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()


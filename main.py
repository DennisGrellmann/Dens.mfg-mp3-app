import PySimpleGUI as sg

# All the stuff inside your window.
layout = [  [sg.Text("Sync your mp3 files to the sd card!")],
            [sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel'), sg.Button('Popup')] ]

# Create the Window
window = sg.Window('MP3 App', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == 'Popup':
        sg.popup("Hello universe...I'm a 1-line GUI program!")


    # if user closes window or clicks cancel
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    print('Hello', values[0], '!')

window.close()

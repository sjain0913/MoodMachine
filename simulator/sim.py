import PySimpleGUI as sg

mainMenuColumn = [
    [
        sg.Text("MoodMachine"),
    ],
    [
        sg.Button("Prerecorded Speech Analysis"),
    ],
    [
        sg.Button("Analyze Mic Speech"),
    ],
    [
        sg.Button("Prerecorded Speech Transcript"),
    ],
    [
        sg.Button("Quit")
    ]
]

layout = [
    [
        sg.Column(mainMenuColumn)
    ]
]
window = sg.Window("MoodMachine", layout)

while True:
    event, values = window.read()
    if event == "Quit" or event == sg.WIN_CLOSED:
        break
    
window.close()
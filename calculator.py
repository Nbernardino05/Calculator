# This program is a simple GUI-based calculator using PySimpleGUI that performs basic arithmetic operations 
# Users can interact with buttons to input numbers and operators, and the result is displayed dynamically in the input field.

import PySimpleGUI as sg    # imports PySimpleGUI library

# Defines the layout of the GUI with buttons & an input text box
number = [[sg.Button("1"),sg.Button("2"),sg.Button("3")],
    [sg.Button("4"),sg.Button("5"),sg.Button("6")],
    [sg.Button("7"),sg.Button("8"),sg.Button("9"),sg.Button("0")],
    [sg.Button("-"),sg.Button("+"),sg.Button("/"),sg.Button("x"),sg.Button("=")],
    [sg.InputText("", size=(15,1), key='-OUTPUT-')]]

# Create the window
window = sg.Window('Calculator', number)

# Function to perform the calculation based on user input
def calculate(values):
    operators = ['+','-', 'x', '/']
    usedOp = ''
    
    # Identify the operator used in the input 
    for operator in operators:
        index = values.find(operator)
        if index != -1:
            usedOp = operator
    
    # Split the input string into numbers based on the operator
    numbers = values.split(usedOp)
    answer = 0

    # Dictionary mapping operators to corresponding functions
    opDict = {
        '+': add,
        '-': subtract,
        'x': multiply,
        '/': divide,
    }

    answer = opDict[usedOp](int(numbers[0]), int(numbers[1])) # performs operation
    return str(answer)

# Functions to perform basic arithmetic operations
def multiply(number1, number2):
    return number1 * number2
def divide(number1, number2):
    return number1 // number2
def add(number1, number2):
    return number1 + number2
def subtract(number1, number2):
    return number1 - number2

# Event loop to process user interactions with the GUI
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: # checks if window is closed
        break
    
    # Handle button presses 
    if isinstance(event, str):
        if event == ("="):  
            print (values['-OUTPUT-'])
            window['-OUTPUT-'].update(calculate(values['-OUTPUT-']))
            continue
        # Update the input display with the pressed button's value
        print (values)
        window['-OUTPUT-'].update(values['-OUTPUT-']+event)

window.close()

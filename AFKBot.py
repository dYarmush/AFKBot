import pyautogui as pag
import keyboard
import random
import time
from tkinter import *

root = Tk()

root.title('AFK Bot')
root.geometry('300x140')
global onOff
onOff = True
global typing
global label
global counter_display
counter_display = StringVar()

counter_display.set('Timer: 0')
curr_coords = pag.position()
afk_counter = 0


def on_key_press(key_pressed):
    key_pressed[0] = True


key_pressed = [False]


def afkrun():
    keyboard.on_press(lambda event: on_key_press(key_pressed))

    global onOff
    global curr_coords
    global afk_counter
    global counter_display
    if onOff:
        if pag.position() == curr_coords and not key_pressed[0]:
            afk_counter += 1
            # counter_display.set(afk_counter)
            counter_display.set(f'Timer: {afk_counter}')
            root.update_idletasks()
        else:
            afk_counter = 0
            counter_display_reset()
            curr_coords = pag.position()
            key_pressed[0] = False
        try:
            if afk_counter > input_verify():
                x = random.randint(600, 700)
                y = random.randint(200, 600)
                pag.moveTo(x, y, 0.5)
                curr_coords = pag.position()
        except TypeError:
            pass

        root.after(100, afkrun)
        time.sleep(1)


def input_verify():
    try:
        input_value = int(myTextBox.get())
        return input_value
    except ValueError:
        global label
        label = Label(root, text="Input only numbers!", fg='Red')
        root.geometry('300x155')
        label.pack()


def turn_on():
    global onOff
    onOff = True
    afkrun()


def turn_off():
    global onOff
    onOff = False
    counter_display_reset()


def counter_display_reset():
    counter_display.set('Timer: 0')
    root.update_idletasks()


myLabel = Label(root, text='Input how long to wait before running the program')
myLabel.pack()

myTextBox = Entry(root, width=30)
myTextBox.pack()

timer = Label(root, textvariable=counter_display)
timer.pack()

myStartButton = Button(root, text='Click to start program', command=turn_on)
myStartButton.pack()

myEndButton = Button(root, text='Click to End program', command=turn_off)
myEndButton.pack()

exitButton = Button(root, text='Exit', command=exit)
exitButton.pack()

root.mainloop()

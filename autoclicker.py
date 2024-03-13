import pyautogui
import time
import keyboard
import pyinputplus as pyip

print('Ctl activates clicking')
print('Space opens click duration input')
print('esc stops program')
active = False;
duration = 3.5

def on_enter(e):
    global active
    if(active == False):
            print(f'\nactive')
            active = True;
    elif(active == True):
            print(f'\nnot active')
            active = False;

def on_esc(e):
    print("ESC key pressed. Exiting...")
    exit()

def on_space(e):
    global duration
    print('Input duration between clicks')
    duration = pyip.inputFloat()
    print('\nnew duration is: ' + str(duration))

keyboard.on_press_key("ctrl", on_enter)
keyboard.on_press_key("space", on_space)
keyboard.on_press_key("esc", on_esc)

while True:
    time.sleep(duration)
    if(active == True):
        print('click')
        pyautogui.click(button='left')



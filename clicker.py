import time
import keyboard

FPS = 24
isRunning = False
clicker_list = []
print("Press space bar to start ")
keyboard.wait('space')
while True:
    if keyboard.is_pressed('left'):
        clicker_list.append("True")
        print("True")
    elif keyboard.is_pressed('right'):
        clicker_list.append("False")
        print("False")
    else:
        clicker_list.append("Neutral")
        print("Neutral")
    time.sleep(1/FPS)
    if keyboard.is_pressed('esc'):
        break 

print(len(clicker_list))
    

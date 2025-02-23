import pyautogui
import time
print('==================================================================================================================')
print('SpeedLabs Copy Toolkit')
print('By HJ')
print('Github: https://github.com/Harshu1000-7')
print('to use this script, open Speedlabs Test Or Practice session on chrome Or Current Session, where you want  to copy       un-copyable text for easier search, like practice or test window')
print(' ')
print('Then Click this window(command prompt), and click chrome and alt-tab to this window')
print('To check if everything is set-up, doing alt-tab will switch between you from this window(command prompt) and chrome')
print('You have to return to this window after everything works, and start the program ')
print(' ')
print('Tutorial: ')
print('AND DO NOT PRESS ANYTHING WHEN YOU HAVE STARTED THE PROGRAM')
print('==================================================================================================================')
print('Start[1]')
print('Help[2]')
print('YoutubeTutorial[3]')
print('Exit[4]')
x = input('Input 1 2 3 or 4 and Press Enter: ')
if x == '4':
    print('Bye')

if x == '3':
    print('Copy This Link: ')
    print('and this window will close in 10 seconds, to run it start again after seeing tutorial')
    time.sleep(5)

if x == '2':
    print('open cmd and type: pip install pyautogui')
    time.sleep(1)
    print('and this window will close in 10 seconds, to run it start again after doing pip install pyautogui')
    time.sleep(9)
if x == '1':
    time.sleep(3)  #
    pyautogui.hotkey("alt", "tab")
    time.sleep(1)
    pyautogui.hotkey("ctrl", "shift", "i")
    time.sleep(2) 
    pyautogui.click(1496, 420)
    time.sleep(1) 
    js_code = "document.querySelectorAll('*').forEach(el => el.style.userSelect = 'text');"
    pyautogui.typewrite(js_code, interval=0.05)  
    pyautogui.press("enter")
    pyautogui.hotkey("ctrl", "shift", "i")
    print("Script executed Successfully")
    print('it will only work as long as you have not refreshed the page')
    print('Exiting Program...')

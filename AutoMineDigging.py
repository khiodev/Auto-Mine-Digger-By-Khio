import time
import threading
from pynput.mouse import Controller, Button, Listener
from pynput.keyboard import Listener, KeyCode , Key, Controller as keyboardController
import keyboard
import random
import colorama
from colorama import Fore

TOGGLE_KEY = KeyCode(char="q")
colorama.init(autoreset=True)
clicking = False
mouse = Controller()
keyboardControl = keyboardController()
pressedOnce = False

minePos1 = ...
minePos2 = ...
minePos3 = ...
minePos4 = ...
minePos5 = ...
minePos6 = ...

print(f"{Fore.LIGHTGREEN_EX}Welcome To Auto Mine Digging For Club Penguin Private Servers Made By Khio")

print(f"{Fore.LIGHTCYAN_EX}Press 1 to mark you're first position.")
while True:

    if keyboard.is_pressed("1"):
            minePos1 = mouse.position
            print(f"1st Position: {minePos1}")
            break
print(f"{Fore.LIGHTCYAN_EX}Press 2 to mark you're first position.")
while True:
    if keyboard.is_pressed("2"):

            minePos2 = mouse.position
            print(f"2nd Position: {minePos2}")
            break

print(f"{Fore.LIGHTCYAN_EX}Press 3 to mark you're first position.")
while True:
    if keyboard.is_pressed("3"):
            minePos3 = mouse.position
            print(f"3rd Position: {minePos3}")
            break
    
print(f"{Fore.LIGHTCYAN_EX}Press 4 to mark you're first position.")
while True:
    if keyboard.is_pressed("4"):
            minePos4 = mouse.position
            print(f"4th Position: {minePos4}")
            break

print(f"{Fore.LIGHTCYAN_EX}Press 5 to mark you're first position.")
while True:
    if keyboard.is_pressed("5"):
            minePos5 = mouse.position
            print(f"5th Position: {minePos5}")
            break
    
print(f"{Fore.LIGHTCYAN_EX}Press 6 to mark you're first position.")
while True:
    if keyboard.is_pressed("6"):
            minePos6 = mouse.position
            print(f"6th Position: {minePos6}")
            break

print(f"{Fore.LIGHTGREEN_EX}Press Q to turn on/off the hack")

def hack():
    while True:
        if clicking:
            randomMinePosList = [minePos1,minePos2,minePos3,minePos4,minePos5,minePos6]
            randomMousePosValue = random.choice(randomMinePosList)
            mouse.position = (randomMousePosValue)
            mouse.click(Button.left,1)
            time.sleep(3)
            keyboard.press('d')
            time.sleep(15)
            randomMousePosValue = random.choice(randomMinePosList)
            mouse.position = (randomMousePosValue)
            mouse.click(Button.left,1)
            time.sleep(3)
            keyboard.press('d')
        time.sleep(15)
def toggle_event(key):
    if key == TOGGLE_KEY:
        global clicking
        clicking = not clicking


click_thread = threading.Thread(target=hack)
click_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()
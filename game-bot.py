import sched, time
import pyautogui
import random

schedProcess = sched.scheduler(time.time, time.sleep)

def PressKey(process):

    pyautogui.press('t')
    pyautogui.typewrite('/balik tut',interval=0.10)
    pyautogui.press('enter')

    schedProcess.enter(random.randint(6,15), 1, PressKey, (process,))

schedProcess.enter(10, 1, PressKey, (schedProcess,))
schedProcess.run()

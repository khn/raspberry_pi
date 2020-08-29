import maestro
import time
import keyboard

servo = maestro.Controller()
servo.runScriptSub(1)
time.sleep(.5)
servo.runScriptSub(2)
time.sleep(1.5)
#servo.setAccel(2,0)
servo.runScriptSub(0)
servo.close
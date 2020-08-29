import maestro
import time

servo = maestro.Controller()
time.sleep(3)
servo.runScriptSub(0)

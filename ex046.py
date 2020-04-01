#contagem regressiva para queima de fogos de artificio
from time import sleep
import playsound
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('0')
playsound.playsound('ex46fireworks.mp3')
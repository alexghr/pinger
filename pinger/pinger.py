from asyncio import get_event_loop
from ping import ping
import display

loop = get_event_loop()

IP = "1.1.1.1"
DELAY = 10

tick_num = 0
def tick():
    global tick_num
    tick_num += 1

    res = ping(IP)
    display.render(tick_num, res, IP)
    loop.call_later(DELAY, tick)

try:
    tick()
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    display.close()
    loop.close()
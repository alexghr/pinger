from asyncio import get_event_loop
from ping import ping
import display
from store import Store
from config import IP, DELAY

loop = get_event_loop()

store = Store()

def tick():
    res = ping(IP)
    store.update(res)

    display.render(store.state())

    loop.call_later(DELAY, tick)

try:
    tick()
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    display.close()
    loop.close()
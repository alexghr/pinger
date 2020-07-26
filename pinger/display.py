from PIL import Image, ImageDraw, ImageFont
import ST7789

from store import State
from config import IP

disp = ST7789.ST7789(
    port=0,
    cs=ST7789.BG_SPI_CS_FRONT,  # BG_SPI_CSB_BACK or BG_SPI_CS_FRONT
    dc=9,
    backlight=19,               # 18 for back BG slot, 19 for front BG slot.
    spi_speed_hz=80 * 1000 * 1000
)

font_main = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
font_sec = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 18)

img = Image.new('RGB', (disp.width, disp.height), color=(0, 0, 0))
draw = ImageDraw.Draw(img)

x = 8

def render(state: State):
    draw.rectangle((0, 0, disp.width, disp.height), (0, 0, 0))

    render_title(state)
    render_status(state)
    render_recent_fail(state)

    disp.display(img)

def render_title(state: State):
    font = font_sec
    y = 8
    title = f"Pinging {IP}"
    draw.text((x, y), title, font=font, fill=(255, 255, 255))

def render_status(state: State):
    font = font_main
    y = 48
    count = (
        f"Pinged {state.total_pings()}\n"
        f"OK {state.count_ok}\n"
        f"Failed {state.count_fail}"
    )

    draw.text((x, y), count, font=font, fill=(255, 255, 255))

def render_recent_fail(state: State):
    if state.count_recent_fail == 0:
        return

    font = font_sec
    y = 136

    recent_fail = f"FAIL x{state.count_recent_fail}"
    draw.text((x, y), recent_fail, font=font, fill=(255, 0, 0))

def close():
    disp.reset()
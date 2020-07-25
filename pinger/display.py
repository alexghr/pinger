from PIL import Image, ImageDraw, ImageFont
import ST7789

disp = ST7789.ST7789(
    port=0,
    cs=ST7789.BG_SPI_CS_FRONT,  # BG_SPI_CSB_BACK or BG_SPI_CS_FRONT
    dc=9,
    backlight=19,               # 18 for back BG slot, 19 for front BG slot.
    spi_speed_hz=80 * 1000 * 1000
)

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 32)
img = Image.new('RGB', (disp.width, disp.height), color=(0, 0, 0))
draw = ImageDraw.Draw(img)

def render(tick_num, res, ip):
    msg = "{}\nping #{} {}".format(ip, tick_num, "OK" if res else "FAIL")

    draw.rectangle((0, 0, disp.width, disp.height), (0, 0, 0))

    draw.text((0, 0), msg, font=font, fill=(255, 255, 255))
    disp.display(img)

def close():
    disp.reset()
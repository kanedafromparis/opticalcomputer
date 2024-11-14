import board
import neopixel
from time import sleep

# This function lihght up the led board in green on by one with a pace of 0.05 sec
def fill_in_square(pixels):
    pixels.fill( (0, 0, 0))
    sleep(0.05)
    pixels.show()
    for item in range(0, 64, 1):
        led = item
        print(item)
        pixels[item]=(0,20,0)
        sleep(0.05)
        print("change led0")
        pixels.show()


if __name__ == "__main__":
    pixels = neopixel.NeoPixel(board.D18, 64)
    print("init")
    fill_in_square(pixels)
    sleep(0.30)
    pixels.fill( (0, 0, 0))
    print("stop")

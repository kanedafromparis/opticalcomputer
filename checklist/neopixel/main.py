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

# This function lihght up the led board in green on by one with a pace of 0.05 sec
def fill_led_with_calib_light(pixels):
    pixels.fill( (0, 0, 0))
    sleep(0.05)
    pixels.show()
    pixels[0]=(10,0,0)
    pixels[7]=(10,10,0)
    pixels[27]=(0,10,0)
    pixels[28]=(0,0,10)
    pixels[35]=(10,10,0)
    pixels[36]=(10,0,0)
    pixels[56]=(0,0,10)
    pixels[63]=(0,10,0)
    sleep(0.30)

if __name__ == "__main__":
    pixels = neopixel.NeoPixel(board.D18, 64)
    print("init")
    pixels.fill( (0, 0, 0))
    display = input("select display [0,1] : ")
    if (display == "0"):
        fill_in_square(pixels)
    if (display == "1"):
        fill_led_with_calib_light(pixels)
    sleep(0.30)
    pixels.fill( (0, 0, 0))
    print("stop")

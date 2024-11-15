from PIL import Image, ImageDraw 
import RPi.GPIO as GPIO
from spidev import SpiDev
from time import sleep
import third_party.ILI9486 as LCD
import legacy.config as config
import random
import numpy as np
import board
import neopixel

from picamzero import Camera
import datetime
# from calculator.Calculator import Calculator


class LCD_Controller:
    def __init__(self, spi:SpiDev)->None:
        self.lcd_size = (480, 320)
        self.spi = spi
        self.spi.mode = 0b10
        self.spi.max_speed_hz = 64000000

        self.lcd = LCD.ILI9486(dc=5, rst=6, spi=self.spi).begin()
        self.lcd = LCD.ILI9486(dc=config.DC_PIN, rst=config.RST_PIN, spi=spi).begin()
        print(f'Initialized display with landscape mode = {self.lcd.is_landscape()} and dimensions {self.lcd.dimensions()}')
        
    def generate_grid(self, rgb_color: tuple) -> Image:
        white_color=(200,200,200)
        img = Image.new('RGB', self.lcd_size, white_color)
        # Split the image into a grid
        for x in range(0, self.lcd_size[0], int(self.lcd_size[0] / 10)):
            img1 = ImageDraw.Draw(img)   
            shape = [(x, 0), (x, self.lcd_size[1])]
            img1.line(shape, fill =rgb_color, width = 5) 
        
        for y in range(0, self.lcd_size[1], int(self.lcd_size[1] / 10)):
            img1 = ImageDraw.Draw(img)   
            shape = [(0, y), (self.lcd_size[0], y)]
            img1.line(shape, fill =rgb_color, width = 5)        

        return img

    def generate_pitchblack(self) -> Image:
        black_color=(0,0,0)
        img = Image.new('RGB', self.lcd_size, black_color)

        return img

    
    def display_img(self, img: Image) -> None:
        self.lcd.display(img)
        
    def _clear(self) -> None:
        img_clear = Image.new('RGB', self.lcd_size, (0, 0, 0))
        self.lcd.display(img_clear)
        
        
if __name__ == '__main__':
    try:
        # cal = Calculator()
        powerled=(2,0,0)
        cam = Camera()
        GPIO.setmode(GPIO.BCM)
        pixels = neopixel.NeoPixel(board.D18, 64)
        pixels.fill( (0, 0, 0))
        # fill with red led then take a snashot
        # cal.fill_in_square(pixels)
        pixels.fill( (0, 0, 0))
        sleep(0.05)
        pixels.show()
        for item in range(0, 64, 1):
            led = item
            pixels[item]=powerled        
            pixels.show()
        # cal.save_picture(cam)
        x = datetime.datetime.now()
        cam.take_photo(x.strftime("%Y-%m-%d-%H-%M-%S-%f"))
        print("square")
        sleep(0.05)

        # fill first and last row red led then take a snashot
        # cal.fill_fisrt_and_last_row(pixels) 
        pixels.fill( (0, 0, 0))
        sleep(0.05)
        pixels.show()
        for item in range(0, 8, 1):
            led = item
            pixels[item]=powerled        
            pixels.show()
        for item in range(56, 64, 1):
            led = item            
            pixels[item]=powerled        
            pixels.show()
        # cal.save_picture(cam)
        x = datetime.datetime.now()
        cam.take_photo(x.strftime("%Y-%m-%d-%H-%M-%S-%f"))
        print("row")
        sleep(0.05)

        # fill with red led then take a snashot

        pixels.fill( (0, 0, 0))
        sleep(0.05)
        pixels.show()
        for item in range(0, 64, 1):
            led = item
            pixels[item]=powerled        
            pixels.show()
        # cal.save_picture(cam)
        
        
        spi_lcd_1 = SpiDev(config.SPI_BUS, config.SPI_DEVICE)
        lcd_control_1 = LCD_Controller(spi=spi_lcd_1)
        blue_color=(0, 0, 255)
        lcd_control_1.display_img(
            lcd_control_1.generate_grid(blue_color)
        )
        x = datetime.datetime.now()
        cam.take_photo(x.strftime("%Y-%m-%d-%H-%M-%S-%f"))
        sleep(10)
        lcd_control_1.display_img(
            lcd_control_1.generate_pitchblack()
        )
        x = datetime.datetime.now()
        cam.take_photo(x.strftime("%Y-%m-%d-%H-%M-%S-%f"))
        
        sleep(10)
    except KeyboardInterrupt:
        pass
    finally:
        lcd_control_1.lcd.clear().display()
        GPIO.cleanup()
        spi_lcd_1.close()

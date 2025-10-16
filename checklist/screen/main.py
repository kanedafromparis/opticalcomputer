from PIL import Image, ImageDraw 
import RPi.GPIO as GPIO
from spidev import SpiDev
from time import sleep
import third_party.ILI9486 as LCD
import config
import random
import numpy as np

class LCD_Controller:
    def __init__(self, spi:SpiDev)->None:
        self.lcd_size = (480, 320)
        self.spi = spi
        self.spi.mode = 0b10
        self.spi.max_speed_hz = 64000000

        self.lcd = LCD.ILI9486(dc=5, rst=6, spi=self.spi).begin()
        self.lcd = LCD.ILI9486(dc=config.DC_PIN, rst=config.RST_PIN, spi=spi).begin()
        print(f'Initialized display with landscape mode = {self.lcd.is_landscape()} and dimensions {self.lcd.dimensions()}')
        
    def generate_grid(self, rgb_color: tuple, grid_size:int) -> Image:
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
    
    
    def display_img(self, img: Image) -> None:
        self.lcd.display(img)
        
    def _clear(self) -> None:
        img_clear = Image.new('RGB', self.lcd_size, (0, 0, 0))
        self.lcd.display(img_clear)
        
        
if __name__ == '__main__':
    try:
        GPIO.setmode(GPIO.BCM)
        spi_lcd_1 = SpiDev(config.SPI_BUS, config.SPI_DEVICE)
        lcd_control_1 = LCD_Controller(spi=spi_lcd_1)
        blue_color=(0, 0, 255)
        lcd_control_1.display_img(
            lcd_control_1.generate_grid(blue_color, 40)
        )
        sleep(10)
    except KeyboardInterrupt:
        pass
    finally:
        lcd_control_1.lcd.clear().display()
        GPIO.cleanup()
        spi_lcd_1.close()

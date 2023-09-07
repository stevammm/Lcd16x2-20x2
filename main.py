from machine import I2C, Pin 
from time import sleep 
from pico_i2c_lcd import I2cLcd 

def hide_cursor_count(lcd): 
  """Hide the cursor and display a count from 0 to 19."""
  lcd.clear() 
  lcd.hide_cursor() 
  for count in range(20): 
    lcd.putstr(str(count)) 
    sleep(0.4) 
    lcd.clear() 

def initialize_i2c_lcd2(sda_pin, scl_pin, i2c_freq): 
  """Initialize the I2C LCD display with the given parameters.""" 
  i2c_bus = I2C(0, sda=Pin(sda_pin), scl=Pin(scl_pin), freq=i2c_freq) 
  i2c_address = i2c_bus.scan()[0] 
  return I2cLcd(i2c_bus, i2c_address, 2, 16), i2c_address 

def initialize_i2c_lcd4(sda_pin, scl_pin, i2c_freq): 
  """Initialize the I2C LCD display with the given parameters.""" 
  i2c_bus = I2C(1, sda=Pin(sda_pin), scl=Pin(scl_pin), freq=i2c_freq) 
  i2c_address = i2c_bus.scan()[0] 
  return I2cLcd(i2c_bus, i2c_address, 4, 20), i2c_address 

def display_address(lcd, i2c_address): 
  """Display the I2C address in decimal and hexadecimal formats.""" 
  lcd.blink_cursor_on() 
  for address_format in (str, hex): 
    lcd.putstr("STEVAM\n") 
    lcd.putstr("LCD 16x2") 
    sleep(2) 
    lcd.clear() 
  lcd.blink_cursor_off() 

def display_address2(lcd, i2c_address2): 
  """Display the I2C address in decimal and hexadecimal formats.""" 
  lcd.blink_cursor_on() 
  for address_format in (str, hex): 
    lcd.putstr("MARCELOT\n") 
    lcd.putstr("2LCD 20x257657656\n") 
    lcd.putstr("3LCD 20x2\n") 
    lcd.putstr("4LCD 20xihugug2\n") 
    sleep(2) 
    lcd.clear() 
  lcd.blink_cursor_off() 

def hide_cursor_count(lcd): 
  """Hide the cursor and display a count from 0 to 19.""" 
  lcd.clear() 
  lcd.hide_cursor() 
  for count in range(20): 
    lcd.putstr(str(count)) 
    sleep(0.4) 
    lcd.clear() 


"""Main function to run the I2C LCD display example.""" 
lcd_display, i2c_address = initialize_i2c_lcd2(sda_pin=0, scl_pin=1, i2c_freq=400000) 
lcd_display2, i2c_address2 = initialize_i2c_lcd4(sda_pin=2, scl_pin=3, i2c_freq=400000) 
while True: 
    display_address(lcd_display, i2c_address) 
    display_address2(lcd_display2, i2c_address2) 
    hide_cursor_count(lcd_display) 

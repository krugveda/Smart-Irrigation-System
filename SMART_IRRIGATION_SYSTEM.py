     # import required modules
      from machine import ADC, Pin
      import machine
      import utime
      import network
      import BlynkLib 
      from gpio_lcd import GpioLcd 
      # Create the LCD object
      lcd = GpioLcd(rs_pin=Pin(16),
              enable_pin=Pin(17),
              d4_pin=Pin(18),
              d5_pin=Pin(19),
              d6_pin=Pin(20),
              d7_pin=Pin(21),
              num_lines=2, num_columns=16)
            # use variables instead of numbers:            soil = ADC(Pin(26))
                  
# Soil moisture PIN reference        button = Pin(15, Pin.IN)        #Calibraton values         min_moisture=35200
        max_moisture=57800 
        readDelay = 2 # delay between readings 
        lcd.display_on()
        lcd.backlight_on() 
        lcd.clear()
        lcd.move_to(0,0)
        lcd.putstr('Soil Moisture’)
        lcd.move_to(0,1)
        lcd.putstr('Control System’)
        utime.sleep(2) 
        lcd.clear()
       lcd.move_to(0,0)
       lcd.putstr('Please Wait...’)
       lcd.move_to(0,1)
       lcd.putstr('Connecting WiFi’)
        utime.sleep(2)
        wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("Rugveda","12345678")
#define BLYNK_TEMPLATE_ID "TMPLwDmJFKmI"
#define BLYNK_TEMPLATE_NAME "Quickstart Template"
#define BLYNK_AUTH_TOKEN "oPBe1o55AEArHhjs50zX-e3-mSMWytpc"
# Blynk authentication token
BLYNK_AUTH = "oPBe1o55AEArHhjs50zX-e3-mSMWytpc"
# connect the network       
wait = 10
while wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
 wait -= 1
    print('waiting for connection...')
    utime.sleep(1)
    # Handle connection error
if wlan.status() != 3:
    lcd.clear()
    lcd.move_to(3,0)
    lcd.putstr('Error Not')
    lcd.move_to(0,1)
    lcd.putstr('Connecting WiFi')
    utime.sleep(2)
 raise RuntimeError('wifi connection failed')
 else:
    print('connected')
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr('WiFi Connected')
    utime.sleep(2)
    ip=wlan.ifconfig()[0]
    print('IP: ', ip)
# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)
 # Initialize the relay pins
pump = Pin(14, Pin.OUT)
 # Register virtual pin handler
@blynk.on("V1") #virtual pin V1
def v1_write_handler(value): #read the value
    if int(value[0]) == 1:
        pump.value(0) #turn the pump on
        print('Pump ON Manual')
        lcd.clear()
        lcd.move_to(2,0)
        lcd.putstr('Manually')
        lcd.move_to(0,1)
        lcd.putstr('Pump OFF')
        utime.sleep(3)
else:
        print('Pump OFF Manual')
        pump.value(1) #turn the pump off
        lcd.clear()
lcd.move_to(2,0)
        lcd.putstr('Manually')
        lcd.move_to(0,1)
        lcd.putstr('Pump ON')
        utime.sleep(3)
 
# Run the main loop
while True:
 
    # read moisture value and convert to percentage into the calibration range
    moisture = (max_moisture-soil.read_u16())*100/(max_moisture-min_moisture) 
    # print values
    print("moisture: " + "%.2f" % moisture +"% (adc: "+str(soil.read_u16())+")")
    #int percentage = ('%f',moisture)
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr('Soil Moisture:')
    lcd.move_to(0,1)
    #lcd.hal_write_data(moisture)
    utime.sleep(3)
# Send sensor data to Blynk
   blynk.virtual_write(0, moisture)  # virtual pin 0 for moisture    
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr('Select Mode')
    lcd.move_to(0,1)
    lcd.putstr("Auto or Manual")
    utime.sleep(3)
    logic_state = button.value()    
    if logic_state == True:     
   # if push_button pressed
        lcd.clear()
        lcd.move_to(0,0)
        lcd.putstr('Automatic Mode')
        lcd.move_to(2,1)
        lcd.putstr('Selected')
        utime.sleep(2)
 if (moisture <30):
            pump.value(0) #turn the pump on
            print('Moisture LOW Pump ON')
lcd.clear()
            lcd.move_to(0,0)
            lcd.putstr('SoilMoisture LOW')
            lcd.move_to(0,1)
            lcd.putstr('Pump ON')
            utime.sleep(3)
        else:
            pump.value(1)    #turn the pump off
            print('Pump OFF')
            lcd.clear()
            lcd.move_to(0,0)
            lcd.putstr('SoilMoisture OK')
            lcd.move_to(0,1)
            lcd.putstr('Pump OFF’)
  utime.sleep(3)
if logic_state == False:
        lcd.clear()
        lcd.move_to(2,0)
        lcd.putstr('Manual Mode')
       lcd.move_to(2,1)
 lcd.putstr('Selected')
        utime.sleep(2)
        lcd.clear()
        lcd.move_to(2,0)
        lcd.putstr('Goto Blynk')
        lcd.move_to(2,1)
        lcd.putstr('Application')
        utime.sleep(2)
        lcd.move_to(2,0)
        lcd.putstr('Goto Blynk')
        lcd.move_to(2,1)
        lcd.putstr('Application’)
 utime.sleep(2) 
    # Run Blynk
  blynk.run()
    utime.sleep(readDelay)
 # set a delay between readings


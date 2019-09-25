import serial

class LED:
    def __init__(self, port, baud=9600):
        if(port):
            self.ser = serial.Serial(port, baud)

        else:
            ## TO DO: Find arduino if no port given
            print("Not implemented yet, need serial port")


    def color(self, red, green, blue):
        # Generate command
        command = str(red)+","+str(green)+","+str(blue)+"\n"
        
        # Send command
        self.ser.write(command.encode())


    def off(self):
        self.color(0, 0, 0)

class LED_test:
    def __init__(self):
        pass
    def color(self, red, green, blue):
        print("Changed LEDS to ("+str(red)+","+str(green)+","+str(blue)+")")
    def off(self):
        print("Changed LEDS to off")

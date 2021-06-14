from machine import Pin
import time


class Led ():
    """
    LED driver
    """
    def __init__(self):
        self.__led = [
            Pin(6, Pin.OUT),
            Pin(7, Pin.OUT),
            Pin(8, Pin.OUT),
            Pin(9, Pin.OUT),
            Pin(10, Pin.OUT),
            Pin(11, Pin.OUT),
            Pin(12, Pin.OUT),
            Pin(13, Pin.OUT),
            Pin(14, Pin.OUT),
            Pin(15, Pin.OUT)
        ]

    def wakeup(self):
        """
        Turn on All LEDs and turn off after a second.
        """
        self.on_all()
        time.sleep(1)
        self.clear()

    def brink_scale(self, scale: int, maximum: int):
        """
        Display the LED corresponding to the seismic intensity class.
        """
        for i in range(0, 10):
            if i <= scale or i == maximum:
                self.on(i)
            else:
                self.off(i)

    def on(self, pin: int):
        """
        Turn on the LED corresponding to the specified seismic intensity class.
        """
        self.__led[pin].on()

    def off(self, pin: int):
        """
        Turn off the LED corresponding to the specified seismic intensity class.
        """
        self.__led[pin].off()

    def toggle(self, pin: int):
        """
        Toggle the LED corresponding to the specified seismic intensity class.
        """
        self.__led[pin].toggle()

    def clear(self):
        """
        Turn off All LEDs.
        """
        for i in range(0, 10):
            self.off(i)

    def on_all(self):
        """
        Turn on All LEDs.
        """
        for i in range(0, 10):
            self.on(i)

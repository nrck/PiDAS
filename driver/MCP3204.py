from math import trunc
from utime import sleep, time
from machine import Pin, SPI


class MCP3204:
    """
    A/D converter MCP3204 driver
    """

    def __init__(self, spi: SPI, cs: Pin):
        self.spi = spi
        self.cs = cs

    def read(self, ch: int):
        """
        Read the value of the channel
        """
        send = bytearray([0x06 | (ch >> 2), 0xff & (ch << 6), 0])
        recv = bytearray(3)
        self.cs.low()
        self.spi.write_readinto(send, recv)
        self.cs.high()
        return int.from_bytes(recv, 'big')


if __name__ == "__main__":
    BAUDRATE = 115200
    SPI_PIN_SCK = Pin(18)
    SPI_PIN_MOSI = Pin(19)
    SPI_PIN_MISO = Pin(20)
    SPI_PIN_CS = Pin(21, Pin.OUT)
    ADC = MCP3204(
        SPI(0, baudrate=BAUDRATE, polarity=0, phase=0, sck=SPI_PIN_SCK, mosi=SPI_PIN_MOSI, miso=SPI_PIN_MISO), SPI_PIN_CS)

    while (True):
        print("Ch0:", ADC.read(0))
        print("Ch1:", ADC.read(1))
        print("Ch2:", ADC.read(2))
        print("Ch3:", ADC.read(3))
        sleep(1)
import time
from uuid import UUID
import logging

import pygatt.backends

logger = logging.getLogger(__name__)

class VAlrtButton(object):
    # 0x34 is also writiable
    # 0x5c 0001
    # 0x62 disconnect?
    
    def __init__(self, address, mode=None, event_handler=None):
        self.address = address
        self._connection = None
        self.mode = mode
        self._serial = None
        self._revision = None
        self.event_handler = event_handler

    @property
    def connection(self):
        if self._connection:
            return self._connection
        elif self.address:
            # logfile=open("/tmp/gatttool.log", "a")
            adapter = pygatt.backends.GATTToolBackend()  # gatttool_logfile=logfile)
            adapter.start(False)
            logger.debug("connecting")
            self._connection = adapter.connect(self.address, address_type=pygatt.BLEAddressType.public, timeout=20.0)
            return self._connection
        else:
            return None

    def command(self, handle, data_array):
        logger.debug("sending: {0} to {1}".format(data_array, handle))
        self.connection.char_write_handle( handle, bytearray(data_array), wait_for_response=True, timeout=20)

    def connect(self):
        # init connection
        self.command(0x0059, [0x80, 0xbe, 0xf5, 0xac, 0xff])
        self.button_mode()
        self.register_button_event_handler()
        self.read_serial()
        self.read_revision()

    def disconnect(self):
        self.connection.disconnect()

    def beep_forever(self):
        self.command(0x0028, [0x01])

    def read_serial(self):
        """
        Return serial number of device
        """
        if not self._serial:
            self._serial = self.connection.char_read(UUID('00002a25-0000-1000-8000-00805f9b34fb'), timeout=15)
        logger.debug(self._serial)
        return self._serial

    def read_revision(self):
        """
        Return revision string
        """
        # writing to it beeps
        if not self._revision:
            self._revision = self.connection.char_read(UUID('00002a28-0000-1000-8000-00805f9b34fb'), timeout=15)
        logger.debug(self._revision)
        return self._revision        

    def read_002f(self):
        # read request 0x002f
        pass

    def battery(self):
        # event handle 0x0030
        pass

    def alarm(self, mode):
        """
        Set alarm on or off.
        0x00 resets alarm
        0x01 sets off alarm
        """
        self.command(0x0052, [mode])

    def alarm_off(self):
        """
        Turn on alarm
        """
        self.alarm(0x00)

    def alarm_on(self):
        """
        Turn off alarm
        """
        self.alarm(0x00)

    def beep(self):
        self.command(0x004c, [0x02])

    def alarm_mode(self, mode=0x00):
        """
        Select which alarm to trigger on 3second button press
         * 0x00: Audio visual alarm
           On mode entry beep once and blink green.
           On alarm activation beep continually and blink red
         * 0x01: Visual alarm
           On mode entry blink green.
           On alarm activation blink red. 
         * 02: Audio alarm
           On mode entry beep once.
           On alarm activation beep once
        """
        self.command(0x004c, [mode])

    def register_button_event_handler(self):
        logger.debug("registering button event")
        self.connection.subscribe(UUID('fffffff4-00f7-4000-b000-000000000000'), self.button_event_handler)
        logger.debug("registered button event")

    def button_event_handler(self, handle, value):
        """
        Possible returned values in button event:
         * 1 button depressed
         * 0 button up
         * 3 second hold on button
         * 4 drop sense?
        """
        if self.event_handler:
            self.event_handler(value)
        logger.debug("got buttton event: {0}".format(value))
        
    def button_mode(self, mode=None):
        """
        Known valid modes:
         * 0x01 send 1 on button down. 0 on button up
         * 0x02 after 3 second press beep, flash red (for ever) and send 3,
           flash green + beep on connect 
         * 0x03 combination of 01 and 02
         * 0x06 enable drop detection?
        """
        self.command(0x004f, [mode or self.mode])
        
if __name__ == "__main__":
    vbtn = VAlrtButton("7c:66:9d:71:14:40", 0x01)
    vbtn.connect()
    vbtn.alarm_mode(0x00)
    time.sleep(60)
    vbtn.beep()
    vbtn.disconnect()

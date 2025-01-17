#!/usr/bin/env python3

import asyncio
import logging

import usb.core
import usb.util
import pyvisa


class ArtiqThorlabsPm400():
    def __init__(self, device):
        rm = pyvisa.ResourceManager()
        self.instr = rm.open_resource(device)

    async def set_power_auto_ranging_on(self, auto_ranging_on):
        """
        Set power measurement auto-ranging on.
        """
        self.instr.write(f"SENS:POW:RANGE:AUTO {auto_ranging_on}")

    async def get_power_auto_ranging_on(self):
        """
        Get power measurement auto-ranging on.
        """
        return int(self.instr.query("SENS:POW:RANGE:AUTO?"))


    async def get_power(self):
        """
        Get the power value.
        """
        return float(self.instr.query("MEAS:POW?"))

    async def ping(self):
        idn = self.instr.query("*IDN?")
        if "PM400" in idn:
            return True
        else:
            return False


class ArtiqThorlabsPm400Sim():
    def __init__(self):
        self.auto_ranging_on = None

    async def set_power_auto_ranging_on(self, auto_ranging_on):
        """
        Simulate setting power measurement auto-ranging on.
        """
        self.auto_ranging_on = auto_ranging_on
        logging.warning(f"Simulated: Setting auto-ranging to {auto_ranging_on}")

    async def get_power_auto_ranging_on(self):
        """
        Simulate getting power measurement auto-ranging on.
        """
        return self.auto_ranging_on
        logging.warning(f"Simulated: Auto-ranging readout: {self.auto_ranging_on}")

    async def get_power(self):
        """
        Simulate getting the power value.
        """
        return 0.3
        logging.warning("Simulated: Power readout: 0.3")

    async def ping(self):
        return True

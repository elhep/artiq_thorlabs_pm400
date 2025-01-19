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
        # Clear errors from memory
        self.instr.write('*CLS')

    def write_instrument(self, query):
        self.instr.write(query)
        error_response = self.instr.query('SYST:ERR?').strip()
        if not error_response.startswith('+0'):
            raise ValueError(f"Instrument Error: {error_response}")

    async def set_power_auto_ranging_on(self, auto_ranging_on):
        """
        Set power measurement auto-ranging on.
        """
        self.write_instrument(f"SENS:POW:RANGE:AUTO {auto_ranging_on}")

    async def get_power_auto_ranging_on(self):
        """
        Get power measurement auto-ranging on.
        """
        return int(self.instr.query("SENS:POW:RANGE:AUTO?"))

    async def set_wavelength(self, wavelength):
        """
        Set wavelength value.
        """
        self.write_instrument(f"SENS:CORR:WAV {wavelength}")

    async def get_wavelength(self):
        """
        Get wavelength value.
        """
        return int(self.instr.query("SENS:CORR:WAV?"))

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
        self.wavelength = None

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

    async def set_wavelength(self, wavelength):
        """
        Simulate setting wavelength value.
        """
        self.wavelength = wavelength
        logging.warning(f"Simulated: Setting wavelength value to {wavelength}")

    async def get_wavelength(self):
        """
        Simulate getting wavelength value.
        """
        return self.wavelength
        logging.warning(f"Simulated: Wavelength readout: {self.wavelength}")

    async def get_power(self):
        """
        Simulate getting the power value.
        """
        return 0.3
        logging.warning("Simulated: Power readout: 0.3")

    async def ping(self):
        return True

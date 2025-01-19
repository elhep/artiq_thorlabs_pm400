import sys

from sipyco.test.generic_rpc import GenericRPCCase


class GenericPm400Test:
    def test_set_power_auto_ranging_on(self):
        """
        Test setting and getting the power autoranging mode.
        """
        self.artiq_pm400.set_power_auto_ranging_on(True)
        self.assertTrue(self.artiq_pm400.get_power_auto_ranging_on())

        self.artiq_pm400.set_power_auto_ranging_on(False)
        self.assertFalse(self.artiq_pm400.get_power_auto_ranging_on())

    def test_set_wavelength(self):
        """
        Test setting and getting the wavelength value.
        """
        wavelength = 600
        self.artiq_pm400.set_wavelength(wavelength)
        self.assertEqual(self.artiq_pm400.get_wavelength(), wavelength)


class TestHighfinesseSim(GenericRPCCase, GenericPm400Test):
    def setUp(self):
        GenericRPCCase.setUp(self)
        command = (
            sys.executable.replace("\\", "\\\\")
            + " -m artiq_thorlabs_pm400.aqctl_artiq_thorlabs_pm400"
            + " -p 3285 --simulation"
        )
        self.artiq_pm400 = self.start_server("artiq_pm400", command, 3285)

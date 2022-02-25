"""Tests of ATTMs Manager."""
from telegram import Location

from nearest_atms.atm_manager import ATMManager


class TestATMManager:
    atm_manager = ATMManager()

    def test_init(self):
        assert len(self.atm_manager.header) == 17
        assert self.atm_manager.rows
        assert self.atm_manager.link
        assert self.atm_manager.banelco

    def test_get_link_atms(self):
        link_atms = self.atm_manager._get_link_atms()
        assert 'BANELCO' not in link_atms

    def test_get_banelco_atms(self):
        banelco_atms = self.atm_manager._get_banelco_atms()
        assert 'LINK' not in banelco_atms

    def test_get_nearest_link_atms_case_log_distance(self):
        """Too big the distance between the user and the ATMs loaded in the system."""
        location_rio_primero_cordoba = Location(longitude=-63.629139, latitude=-31.32809)

        nearest_atms = self.atm_manager.get_nearest_link_atms(location_rio_primero_cordoba)

        assert nearest_atms == []

    def test_get_nearest_link_atms_case_good(self):
        """The location of the user is in the Obelisk, and have nears Link ATMs loaded in the system."""
        location_obelisk = Location(longitude=-34.60306774908537, latitude=-58.38163477301819)

        nearest_atms = self.atm_manager.get_nearest_link_atms(location_obelisk)

        assert len(nearest_atms) == 3

        networks = [x[4] for x in nearest_atms]
        assert 'BANELCO' not in networks

    def test_get_nearest_banelco_atms_case_good(self):
        """The location of the user is in the Obelisk, and have nears Banelco ATMs loaded in the system."""
        location_obelisk = Location(longitude=-34.60306774908537, latitude=-58.38163477301819)

        nearest_atms = self.atm_manager.get_nearest_banelco_atms(location_obelisk)

        assert len(nearest_atms) == 3

        networks = [x[4] for x in nearest_atms]
        assert 'LINK' not in networks

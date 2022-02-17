"""Tests of ATTMs Manager."""
from unittest import TestCase

from nearest_atms.atm_manager import ATMManager


class TestATMManager(TestCase):
    atm_manager = ATMManager()

    def test_init(self):
        assert len(self.atm_manager.header) == 17
        assert self.atm_manager.rows
        assert self.atm_manager.link
        assert self.atm_manager.banelco

    def test_get_nearest_link_atms(self):
        """TODO."""
        pass

    def test_get_link_atms(self):
        link_atms = self.atm_manager._get_link_atms()
        assert 'BANELCO' not in link_atms

    def test_get_banelco_atms(self):
        """TODO."""
        pass

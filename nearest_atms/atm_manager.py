"""ATMs Manager."""
import csv
from nearest_atms import settings
from geopy.distance import distance


class ATMManager:
    """ATMs Manager"""

    def __init__(self):
        file = open(settings.ATMS_FILE)
        csvreader = csv.reader(file)
        self.header = next(csvreader)
        self.rows = self._get_rows(csvreader)
        file.close()

        self.link = self._get_link_atms()
        self.banelco = self._get_banelco_atms()

    def get_nearest_link_atms(self, location):
        """
        TODO.
        Args:
            location ():
        """
        user_coords = (location.latitude, location.longitude)

        asd = []
        for i in self.link:
            atm_coords = (i.latitude, i.longitude)
            asd.append(distance(user_coords, atm_coords).km)

        asd.sort()

    def _get_link_atms(self):
        link_atms = []
        red_index = self.header.index('red')
        for row in self.rows:
            if row[red_index] == 'LINK':
                link_atms.append(row)

        return link_atms

    def _get_banelco_atms(self):
        banelco_atms = []
        red_index = self.header.index('red')
        for row in self.rows:
            if row[red_index] == 'BANELCO':
                banelco_atms.append(row)

        return banelco_atms

    @staticmethod
    def _get_rows(csvreader):
        """
        TODO.
        Args:
            csvreader ():

        Returns:

        """
        rows = []

        for row in csvreader:
            rows.append(row)

        return rows

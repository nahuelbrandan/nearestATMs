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

        self.longitude_index = self.header.index('long')
        self.latitude_index = self.header.index('lat')

        self.link = self._get_link_atms()
        self.banelco = self._get_banelco_atms()

    def get_nearest_link_atms(self, location):
        """
        Get the user's location and obtain the nearest ATMs of the Link networks.
        Args:
            location (Location): location of the user

        Returns:
            List(tuple): Information of the nearest ATMs that have the users.
                         List with maximum 3 elements.
        """
        user_coords = (location.latitude, location.longitude)

        response = []
        for i in self.link:
            atm_coords = (float(i[self.longitude_index]), float(i[self.latitude_index]))

            distance_from_user_to_atm = distance(user_coords, atm_coords).km
            if distance_from_user_to_atm > settings.MAX_DISTANCE:
                continue

            response.append((distance_from_user_to_atm, i))

        response = sorted(response, key=lambda x: x[0])
        response = response[:3]
        response = [x[1] for x in response]

        return response

    def get_nearest_banelco_atms(self, location):
        """
        Get the user's location and obtain the nearest ATMs of the Banelco networks.
        Args:
            location (Location): location of the user

        Returns:
            List(tuple): Information of the nearest ATMs that have the users.
                         List with maximum 3 elements.
        """
        user_coords = (location.latitude, location.longitude)

        response = []
        for i in self.banelco:
            atm_coords = (float(i[self.longitude_index]), float(i[self.latitude_index]))

            distance_from_user_to_atm = distance(user_coords, atm_coords).km
            if distance_from_user_to_atm > settings.MAX_DISTANCE:
                continue

            response.append((distance_from_user_to_atm, i))

        response = sorted(response, key=lambda x: x[0])
        response = response[:3]
        response = [x[1] for x in response]

        return response

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

"""Project settings."""

import os

dir_path = os.path.dirname(os.path.realpath(__file__))

TOKEN = 'YOUR_BOT_TOKEN'

ATMS_FILE = os.path.join(dir_path, '../resources', 'ATMs-in-CABA.csv')

MAX_DISTANCE = 0.5  # kms
MAX_QUANTITY = 3  # maximum number of ATMs to show

"""Setup of the project."""

import os

from setuptools import (
    setup,
    find_packages,
)

from nearest_atms.version import __version__

NAME = "nearestATMs"

SCRIPT = [os.path.join("nearest_atms", 'main.py')]

DESCRIPTION = "Telegram bot, fot get the nearest ATMs of the user location."
LONG_DESCRIPTION = "Telegram bot, where the user using his location, " \
                   "could ask information for the nearest ATMs that he have."

with open("requirements.txt") as f:
    required = f.read().splitlines()

here = os.path.dirname(os.path.realpath(__file__))

setup(
    name=NAME,
    version=__version__,
    url="https://github.com/nahuelbrandan/nearestATMs",
    license="GNU GENERAL PUBLIC LICENSE",
    author="nahuel brandan",
    keywords="telegram bot",
    install_requires=required,
    author_email="contact@nahuelbrandan.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    entry_points={
        'console_scripts': ['nearestATMs=nearest_atms.main:main']
    },
    platforms="any",
    classifiers=[
        "Development Status :: 1 - Development",
        "Programming Language :: Python :: >3.6",
        "Environment :: Console",
        "Topic :: Software Development :: Telegram Bot :: Map localization",
    ],
    scripts=SCRIPT,
)

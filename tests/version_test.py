"""Version tests."""
from nearest_atms.version import __version__


class TestVersion:

    def test_version(self):
        assert __version__ == "0.0.1"

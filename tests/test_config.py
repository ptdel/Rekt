import sys
import toml
import pytest
from io import StringIO
from pathlib import Path
from tempfile import NamedTemporaryFile


base_directory = Path(__file__).absolute().parent.parent
sys.path.insert(0, str(base_directory / "Rekt"))

from Rekt.Config import Config


@pytest.fixture()
def config_file():
    settings = b"""
    [a]
    b = \"c\"
    """
    temp = NamedTemporaryFile()
    temp.write(settings)
    temp.flush()
    yield temp


def test_config(config_file):
    with open(config_file.name, "r") as fp:
        config_file = toml.load(fp)
        config = Config(config_file)

    assert config.a.b == "c"

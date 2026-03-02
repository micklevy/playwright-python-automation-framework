import json
import pytest


@pytest.fixture(scope="session")
def config():
    with open("config/config.json") as f:
        return json.load(f)
import json
import os

import pytest
project_dir = os.path.dirname(os.path.abspath(__file__))

from fixture.sut import Sut

fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


@pytest.fixture
def app(request):
    global fixture
    global target
    config = load_config(request.config.getoption("--target"))

    if fixture is None or not fixture.is_valid():
        fixture = Sut(config['path'])
    fixture.main.ensure_modals_closed()
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.main.ensure_modals_closed()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--target", action="store", default="config.json")



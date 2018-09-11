import clr
import json
import os

import pytest

project_dir = os.path.dirname(os.path.abspath(__file__))

clr.AddReferenceByName(
    "Microsoft.Office.Interop.Excel, Version=15.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c")

from Microsoft.Office.Interop import Excel

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


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("xlsx_"):
            testdata = load_from_xlsx(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_xlsx(file):
    f = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.xlsx" % file)
    excel = Excel.ApplicationClass()
    workbook = excel.Workbooks.Open(f)
    sheet = workbook.ActiveSheet
    l = []
    for i in range(65536):
        value = sheet.Range["A%s" % (i + 1)].Value2
        if not value:
            break
        l.append(value)
    excel.Quit()
    return l

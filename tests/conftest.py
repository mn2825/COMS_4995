import pytest

def pytest_addoption(parser):
    parser.addoption("--cmdopt", action="store", default="../data/comm_public_2017.xlsx")

@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")

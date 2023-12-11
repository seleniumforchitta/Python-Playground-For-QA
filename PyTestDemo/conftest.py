import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executed first.")
    yield
    print("I will be executed last.")


@pytest.fixture
def dataLoad():
    print("User profile data is being created")
    return ["rama", "Ranjan", "Google.com"]


@pytest.fixture(params=[("Chrome","rama"), ("Firefox","Ranjan"), ("IE","Swain")])
def crossBrowser(request):
    return request.param

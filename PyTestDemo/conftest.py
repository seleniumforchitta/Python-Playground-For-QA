import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executed first.")
    yield
    print("I will be executed last.")


@pytest.fixture
def dataLoad():
    print("User profile data is being created")
    return ["rama", "Kumar ", "Google.com"]


@pytest.fixture(params=[("Chrome","rama"), ("Firefox","Kumar "), ("IE","Mishra ")])
def crossBrowser(request):
    return request.param

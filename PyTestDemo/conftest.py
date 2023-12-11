import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executed first.")
    yield
    print("I will be executed last.")


@pytest.fixture
def dataLoad():
    print("User profile data is being created")
    return ["Chitta", "Ranjan", "Google.com"]


@pytest.fixture(params=[("Chrome","Chitta"), ("Firefox","Ranjan"), ("IE","Swain")])
def crossBrowser(request):
    return request.param

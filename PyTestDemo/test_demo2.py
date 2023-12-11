import pytest


@pytest.mark.xfail
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed because strings don't match."


@pytest.mark.smoke
def test_secondCreditCard():
    a = 4
    b = 6
    assert a + 2 == b, "Addition didn't match"


@pytest.fixture()
def setup():
    print("I will be executed first.")


def test_fixtureDemo(setup):
    print("It will execute after setup")

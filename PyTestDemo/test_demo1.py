import pytest


@pytest.mark.smoke
def test_firstProgram():
    print("Hello")


def test_GreetCreditCard(setup):
    print("Good Morning!")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[0])

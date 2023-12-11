import pytest

from PyTestDemo.BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):

    def test_editProfile(self, dataLoad):
        log = self.getlogger()
        print(dataLoad)
        print(dataLoad[0])
        print(dataLoad[1])
        print(dataLoad[2])
        log.info(dataLoad)
        log.info(dataLoad[0])
        log.info(dataLoad[2])
        print(dataLoad[1])




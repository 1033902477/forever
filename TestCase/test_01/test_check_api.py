import pytest
import inspect
import time
import json
from Common.OperationData import DealData as dlt
from Common.ResquestMethod import ResquestMethodS as rms
from Common.LogLog import logger

pytest.mark.usefixtures('statr_test')
# @pytest.mark.usefixtures('init')
class TestCheckAPI():

    @pytest.mark.parametrize('name, method, api, params, expection', dlt().deal_data())
    def test_api(self, name, method, api, params, expection):
        logger.info("开始运行用例 %s" % (inspect.stack()[0][3]))
        response = rms(name=name, url=api, method=method, params=params).rqmethod()
        expection = json.loads(expection)
        assert expection['status_code'] == response.status_code
        assert dlt().validation_data(expection = expection, response = response.json())


if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test_check_api.py'])
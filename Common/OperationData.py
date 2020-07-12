import time, json
from Common.GetCaseData import GetExeclData
from Common.ResquestMethod import ResquestMethodS as rm
from Data.TestCasePath import test_case_path
from Common.LogLog import Logger


class DealData:

    # 处理数据格式
    def deal_data(self):
        filename = test_case_path()
        data = GetExeclData(filename=filename).get_execl_data()
        data_list = []
        for i in data.values():
            data_list.append((i['name'],i['method'],i['api'], i['params'],i['expection']))

        return data_list

    # 判断数据类型
    def valid_flag(self, data):
        if isinstance(data, list):
            return True
        elif isinstance(data, dict):
            return True
        else:
            return False

    # 检验数据
    def validation_data(self, expection: dict, response: dict):
        expection_str = str(expection)
        response_str = str(response)
        if expection_str == response_str:
            return True
        else:
            return False



if __name__ == '__main__':
    expection = '{"translateResult":[[{"tgt":"Validation data","src":"验证数据"}]],"errorCode":0,"type":"zh-CHS2en","smartResult":{"entries":["","data authentication\r\n","data validation\r\n"],"type":1}}'
    response = '{"translateResult":[[{"tgt":"Validation data","src":"验证数据"}]],"errorCode":0,"type":"zh-CHS2en","smartResult":{"entries":["","data authentication\r\n","data validation\r\n"],"type":1}}'
    expection = json.loads(expection.replace('\r\n',''))
    response = json.loads(response.replace('\r\n', ''))
    da = DealData().validation_data(expection, response)
    print(da)
    # a = [1000]
    # print(isinstance(a, str))
    # dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    # dict2 = {'a': 1, 'b': 2, 'c': 5, 'e': 6}
    # print(dict1.items())
    # differ = set(dict1.items()) ^ set(dict2.items())
    # print(differ)
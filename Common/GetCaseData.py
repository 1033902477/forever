import pandas as pd
from Common.LogLog import logger


class GetExeclData:

    def __init__(self, filename):
        self._filename = filename

    def get_execl_data(self):
        try:
            resquest_base = {}  # 读取全部用例
            execl_data = pd.DataFrame(pd.read_excel(self._filename, keep_default_na=False))
            logger.info("=====测试用例读取开始=====")
            execl_data = execl_data.fillna(0)
            for coordinates in range(len(execl_data)):
                execl_base_data = execl_data.ix[coordinates]
                resquest_base[execl_base_data['number']] = {
                    'name': execl_base_data['name'],
                    'method': execl_base_data['method'],
                    'api': execl_base_data['api'],
                    'params': execl_base_data['params'],
                    'precondition': execl_base_data['precondition'],
                    'expection': execl_base_data['expection'],
                    'status': execl_base_data['status'],
                    'result': execl_base_data['result']
                }
            logger.info("=====测试用例读取完成=====")
            return resquest_base
        except Exception as e:
            logger.warning(e)
            # raise e

    def write_execl_data(self, index, status, result):
        execl_data = pd.DataFrame(data=pd.read_excel(self._filename, sheet_name=0))
        execl_data.loc[index, 'status'] = str(status)
        execl_data.loc[index, 'result'] = str(result)
        pd_write = pd.ExcelWriter(self._filename, sheet_name=0)
        execl_data.to_excel(pd_write)
        pd_write.save()


if __name__ == '__main__':
    filename = '/Users/liuqing/Desktop/apitest/forever/template.xlsx'
    c = GetExeclData(filename=filename).get_execl_data()
    print(c)


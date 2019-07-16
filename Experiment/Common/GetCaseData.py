import pandas as pd



class GetExeclData:

    def __init__(self, filename):
        self._filename = filename

    def get_execl_data_by_pandas(self):
        resquest_base = {}  # 读取全部用例
        execl_data = pd.DataFrame(pd.read_excel(self._filename))
        execl_data = execl_data.fillna(0)
        for coordinates in range(len(execl_data)):
            execl_base_data = execl_data.ix[coordinates]
            resquest_base[execl_base_data['number']] = {
                'method': execl_base_data['method'],
                'api': execl_base_data['api'],
                'params': execl_base_data['params'],
                'precondition': execl_base_data['precondition'],
                'expection': execl_base_data['expection'],
                'status': execl_base_data['status'],
                'result': execl_base_data['result']
            }
        return resquest_base

    def write_execl_data_by_pandas(self, index, status, result):
        execl_data = pd.DataFrame(data=pd.read_excel(self._filename, sheet_name=0))
        execl_data.loc[index, 'status'] = str(status)
        execl_data.loc[index, 'result'] = str(result)
        pd_write = pd.ExcelWriter(self._filename, sheet_name=0)
        execl_data.to_excel(pd_write)
        pd_write.save()


if __name__ == '__main__':
    filename = ''
    c = GetExeclData(filename=filename).get_execl_data_by_pandas()[4]['result']


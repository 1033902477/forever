import time, json
from Experiment.Common.GetCaseData import GetExeclData
from Experiment.InterFace.ExperimentInterFace import InterFaceFirst
from Experiment.CaseFile.TestCasePath import TestCasePath
from Experiment.Log.LogLog import LogDetail


class OperationBaseData(TestCasePath, LogDetail):

    def operation_data(self):
        filename = self.test_case_path()
        base_data = self.__init__base_data()
        data_all = GetExeclData(filename=filename).get_execl_data_by_pandas()
        for base_data['case_number'] in range(len(data_all)):
            coordinate = base_data['case_number'] + 1
            data = data_all[coordinate]
            # print('第{}条用例正在执行'.format(str(coordinate)))
            if data['precondition'] != 0:
                number = data['precondition']
                if data_all[number]['status'] != 'Y':
                    base_data['status'] = 'N'
                    base_data['result'] = 'this test_case is blocked'
                else:
                    response = InterFaceFirst().get_hot_video(method=data['method'],
                                                              path=data['api'],
                                                              params=data['params'])

                    if json.loads(response)['status_code'] == data['expection']:
                        base_data['status'] = 'Y'
                        base_data['result'] = response.encode('utf-8').decode('unicode_escape')
                    else:
                        base_data['status'] = 'N'
                        base_data['result'] = response.encode('utf-8').decode('unicode_escape')
            else:
                response = InterFaceFirst().get_hot_video(method=data['method'],
                                                          path=data['api'],
                                                          params=data['params'])

                if json.loads(response)['status_code'] == data['expection']:
                    base_data['status'] = 'Y'
                    base_data['result'] = response.encode('utf-8').decode('unicode_escape')
                else:
                    base_data['status'] = 'N'
                    base_data['result'] = response.encode('utf-8').decode('unicode_escape')

            GetExeclData(filename=filename).write_execl_data_by_pandas(index=base_data['case_number'],
                                                                       status=base_data['status'],
                                                                       result=base_data['result'])
            # print('第{}条用例执行完毕'.format(str(coordinate)))
            time.sleep(1)


    def __init__base_data(self):
        base_data = {'case_number': 0, 'status': 'Y', 'result': ''}
        return base_data

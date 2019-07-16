import requests
from Experiment.Common.Headers import Headers
from Experiment.Log.LogLog import LogDetail

class ResquestMethodS(Headers, LogDetail):

    def __init__(self, url, method, params):
        self.url = url
        self.method = method
        self.params = params

    def resquest_method(self):
        try:
            response = requests.request(method=self.method, url=self.url, headers=self._headers(), params=self.__resquest_params()).text
            return response
        except Exception as e:
            print(e)

    def __resquest_params(self):
        if self.params != float(0) or int(0):
            if self.method == 'POST':
                self.params = eval(str(self.params))
        else:
            self.params = None
        self.basic_config(info_message='请求方法：' + str(self.method))
        self.basic_config(info_message='请求参数：' + str(self.params))
        return self.params









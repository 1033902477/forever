import requests
from Common.Headers import Headers
from Common.LogLog import logger


class ResquestMethodS(Headers):
    """
    该方法主要是为了更好的进行接口请求，对该模块进行二次封装
    参数介绍
    :url: 接口请求的url
    ：method：当前方法仅支持GET和POST
    :params: 接口传参数，默认为None
    :name:接口名称，默认为None
    """
    def __init__(self, url, method, params=None, name=None):
        self.url = url
        self.method = method
        self.params = params
        self.apiname = name
        super(ResquestMethodS, self).__init__()

    # 接口请求的实际参数
    def rqmethod(self):
        try:
            logger.info("%s接口正在发送请求" % (self.apiname))
            response = requests.request(
                method=self.method,
                url=self.url,
                headers=self._headers,
                params=self.__resquest_params
            )
            logger.info("%s接口请求成功" % (self.apiname))
            return response
        except Exception as e:
            raise e

    @property
    def __resquest_params(self):
        if self.params != '':
            self.params = eval(str(self.params))
        else:
            self.params = None
        return self.params


if __name__ == '__main__':
    RM = ResquestMethodS(url='http://www.baidu.com', params='', method='GET', name='百度')
    text = RM.rqmethod()
    print(text.status_code)







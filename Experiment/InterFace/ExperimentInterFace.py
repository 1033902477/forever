from Experiment.Common.ResquestMethod import ResquestMethodS


class InterFaceFirst():

    def get_hot_video(self, method, path, params):
        url = ''
        response = ResquestMethodS(url=url, method=method, params=params).resquest_method()
        return response


if __name__ == '__main__':
    method = 'POST'
    path = 'kol/task'
    data = ""
    a = InterFaceFirst().get_hot_video(method, path, data)
    print(a)